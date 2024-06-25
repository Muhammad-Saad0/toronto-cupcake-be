from fastapi import APIRouter, HTTPException, Request
from models.models import CreateCheckoutSessionRequest
from DB import cupcakes
from settings import Envs
import stripe

router = APIRouter()
stripe.api_key = "sk_test_51NPXIFHhvmEf964AuKLn2JOlLOwnuHAe1PeHLLbu4I2g7taQApo8QoZ6adhrLfUXRQXoH2FUVjMc6Dry0kSRkk7X00VgI3AHEL"
endpoint_secret = "whsec_gDZySJdLOR0hco5VZlmaIyEE1KBSRF7R"

@router.post("/create-stripe-checkout-session")
async def create_checkout_session(request: CreateCheckoutSessionRequest):
    addressData = request.address
    
    try:
        line_items = []
        for item in request.items:
            matching_cupcake = [cupcake for cupcake in cupcakes if cupcake.id == item.item_id][0]
            matching_cupcake.price = matching_cupcake.price * 1.05
            
            line_items.append({
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": matching_cupcake.name,
                        "description": matching_cupcake.description,
                        'images': [matching_cupcake.image],
                    },
                    "unit_amount": int(matching_cupcake.price * 100),
                    },
                "quantity": item.quantity,
            })
        addressData.email
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=f'{Envs.FRONTEND_URL}/Payment_Successfull',
            cancel_url=f'{Envs.FRONTEND_URL}/success',
            metadata={
                "customer_email":addressData.email
            }
        )
        
        return {"id": session.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        handle_successful_payment(session)

    return {"message": "success"}

def handle_successful_payment(session):
    print("Payment was successful!")
    print(f"Session ID: {session['id']}")

    customer_email = session.get('customer_email')
    amount_total = session.get('amount_total') / 100
    currency = session.get('currency')

    metadata = session.get('metadata', {})
    customer_email = metadata.get('customer_email')

    print(f"Customer Email: {customer_email}")
    print(f"Amount Total: {amount_total} {currency}")

    session_id = session['id']
    checkout_session = stripe.checkout.Session.retrieve(session_id, expand=['line_items'])
    line_items = checkout_session['line_items']['data']

    for item in line_items:
        print(f"Item: {item['description']}, Quantity: {item['quantity']}, Price: {item['amount_total'] / 100}")
        
    