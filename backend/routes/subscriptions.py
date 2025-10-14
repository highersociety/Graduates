from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
from app import db
from models import User, Subscription

subscriptions_bp = Blueprint('subscriptions', __name__)

# Subscription plans configuration
SUBSCRIPTION_PLANS = {
    'basic': {
        'name': 'Basic Plan',
        'price': 200.00,  # KES 200/month
        'features': [
            'Create unlimited events',
            'Basic analytics',
            'Standard support',
            'M-Pesa payment processing'
        ]
    },
    'premium': {
        'name': 'Premium Plan', 
        'price': 500.00,  # KES 500/month
        'features': [
            'All Basic features',
            'Advanced analytics',
            'Priority support',
            'Custom branding',
            'Bulk ticket operations',
            'Export reports'
        ]
    }
}

@subscriptions_bp.route('/plans', methods=['GET'])
def get_subscription_plans():
    """Get available subscription plans"""
    return jsonify({
        'success': True,
        'data': SUBSCRIPTION_PLANS
    }), 200

@subscriptions_bp.route('/my-subscription', methods=['GET'])
@jwt_required()
def get_my_subscription():
    """Get current user's subscription status"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    # Get active subscription
    active_subscription = Subscription.query.filter_by(
        user_id=current_user_id,
        status='active'
    ).first()
    
    response_data = {
        'user_id': user.id,
        'subscription_status': user.subscription_status,
        'trial_end_date': user.trial_end_date.isoformat() if user.trial_end_date else None,
        'is_trial_expired': user.is_trial_expired(),
        'active_subscription': active_subscription.to_dict() if active_subscription else None
    }
    
    return jsonify({
        'success': True,
        'data': response_data
    }), 200

@subscriptions_bp.route('/subscribe', methods=['POST'])
@jwt_required()
def create_subscription():
    """Create new subscription for user"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if user.role != 'verified_leader':
        return jsonify({
            'success': False,
            'message': 'Only verified leaders can subscribe'
        }), 403
    
    data = request.json
    plan_type = data.get('plan_type')
    
    if plan_type not in SUBSCRIPTION_PLANS:
        return jsonify({
            'success': False,
            'message': 'Invalid subscription plan'
        }), 400
    
    # Check if user already has active subscription
    existing_subscription = Subscription.query.filter_by(
        user_id=current_user_id,
        status='active'
    ).first()
    
    if existing_subscription:
        return jsonify({
            'success': False,
            'message': 'User already has an active subscription'
        }), 400
    
    # Create new subscription
    plan = SUBSCRIPTION_PLANS[plan_type]
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=30)  # Monthly subscription
    
    subscription = Subscription(
        user_id=current_user_id,
        plan_type=plan_type,
        monthly_fee=plan['price'],
        start_date=start_date,
        end_date=end_date,
        status='active'
    )
    
    # Update user subscription status
    user.subscription_status = 'active'
    
    db.session.add(subscription)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'Successfully subscribed to {plan["name"]}',
        'data': subscription.to_dict()
    }), 201

@subscriptions_bp.route('/cancel', methods=['POST'])
@jwt_required()
def cancel_subscription():
    """Cancel current subscription"""
    current_user_id = get_jwt_identity()
    
    active_subscription = Subscription.query.filter_by(
        user_id=current_user_id,
        status='active'
    ).first()
    
    if not active_subscription:
        return jsonify({
            'success': False,
            'message': 'No active subscription found'
        }), 404
    
    # Cancel subscription (will remain active until end date)
    active_subscription.status = 'cancelled'
    
    # Update user status
    user = User.query.get(current_user_id)
    user.subscription_status = 'cancelled'
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Subscription cancelled successfully. Access will continue until end of billing period.',
        'data': {
            'end_date': active_subscription.end_date.isoformat()
        }
    }), 200

@subscriptions_bp.route('/upgrade', methods=['POST'])
@jwt_required()
def upgrade_subscription():
    """Upgrade subscription plan"""
    current_user_id = get_jwt_identity()
    data = request.json
    new_plan_type = data.get('plan_type')
    
    if new_plan_type not in SUBSCRIPTION_PLANS:
        return jsonify({
            'success': False,
            'message': 'Invalid subscription plan'
        }), 400
    
    active_subscription = Subscription.query.filter_by(
        user_id=current_user_id,
        status='active'
    ).first()
    
    if not active_subscription:
        return jsonify({
            'success': False,
            'message': 'No active subscription found'
        }), 404
    
    if active_subscription.plan_type == new_plan_type:
        return jsonify({
            'success': False,
            'message': 'Already subscribed to this plan'
        }), 400
    
    # Update subscription plan
    new_plan = SUBSCRIPTION_PLANS[new_plan_type]
    active_subscription.plan_type = new_plan_type
    active_subscription.monthly_fee = new_plan['price']
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'Successfully upgraded to {new_plan["name"]}',
        'data': active_subscription.to_dict()
    }), 200