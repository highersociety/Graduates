from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from datetime import datetime, timedelta
from app import db
from models import User, Club, Event, Purchase, Commission, Subscription
from schemas import UserSchema, ClubSchema, EventSchema
from decorators import admin_required

admin_bp = Blueprint('admin', __name__)
user_schema = UserSchema()
club_schema = ClubSchema()
event_schema = EventSchema()

@admin_bp.route('/dashboard', methods=['GET'])
@jwt_required()
@admin_required
def admin_dashboard():
    """Get admin dashboard statistics"""
    
    # User statistics
    total_users = User.query.count()
    pending_leaders = User.query.filter_by(verification_status='pending').count()
    verified_leaders = User.query.filter_by(verification_status='approved').count()
    
    # Event statistics
    total_events = Event.query.count()
    paid_events = Event.query.filter_by(is_paid=True).count()
    
    # Revenue statistics
    total_revenue = db.session.query(db.func.sum(Commission.platform_fee_amount)).scalar() or 0
    monthly_revenue = db.session.query(db.func.sum(Commission.platform_fee_amount)).filter(
        Commission.created_at >= datetime.now() - timedelta(days=30)
    ).scalar() or 0
    
    # Recent activity
    recent_purchases = Purchase.query.filter_by(status='completed').order_by(
        Purchase.created_at.desc()
    ).limit(10).all()
    
    return jsonify({
        'success': True,
        'data': {
            'users': {
                'total': total_users,
                'pending_leaders': pending_leaders,
                'verified_leaders': verified_leaders
            },
            'events': {
                'total': total_events,
                'paid_events': paid_events
            },
            'revenue': {
                'total': float(total_revenue),
                'monthly': float(monthly_revenue)
            },
            'recent_purchases': [purchase.to_dict() for purchase in recent_purchases]
        }
    }), 200

@admin_bp.route('/pending-leaders', methods=['GET'])
@jwt_required()
@admin_required
def get_pending_leaders():
    """Get all pending leader applications"""
    
    pending_users = User.query.filter_by(
        verification_status='pending'
    ).order_by(User.created_at.desc()).all()
    
    return jsonify({
        'success': True,
        'data': [user.to_dict() for user in pending_users]
    }), 200

@admin_bp.route('/verify-leader/<int:user_id>', methods=['POST'])
@jwt_required()
@admin_required
def verify_leader(user_id):
    """Approve or reject leader application"""
    
    data = request.json
    action = data.get('action')  # 'approve' or 'reject'
    reason = data.get('reason', '')
    
    if action not in ['approve', 'reject']:
        return jsonify({
            'success': False,
            'message': 'Invalid action. Use "approve" or "reject"'
        }), 400
    
    user = User.query.get_or_404(user_id)
    
    if user.verification_status != 'pending':
        return jsonify({
            'success': False,
            'message': 'User is not pending verification'
        }), 400
    
    if action == 'approve':
        user.verification_status = 'approved'
        user.role = 'verified_leader'
        user.start_trial()  # Start 2-month trial
        
        # TODO: Send approval email
        message = 'Leader application approved successfully'
        
    else:  # reject
        user.verification_status = 'rejected'
        
        # TODO: Send rejection email with reason
        message = 'Leader application rejected'
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': message,
        'data': user.to_dict()
    }), 200

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_all_users():
    """Get all users with filtering options"""
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    role_filter = request.args.get('role')
    status_filter = request.args.get('status')
    
    query = User.query
    
    if role_filter:
        query = query.filter_by(role=role_filter)
    
    if status_filter:
        query = query.filter_by(verification_status=status_filter)
    
    users = query.order_by(User.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'success': True,
        'data': {
            'users': [user.to_dict() for user in users.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': users.total,
                'pages': users.pages
            }
        }
    }), 200

@admin_bp.route('/users/<int:user_id>/suspend', methods=['POST'])
@jwt_required()
@admin_required
def suspend_user(user_id):
    """Suspend or activate user account"""
    
    data = request.json
    action = data.get('action')  # 'suspend' or 'activate'
    reason = data.get('reason', '')
    
    user = User.query.get_or_404(user_id)
    
    if action == 'suspend':
        user.role = 'suspended'
        message = 'User suspended successfully'
    elif action == 'activate':
        # Restore previous role (you might want to store this)
        user.role = 'user'  # Default restoration
        message = 'User activated successfully'
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid action'
        }), 400
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': message
    }), 200

@admin_bp.route('/events', methods=['GET'])
@jwt_required()
@admin_required
def get_all_events():
    """Get all events for admin management"""
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    events = Event.query.order_by(Event.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'success': True,
        'data': {
            'events': [event.to_dict(include_tickets=True) for event in events.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': events.total,
                'pages': events.pages
            }
        }
    }), 200

