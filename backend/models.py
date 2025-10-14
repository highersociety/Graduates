from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # admin, leader, user
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    created_clubs = db.relationship('Club', backref='creator', lazy=True, foreign_keys='Club.created_by')
    created_events = db.relationship('Event', backref='creator', lazy=True, foreign_keys='Event.created_by')
    registrations = db.relationship('Registration', backref='student', lazy=True, cascade='all, delete-orphan')
    club_memberships = db.relationship('ClubMember', backref='student', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }

class Club(db.Model):
    __tablename__ = 'clubs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    events = db.relationship('Event', backref='club', lazy=True)
    members = db.relationship('ClubMember', backref='club', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self, include_members=False, include_events=False):
        result = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_by': self.created_by,
            'creator_name': self.creator.name,
            'member_count': len(self.members),
            'created_at': self.created_at.isoformat()
        }
        
        if include_members:
            result['members'] = [member.to_dict() for member in self.members]
        
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
    created_by = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    capacity = db.Column(db.Integer, default=50)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    registrations = db.relationship('Registration', backref='event', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self, include_registrations=False):
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
            'capacity': self.capacity,
            'registered_count': len(self.registrations),
            'created_at': self.created_at.isoformat()
        }
        
        if include_registrations:
            result['registrations'] = [reg.to_dict() for reg in self.registrations]
            
        return result

class Registration(db.Model):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    status = db.Column(db.String(20), default='going')  # going, interested, declined
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('student_id', 'event_id'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'student_name': self.student.name,
            'event_id': self.event_id,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

class ClubMember(db.Model):
    __tablename__ = 'club_members'
    
    id = db.Column(db.Integer, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    role = db.Column(db.String(20), default='member')  # leader, member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('club_id', 'student_id'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'club_id': self.club_id,
            'student_id': self.student_id,
            'student_name': self.student.name,
            'role': self.role,
            'joined_at': self.joined_at.isoformat()
        }