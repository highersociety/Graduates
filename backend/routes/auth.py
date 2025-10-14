from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app import db
from models import Student
from schemas import StudentSchema, LoginSchema

auth_bp = Blueprint('auth', __name__)
student_schema = StudentSchema()
login_schema = LoginSchema()

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = login_schema.load(request.json) if 'role' not in request.json else student_schema.load(request.json)
    except ValidationError as err:
        return jsonify({'success': False, 'errors': err.messages}), 400
    
    # Check if user already exists
    if Student.query.filter_by(email=data['email']).first():
        return jsonify({
            'success': False, 
            'errors': {'email': ['Email already registered']}
        }), 400
    
    # Create new student
    student = Student(
        name=data['name'],
        email=data['email'],
        role=data.get('role', 'user')
    )
    student.set_password(data['password'])
    
    db.session.add(student)
    db.session.commit()
    
    # Create access token
    access_token = create_access_token(identity=student.id)
    
    return jsonify({
        'success': True,
        'data': {
            'user': student.to_dict(),
            'token': access_token
        },
        'message': 'Registration successful'
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = login_schema.load(request.json)
    except ValidationError as err:
        return jsonify({'success': False, 'errors': err.messages}), 400
    
    student = Student.query.filter_by(email=data['email']).first()
    
    if not student or not student.check_password(data['password']):
        return jsonify({
            'success': False,
            'errors': {'credentials': ['Invalid email or password']}
        }), 401
    
    access_token = create_access_token(identity=student.id)
    
    return jsonify({
        'success': True,
        'data': {
            'user': student.to_dict(),
            'token': access_token
        },
        'message': 'Login successful'
    }), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    student = Student.query.get(current_user_id)
    
    if not student:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    return jsonify({
        'success': True,
        'data': student.to_dict()
    }), 200