from fastapi import APIRouter
import stripe

router = APIRouter(
    prefix='/stripe',
    tags=['Stripe']
)

YOUR_DOMAIN = 'hhtp://localhost'

@router.post('/checkout')
async def stripe_checkout():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # PRICE ID DU PRODUIT QUE VOUS VOULEZ VENDRE
                    'price': 'price_1O51yYAGH7tUuIcUbKRqqIpu',
                    'quantity': 1
                }
            ],
            mode = 'payment',
            succes_url = YOUR_DOMAIN+'/succes.html',
            cancel_url = YOUR_DOMAIN+'/cancel.html'
        )
        return checkout_session
    except Exception as e:
        return str(e)