@admin_bp.route('/events/<int:event_id>/moderate', methods=['POST'])
@jwt_required()
@admin_required
def moderate_event(event_id):
    """Moderate event (approve, reject, or remove)"""
    
    data = request.json
    action = data.get('action')  # 'approve', 'reject', 'remove'
    reason = data.get('reason', '')
    
    event = Event.query.get_or_404(event_id)
    
    if action == 'remove':
        # Check if event has purchases
        if event.total_tickets_sold() > 0:
            return jsonify({
                'success': False,
                'message': 'Cannot remove event with existing ticket sales'
            }), 400
        
        db.session.delete(event)
        message = 'Event removed successfully'
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid action'
        }), 400
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': message
    }), 200

@admin_bp.route('/revenue/analytics', methods=['GET'])
@jwt_required()
@admin_required
def revenue_analytics():
    """Get detailed revenue analytics"""
    
    # Time period filter
    days = request.args.get('days', 30, type=int)
    start_date = datetime.now() - timedelta(days=days)
    
    # Revenue by day
    daily_revenue = db.session.query(
        db.func.date(Commission.created_at).label('date'),
        db.func.sum(Commission.platform_fee_amount).label('revenue')
    ).filter(
        Commission.created_at >= start_date
    ).group_by(
        db.func.date(Commission.created_at)
    ).all()
    
    # Top performing events
    top_events = db.session.query(
        Event.title,
        db.func.sum(Commission.platform_fee_amount).label('revenue')
    ).join(
        Purchase, Purchase.ticket_id == Event.id
    ).join(
        Commission, Commission.purchase_id == Purchase.id
    ).filter(
        Commission.created_at >= start_date
    ).group_by(
        Event.id, Event.title
    ).order_by(
        db.func.sum(Commission.platform_fee_amount).desc()
    ).limit(10).all()
    
    # Revenue by organizer
    organizer_revenue = db.session.query(
        User.name,
        db.func.sum(Commission.platform_fee_amount).label('platform_revenue'),
        db.func.sum(Commission.organizer_amount).label('organizer_revenue')
    ).join(
        Event, Event.created_by == User.id
    ).join(
        Purchase, Purchase.ticket_id == Event.id
    ).join(
        Commission, Commission.purchase_id == Purchase.id
    ).filter(
        Commission.created_at >= start_date
    ).group_by(
        User.id, User.name
    ).order_by(
        db.func.sum(Commission.platform_fee_amount).desc()
    ).limit(10).all()
    
    return jsonify({
        'success': True,
        'data': {
            'daily_revenue': [
                {'date': str(row.date), 'revenue': float(row.revenue)}
                for row in daily_revenue
            ],
            'top_events': [
                {'title': row.title, 'revenue': float(row.revenue)}
                for row in top_events
            ],
            'organizer_revenue': [
                {
                    'organizer': row.name,
                    'platform_revenue': float(row.platform_revenue),
                    'organizer_revenue': float(row.organizer_revenue)
                }
                for row in organizer_revenue
            ]
        }
    }), 200

@admin_bp.route('/commissions/pending-payouts', methods=['GET'])
@jwt_required()
@admin_required
def pending_payouts():
    """Get pending commission payouts"""
    
    pending_commissions = Commission.query.filter_by(
        payout_status='pending'
    ).join(Purchase).join(User).all()
    
    # Group by organizer
    organizer_payouts = {}
    for commission in pending_commissions:
        organizer_id = commission.purchase.ticket.event.created_by
        organizer_name = commission.purchase.ticket.event.creator.name
        
        if organizer_id not in organizer_payouts:
            organizer_payouts[organizer_id] = {
                'organizer_id': organizer_id,
                'organizer_name': organizer_name,
                'total_amount': 0,
                'commission_count': 0
            }
        
        organizer_payouts[organizer_id]['total_amount'] += float(commission.organizer_amount)
        organizer_payouts[organizer_id]['commission_count'] += 1
    
    return jsonify({
        'success': True,
        'data': list(organizer_payouts.values())
    }), 200

@admin_bp.route('/commissions/process-payout', methods=['POST'])
@jwt_required()
@admin_required
def process_payout():
    """Process commission payout to organizer"""
    
    data = request.json
    organizer_id = data.get('organizer_id')
    
    if not organizer_id:
        return jsonify({
            'success': False,
            'message': 'Organizer ID is required'
        }), 400
    
    # Get all pending commissions for this organizer
    pending_commissions = db.session.query(Commission).join(
        Purchase
    ).join(
        Event, Event.id == Purchase.ticket_id
    ).filter(
        Event.created_by == organizer_id,
        Commission.payout_status == 'pending'
    ).all()
    
    if not pending_commissions:
        return jsonify({
            'success': False,
            'message': 'No pending payouts for this organizer'
        }), 400
    
    # Mark commissions as paid
    total_payout = 0
    for commission in pending_commissions:
        commission.payout_status = 'paid'
        commission.payout_date = datetime.utcnow()
        total_payout += float(commission.organizer_amount)
    
    db.session.commit()
    
    # TODO: Integrate with actual payout system (bank transfer, mobile money, etc.)
    
    return jsonify({
        'success': True,
        'message': f'Payout of KES {total_payout:.2f} processed successfully',
        'data': {
            'total_amount': total_payout,
            'commission_count': len(pending_commissions)
        }
    }), 200