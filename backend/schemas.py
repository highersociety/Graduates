from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime, time

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6), load_only=True)
    role = fields.Str(validate=validate.OneOf(['admin', 'leader', 'user']), missing='user')
    created_at = fields.DateTime(dump_only=True)

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))

class ClubSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    description = fields.Str(validate=validate.Length(max=500))
    created_by = fields.Int(dump_only=True)
    creator_name = fields.Str(dump_only=True)
    member_count = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=2, max=200))
    description = fields.Str(validate=validate.Length(max=1000))
    date = fields.Date(required=True)
    start_time = fields.Time(required=True)
    end_time = fields.Time(required=True)
    location = fields.Str(required=True, validate=validate.Length(min=2, max=200))
    club_id = fields.Int(allow_none=True)
    club_name = fields.Str(dump_only=True)
    created_by = fields.Int(dump_only=True)
    creator_name = fields.Str(dump_only=True)
    capacity = fields.Int(validate=validate.Range(min=1, max=1000), missing=50)
    registered_count = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    
    @validates('date')
    def validate_date(self, value):
        if value < datetime.now().date():
            raise ValidationError('Event date cannot be in the past')
    
    @validates('end_time')
    def validate_end_time(self, value):
        # This validation requires both start_time and end_time to be present
        # In a real application, you might want to use validates_schema for cross-field validation
        pass

class RegistrationSchema(Schema):
    id = fields.Int(dump_only=True)
    student_id = fields.Int(dump_only=True)
    student_name = fields.Str(dump_only=True)
    event_id = fields.Int(dump_only=True)
    status = fields.Str(validate=validate.OneOf(['going', 'interested', 'declined']), missing='going')
    created_at = fields.DateTime(dump_only=True)

class ClubMemberSchema(Schema):
    id = fields.Int(dump_only=True)
    club_id = fields.Int(dump_only=True)
    student_id = fields.Int(dump_only=True)
    student_name = fields.Str(dump_only=True)
    role = fields.Str(validate=validate.OneOf(['leader', 'member']), missing='member')
    joined_at = fields.DateTime(dump_only=True)