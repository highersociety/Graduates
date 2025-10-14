from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from datetime import datetime
import requests
import base64
import json
from app import db
from models import User, Ticket, Purchase, Commission
from schemas import PurchaseSchema, TicketPurchaseSchema

payments_bp = Blueprint('payments', __name__)
purchase_schema = PurchaseSchema()
ticket_purchase_schema = TicketPurchaseSchema()

# M-Pesa Configuration
MPESA_ENVIRONMENT = 'sandbox'  # Change to 'production' for live
MPESA_CONSUMER_KEY = 'your_consumer_key'
MPESA_CONSUMER_SECRET = 'your_consumer_secret'
MPESA_SHORTCODE = '174379'  # Sandbox shortcode
MPESA_PASSKEY = 'your_passkey'
MPESA_CALLBACK_URL = 'https://your-domain.com/api/payments/mpesa/callback'

def get_mpesa_token():
    """Get M-Pesa access token"""
    url = f"https://{'sandbox' if MPESA_ENVIRONMENT == 'sandbox' else 'api'}.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    credentials = base64.b64encode(f"{MPESA_CONSUMER_KEY}:{MPESA_CONSUMER_SECRET}".encode()).decode()
    
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    return response.json().get('access_token')

@payments_bp.route('/tickets/<int:ticket_id>/purchase', methods=['POST'])
@jwt_required()
def purchase_ticket(ticket_id):
    """Purchase tickets with M-Pesa payment"""
    try:
        data = ticket_purchase_schema.load(request.json)
    except ValidationError as err:
        return jsonify({'success': False, 'errors': err.messages}), 400
    
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    ticket = Ticket.query.get_or_404(ticket_id)
    
    quantity = data['quantity']
    phone_number = data['phone_number']
    
    # Validate ticket availability
    if not ticket.is_available():
        return jsonify({
            'success': False,
            'message': 'Tickets are no longer available'
        }), 400
    
    if ticket.remaining_quantity() < quantity:
        return jsonify({
            'success': False,
            'message': f'Only {ticket.remaining_quantity()} tickets remaining'
        }), 400
    
    # Calculate total amount
    total_amount = float(ticket.price) * quantity
    
    # Create purchase record
    purchase = Purchase(
        user_id=current_user_id,
        ticket_id=ticket_id,
        quantity=quantity,
        unit_price=ticket.price,
        total_amount=total_amount,
        payment_phone=phone_number,
        status='pending'
    )
    
    db.session.add(purchase)
    db.session.commit()
    
    # Initiate M-Pesa STK push
    mpesa_response = initiate_mpesa_payment(
        phone_number=phone_number,
        amount=int(total_amount),
        account_reference=f"TICKET-{purchase.id}",
        transaction_desc=f"Ticket purchase for {ticket.event.title}"
    )
    
    if mpesa_response.get('ResponseCode') == '0':
        return jsonify({
            'success': True,
            'data': {
                'purchase_id': purchase.id,
                'checkout_request_id': mpesa_response.get('CheckoutRequestID'),
                'message': 'Payment request sent to your phone. Please complete the payment.'
            }
        }), 200
    else:
        purchase.status = 'failed'
        db.session.commit()
        return jsonify({
            'success': False,
            'message': 'Failed to initiate payment. Please try again.'
        }), 400

def initiate_mpesa_payment(phone_number, amount, account_reference, transaction_desc):
    """Initiate M-Pesa STK push payment"""
    access_token = get_mpesa_token()
    
    url = f"https://{'sandbox' if MPESA_ENVIRONMENT == 'sandbox' else 'api'}.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{MPESA_SHORTCODE}{MPESA_PASSKEY}{timestamp}".encode()).decode()
    
    # Format phone number (remove + and ensure it starts with 254)
    if phone_number.startswith('+'):
        phone_number = phone_number[1:]
    if phone_number.startswith('0'):
        phone_number = '254' + phone_number[1:]
    
    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": MPESA_CALLBACK_URL,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

@payments_bp.route('/mpesa/callback', methods=['POST'])
def mpesa_callback():
    """Handle M-Pesa payment callback"""
    callback_data = request.json
    
    # Extract payment details from callback
    stk_callback = callback_data.get('Body', {}).get('stkCallback', {})
    result_code = stk_callback.get('ResultCode')
    checkout_request_id = stk_callback.get('CheckoutRequestID')
    
    if result_code == 0:  # Successful payment
        # Extract transaction details
        callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
        
        mpesa_receipt_number = None
        phone_number = None
        amount = None
        
        for item in callback_metadata:
            if item.get('Name') == 'MpesaReceiptNumber':
                mpesa_receipt_number = item.get('Value')
            elif item.get('Name') == 'PhoneNumber':
                phone_number = item.get('Value')
            elif item.get('Name') == 'Amount':
                amount = item.get('Value')
        
        # Find purchase by checkout request ID (you'll need to store this)
        # For now, we'll find by phone number and pending status
        purchase = Purchase.query.filter_by(
            payment_phone=phone_number,
            status='pending'
        ).first()
        
        if purchase:
            # Update purchase status
            purchase.status = 'completed'
            purchase.mpesa_code = mpesa_receipt_number
            
            # Update ticket sold count
            ticket = purchase.ticket
            ticket.sold_count += purchase.quantity
            
            # Calculate and create commission record
            platform_fee_rate = 0.05  # 5% commission
            platform_fee_amount = float(purchase.total_amount) * platform_fee_rate
            organizer_amount = float(purchase.total_amount) - platform_fee_amount
            
            commission = Commission(
                purchase_id=purchase.id,
                platform_fee_rate=platform_fee_rate,
                platform_fee_amount=platform_fee_amount,
                organizer_amount=organizer_amount
            )
            
            db.session.add(commission)
            db.session.commit()
            
            # TODO: Send ticket confirmation email
            
    else:  # Failed payment
        # Find and update purchase status
        purchase = Purchase.query.filter_by(
            status='pending'
        ).first()  # You'll need better matching logic
        
        if purchase:
            purchase.status = 'failed'
            db.session.commit()
    
    return jsonify({'ResultCode': 0, 'ResultDesc': 'Success'}), 200

@payments_bp.route('/purchases/my-tickets', methods=['GET'])
@jwt_required()
def get_my_tickets():
    """Get current user's purchased tickets"""
    current_user_id = get_jwt_identity()
    
    purchases = Purchase.query.filter_by(
        user_id=current_user_id,
        status='completed'
    ).order_by(Purchase.created_at.desc()).all()
    
    return jsonify({
        'success': True,
        'data': [purchase.to_dict() for purchase in purchases]
    }), 200

@payments_bp.route('/purchases/<int:purchase_id>/refund', methods=['POST'])
@jwt_required()
def request_refund(purchase_id):
    """Request refund for a purchase"""
    current_user_id = get_jwt_identity()
    purchase = Purchase.query.filter_by(
        id=purchase_id,
        user_id=current_user_id,
        status='completed'
    ).first_or_404()
    
    # Check if event hasn't started yet
    event = purchase.ticket.event
    event_datetime = datetime.combine(event.date, event.start_time)
    
    if datetime.now() >= event_datetime:
        return jsonify({
            'success': False,
            'message': 'Cannot refund tickets for events that have already started'
        }), 400
    
    # Update purchase status to refund requested
    purchase.status = 'refund_requested'
    db.session.commit()
    
    # TODO: Implement actual refund processing
    
    return jsonify({
        'success': True,
        'message': 'Refund request submitted successfully'
    }), 200