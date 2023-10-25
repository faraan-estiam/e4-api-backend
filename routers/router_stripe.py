from fastapi import APIRouter, Header, Request
from configs.stripe_config import stripe_config
import stripe

router = APIRouter(
    prefix='/stripe',
    tags=['Stripe']
)

#votre test secret API Key
stripe.api_key = stripe_config['secret_key']

YOUR_DOMAIN = 'http://localhost'

@router.post('/checkout')
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
            payment_method_types = ['Card'],
            succes_url = YOUR_DOMAIN+'/succes.html',
            cancel_url = YOUR_DOMAIN+'/cancel.html'
        )
        return checkout_session
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
    elif event_type == 'invoice.paid': print('Invoice paid')
    elif event_type == 'invoice.payment_failed': print('Invoice payment failed')
    else : print(f'Unhandled event: {event_type}')