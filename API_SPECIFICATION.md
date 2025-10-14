# API Specification

## Base URL
- Development: `http://localhost:5000/api`
- Production: `https://your-backend-url.com/api`

## Authentication
All protected endpoints require JWT token in Authorization header:
```
Authorization: Bearer <jwt_token>
```

## Response Format
All responses follow consistent JSON structure:

**Success Response:**
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}
```

**Error Response:**
```json
{
  "success": false,
  "errors": {
    "field_name": ["Error message"]
  },
  "message": "Validation failed"
}
```

## Authentication Endpoints

### Register User
**POST** `/auth/register`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@campus.edu",
  "password": "SecurePass123",
  "role": "user"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "name": "John Doe",
      "email": "john@campus.edu",
      "role": "user"
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

### Login User
**POST** `/auth/login`

**Request Body:**
```json
{
  "email": "john@campus.edu",
  "password": "SecurePass123"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "name": "John Doe",
      "email": "john@campus.edu",
      "role": "user"
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

## Club Endpoints

### List All Clubs
**GET** `/clubs`

**Query Parameters:**
- `q` (optional): Search clubs by name
- `page` (optional): Page number for pagination (default: 1)
- `per_page` (optional): Items per page (default: 10)

**Response (200):**
```json
{
  "success": true,
  "data": {
    "clubs": [
      {
        "id": 1,
        "name": "Computer Science Club",
        "description": "For CS students and enthusiasts",
        "created_by": 2,
        "creator_name": "Club Leader",
        "member_count": 15,
        "created_at": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "per_page": 10,
      "total": 1,
      "pages": 1
    }
  }
}
```

### Get Club Details
**GET** `/clubs/<id>`

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "Computer Science Club",
    "description": "For CS students and enthusiasts",
    "created_by": 2,
    "creator_name": "Club Leader",
    "members": [
      {
        "id": 3,
        "name": "Student User",
        "role": "member",
        "joined_at": "2024-01-16T09:00:00Z"
      }
    ],
    "events": [
      {
        "id": 1,
        "title": "Tech Talk: AI in Education",
        "date": "2024-02-15",
        "start_time": "14:00",
        "location": "Room 101"
      }
    ],
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

### Create Club
**POST** `/clubs` (Authentication required)

**Request Body:**
```json
{
  "name": "Photography Club",
  "description": "For photography enthusiasts"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": 2,
    "name": "Photography Club",
    "description": "For photography enthusiasts",
    "created_by": 1,
    "created_at": "2024-01-20T14:30:00Z"
  }
}
```

### Update Club
**PATCH** `/clubs/<id>` (Authentication required - Owner/Admin only)

**Request Body:**
```json
{
  "name": "Updated Club Name",
  "description": "Updated description"
}
```

### Delete Club
**DELETE** `/clubs/<id>` (Authentication required - Owner/Admin only)

**Response (204):** No content

### Join Club
**POST** `/clubs/<id>/join` (Authentication required)

**Response (201):**
```json
{
  "success": true,
  "message": "Successfully joined club"
}
```

## Event Endpoints

### List All Events
**GET** `/events`

**Query Parameters:**
- `club_id` (optional): Filter by club
- `date` (optional): Filter by specific date (YYYY-MM-DD)
- `upcoming` (optional): Show only future events (true/false)
- `page` (optional): Page number for pagination
- `per_page` (optional): Items per page

**Response (200):**
```json
{
  "success": true,
  "data": {
    "events": [
      {
        "id": 1,
        "title": "Tech Talk: AI in Education",
        "description": "Discussion on AI applications",
        "date": "2024-02-15",
        "start_time": "14:00",
        "end_time": "16:00",
        "location": "Room 101",
        "club_id": 1,
        "club_name": "Computer Science Club",
        "created_by": 2,
        "creator_name": "Club Leader",
        "capacity": 30,
        "registered_count": 5,
        "created_at": "2024-01-20T10:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "per_page": 10,
      "total": 1,
      "pages": 1
    }
  }
}
```

### Get Event Details
**GET** `/events/<id>`

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "Tech Talk: AI in Education",
    "description": "Discussion on AI applications in modern education",
    "date": "2024-02-15",
    "start_time": "14:00",
    "end_time": "16:00",
    "location": "Room 101",
    "club_id": 1,
    "club_name": "Computer Science Club",
    "created_by": 2,
    "creator_name": "Club Leader",
    "capacity": 30,
    "registered_count": 5,
    "registrations": [
      {
        "id": 1,
        "student_id": 3,
        "student_name": "Student User",
        "status": "going",
        "created_at": "2024-01-21T09:30:00Z"
      }
    ],
    "created_at": "2024-01-20T10:00:00Z"
  }
}
```

### Create Event
**POST** `/events` (Authentication required)

**Request Body:**
```json
{
  "title": "Workshop: Web Development",
  "description": "Hands-on web development workshop",
  "date": "2024-03-01",
  "start_time": "10:00",
  "end_time": "12:00",
  "location": "Lab 201",
  "club_id": 1,
  "capacity": 25
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": 2,
    "title": "Workshop: Web Development",
    "description": "Hands-on web development workshop",
    "date": "2024-03-01",
    "start_time": "10:00",
    "end_time": "12:00",
    "location": "Lab 201",
    "club_id": 1,
    "created_by": 1,
    "capacity": 25,
    "created_at": "2024-01-22T15:00:00Z"
  }
}
```

### Update Event
**PATCH** `/events/<id>` (Authentication required - Owner/Admin/Club Leader only)

### Delete Event
**DELETE** `/events/<id>` (Authentication required - Owner/Admin only)

### RSVP to Event
**POST** `/events/<id>/rsvp` (Authentication required)

**Request Body:**
```json
{
  "status": "going"
}
```

**Valid status values:** `going`, `interested`, `declined`

**Response (201):**
```json
{
  "success": true,
  "data": {
    "registration_id": 1,
    "status": "going",
    "message": "RSVP updated successfully"
  }
}
```

### Cancel Event
**POST** `/events/<id>/cancel` (Authentication required - Owner/Admin only)

## Admin Endpoints

### List All Users
**GET** `/admin/users` (Admin only)

**Response (200):**
```json
{
  "success": true,
  "data": {
    "users": [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@campus.edu",
        "role": "user",
        "created_at": "2024-01-15T08:00:00Z"
      }
    ]
  }
}
```

### Update User Role
**PATCH** `/admin/users/<id>` (Admin only)

**Request Body:**
```json
{
  "role": "leader"
}
```

## Error Codes

- **400 Bad Request**: Invalid request data or validation errors
- **401 Unauthorized**: Missing or invalid authentication token
- **403 Forbidden**: Insufficient permissions for requested action
- **404 Not Found**: Requested resource does not exist
- **409 Conflict**: Resource conflict (e.g., duplicate registration)
- **500 Internal Server Error**: Server-side error

## Rate Limiting

- Authentication endpoints: 5 requests per minute per IP
- General API endpoints: 100 requests per minute per authenticated user
- Public endpoints: 50 requests per minute per IP

## CORS Configuration

The API supports cross-origin requests from approved frontend domains. In development, all origins are allowed for testing purposes.