from fastapi import APIRouter, Header, Request, Depends, Body
from fastapi.responses import RedirectResponse
import stripe
from firebase_admin import auth
from database.firebase import db
from routers.router_auth import get_current_user

from dotenv import dotenv_values
import json
stripe_config = json.loads(dotenv_values(dotenv_path='.env')['STRIPE_CONFIG'])
stripe.api_key = stripe_config['private_key']

router = APIRouter(
    prefix='/stripe',
    tags=['Stripe']
)



YOUR_DOMAIN = 'http://localhost'

@router.get('/checkout')
async def stripe_checkout():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # PRICE ID DU PRODUIT QUE VOUS VOULEZ VENDRE
                    'price': stripe_config['price_id'],
                    'quantity': 1
                }
            ],
            mode = 'subscription',
            payment_method_types = ['card'],
            success_url = YOUR_DOMAIN+'/success.html',
            cancel_url = YOUR_DOMAIN+'/cancel.html'
        )
        response = RedirectResponse(checkout_session['url'])
        return response
    except Exception as e:
        return str(e)
    
@router.post('/webhook')
async def webhook_received(request:Request, stripe_signature: str = Header(None)):
    webhook_secret = stripe_config['webhook_secret']
    data = await request.body
    try:
        event = stripe.Webhook.construct_event(
            payload=data,
            sig_header=stripe_signature,
            secret=webhook_secret
        )
        event_data = event['data']
    except Exception as e:
        return {'error':str(e)}
    
    event_type = event ['type']
    if event_type == 'checkout.session.completed': print('Checkout session completed')
    elif event_type == 'invoice.paid':
        print('Invoice paid')
        customer_email = event_data['object']['customer_email']
        firebase_user = auth.get_user_by_email(customer_email)
        customer_id = event_data['object']['customer']
        item_id = event_data['object']['lines']['data'][0]['subscription_item']
        db.child('users').child(firebase_user.uid).child('stripe').set(
            data={
                'item_id':item_id,
                'customer_id':customer_id
            }
        )
    elif event_type == 'invoice.payment_failed': print('Invoice payment failed')
    else : print(f'Unhandled event: {event_type}')

@router.get('/usage')
async def stripe_usage(userData: int = Depends(get_current_user)):
    fireBase_user= auth.get_user(userData['uid'])
    stripe_data= db.child("users").child(fireBase_user.uid).child("stripe").get().val()
    cust_id = stripe_data["cust_id"]
    return stripe.Invoice.upcoming(customer=cust_id)

def increment_stripe(userId:str):
    firebase_user = auth.get_user(userId)
    stripe_data = db.child('users').child(firebase_user.uid).child('stripe').get().val()
    print(stripe_data.values())
    item_id = stripe_data['item_id']
    stripe.SubscriptionItem.create_usage_record(id=item_id, quantity=1)
    return