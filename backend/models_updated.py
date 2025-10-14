from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # admin, verified_leader, pending_leader, user
    verification_status = db.Column(db.String(20), default='none')  # none, pending, approved, rejected
    subscription_status = db.Column(db.String(20), default='trial')  # trial, active, expired, cancelled
    trial_end_date = db.Column(db.DateTime)
    phone_number = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    created_clubs = db.relationship('Club', backref='creator', lazy=True, foreign_keys='Club.created_by')
    created_events = db.relationship('Event', backref='creator', lazy=True, foreign_keys='Event.created_by')
    purchases = db.relationship('Purchase', backref='user', lazy=True, cascade='all, delete-orphan')
    subscriptions = db.relationship('Subscription', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def start_trial(self):
        """Start 2-month trial period for new leaders"""
        self.trial_end_date = datetime.utcnow() + timedelta(days=60)
        self.subscription_status = 'trial'
    
    def is_trial_expired(self):
        """Check if trial period has expired"""
        return self.trial_end_date and datetime.utcnow() > self.trial_end_date
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'verification_status': self.verification_status,
            'subscription_status': self.subscription_status,
            'trial_end_date': self.trial_end_date.isoformat() if self.trial_end_date else None,
            'created_at': self.created_at.isoformat()
        }

class Club(db.Model):
    __tablename__ = 'clubs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    verification_status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    logo_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    events = db.relationship('Event', backref='club', lazy=True)
    
    def to_dict(self, include_events=False):
        result = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_by': self.created_by,
            'creator_name': self.creator.name,
            'verification_status': self.verification_status,
            'logo_url': self.logo_url,
            'event_count': len(self.events),
            'created_at': self.created_at.isoformat()
        }
        
        if include_events:
            result['events'] = [event.to_dict() for event in self.events]
            
        return result

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_paid = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    tickets = db.relationship('Ticket', backref='event', lazy=True, cascade='all, delete-orphan')
    
    def total_revenue(self):
        """Calculate total revenue from all ticket sales"""
        return sum(ticket.total_revenue() for ticket in self.tickets)
    
    def total_tickets_sold(self):
        """Calculate total tickets sold across all ticket types"""
        return sum(ticket.sold_count for ticket in self.tickets)
    
    def to_dict(self, include_tickets=False):
        result = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date.isoformat(),
            'start_time': self.start_time.strftime('%H:%M'),
            'end_time': self.end_time.strftime('%H:%M'),
            'location': self.location,
            'club_id': self.club_id,
            'club_name': self.club.name if self.club else None,
            'created_by': self.created_by,
            'creator_name': self.creator.name,
            'is_paid': self.is_paid,
            'image_url': self.image_url,
            'total_revenue': self.total_revenue(),
            'tickets_sold': self.total_tickets_sold(),
            'created_at': self.created_at.isoformat()
        }
        
        if include_tickets:
            result['tickets'] = [ticket.to_dict() for ticket in self.tickets]
            
        return result

class Ticket(db.Model):
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)  # e.g., "Early Bird", "VIP", "General"
    description = db.Column(db.Text)
    price = db.Column(db.Decimal(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sold_count = db.Column(db.Integer, default=0)
    sale_start_date = db.Column(db.DateTime, default=datetime.utcnow)
    sale_end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    purchases = db.relationship('Purchase', backref='ticket', lazy=True)
    
    def is_available(self):
        """Check if tickets are still available for purchase"""
        now = datetime.utcnow()
        return (self.sold_count < self.quantity and 
                now >= self.sale_start_date and 
                (not self.sale_end_date or now <= self.sale_end_date))
    
    def remaining_quantity(self):
        """Get remaining tickets available"""
        return self.quantity - self.sold_count
    
    def total_revenue(self):
        """Calculate total revenue from this ticket type"""
        return float(self.price) * self.sold_count
    
    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'quantity': self.quantity,
            'sold_count': self.sold_count,
            'remaining': self.remaining_quantity(),
            'is_available': self.is_available(),
            'sale_start_date': self.sale_start_date.isoformat(),
            'sale_end_date': self.sale_end_date.isoformat() if self.sale_end_date else None,
            'total_revenue': self.total_revenue(),
            'created_at': self.created_at.isoformat()
        }

class Purchase(db.Model):
    __tablename__ = 'purchases'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Decimal(10, 2), nullable=False)
    total_amount = db.Column(db.Decimal(10, 2), nullable=False)
    mpesa_code = db.Column(db.String(50))
    payment_phone = db.Column(db.String(15))
    status = db.Column(db.String(20), default='pending')  # pending, completed, failed, refunded
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    commission = db.relationship('Commission', backref='purchase', uselist=False, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_name': self.user.name,
            'ticket_id': self.ticket_id,
            'ticket_name': self.ticket.name,
            'event_title': self.ticket.event.title,
            'quantity': self.quantity,
            'unit_price': float(self.unit_price),
            'total_amount': float(self.total_amount),
            'mpesa_code': self.mpesa_code,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_type = db.Column(db.String(50), nullable=False)  # basic, premium
    monthly_fee = db.Column(db.Decimal(10, 2), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, cancelled, expired
    stripe_subscription_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def is_active(self):
        """Check if subscription is currently active"""
        now = datetime.utcnow()
        return self.status == 'active' and self.start_date <= now <= self.end_date
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'plan_type': self.plan_type,
            'monthly_fee': float(self.monthly_fee),
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'status': self.status,
            'is_active': self.is_active(),
            'created_at': self.created_at.isoformat()
        }

class Commission(db.Model):
    __tablename__ = 'commissions'
    
    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchases.id'), nullable=False)
    platform_fee_rate = db.Column(db.Decimal(5, 4), nullable=False)  # e.g., 0.0500 for 5%
    platform_fee_amount = db.Column(db.Decimal(10, 2), nullable=False)
    organizer_amount = db.Column(db.Decimal(10, 2), nullable=False)
    payout_status = db.Column(db.String(20), default='pending')  # pending, paid, failed
    payout_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'purchase_id': self.purchase_id,
            'platform_fee_rate': float(self.platform_fee_rate),
            'platform_fee_amount': float(self.platform_fee_amount),
            'organizer_amount': float(self.organizer_amount),
            'payout_status': self.payout_status,
            'payout_date': self.payout_date.isoformat() if self.payout_date else None,
            'created_at': self.created_at.isoformat()
        }