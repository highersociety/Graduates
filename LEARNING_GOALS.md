# Learning Goals Mapping

This document maps each curriculum requirement to specific implementation files and code sections in our Campus Event Management System.

## Backend Requirements

### Flask-RESTful API Implementation
- **Location**: `backend/routes/`
- **Files**: 
  - `backend/routes/event_routes.py` - Event CRUD endpoints
  - `backend/routes/club_routes.py` - Club management endpoints
  - `backend/routes/auth.py` - Authentication endpoints
- **Evidence**: RESTful endpoints with proper HTTP methods (GET, POST, PATCH, DELETE)

### SQLAlchemy ORM & Database Design
- **Location**: `backend/models.py`
- **Evidence**: 
  - Student, Club, Event, Registration models
  - Foreign key relationships
  - Many-to-many relationship via Registration table
  - 2NF normalization achieved

### Marshmallow Serialization
- **Location**: `backend/schemas.py`
- **Evidence**: Input validation and JSON serialization for all models

### JWT Authentication
- **Location**: `backend/routes/auth.py`
- **Evidence**: 
  - Login/register endpoints returning JWT tokens
  - Protected routes using `@jwt_required()` decorator

### PostgreSQL Database
- **Location**: `backend/config.py`
- **Evidence**: PostgreSQL connection string and SQLAlchemy configuration

## Frontend Requirements

### React Application
- **Location**: `frontend/src/`
- **Evidence**: Complete React application with components and pages

### React Router v6
- **Location**: `frontend/src/App.jsx`
- **Evidence**: 
  - Route definitions using React Router v6 syntax
  - Protected routes implementation

### React Hook Form
- **Location**: 
  - `frontend/src/components/CreateEventForm.jsx`
  - `frontend/src/components/CreateClubForm.jsx`
- **Evidence**: Form validation and submission handling

### Tailwind CSS Styling
- **Location**: All frontend components
- **Evidence**: Utility-first CSS classes throughout the application

### State Management (Context API)
- **Location**: `frontend/src/context/AppContext.jsx`
- **Evidence**: Global state management for user, events, and clubs

## Advanced Features

### Role-Based Access Control (RBAC)
- **Backend**: `backend/decorators.py` - Role checking decorators
- **Frontend**: Conditional rendering based on user roles
- **Evidence**: Admin, Leader, User roles with specific permissions

### CRUD Operations with Validation
- **Location**: All route files
- **Evidence**: Complete Create, Read, Update, Delete operations with Marshmallow validation

### Pagination
- **Location**: `backend/routes/event_routes.py`, `backend/routes/club_routes.py`
- **Evidence**: Query parameter-based pagination implementation

### Email Integration (SendGrid)
- **Location**: `backend/services/email.py`
- **Evidence**: Email verification and notification system

### Image Handling (Cloudinary)
- **Location**: `backend/services/cloudinary.py`
- **Evidence**: Image upload, resize, and optimization

### API Documentation (Swagger)
- **Location**: `backend/swagger/`
- **Evidence**: OpenAPI specification and Swagger UI integration

## Testing Implementation

### Backend Testing
- **Location**: `tests/`
- **Files**:
  - `tests/test_auth.py` - Authentication endpoint tests
  - `tests/test_events.py` - Event CRUD tests
  - `tests/test_clubs.py` - Club functionality tests
- **Evidence**: pytest test suite with Flask test client

### Seed Data
- **Location**: `backend/seed.py`
- **Evidence**: Sample data creation for demonstration

## Deployment & DevOps

### Version Control (Git/GitHub)
- **Evidence**: Gitflow workflow with main, develop, and feature branches
- **Location**: GitHub repository with proper commit history

### Deployment
- **Backend**: Deployed on Render/Heroku
- **Frontend**: Deployed on Netlify/Vercel
- **Evidence**: Live application URLs and deployment configurations

### Documentation
- **Location**: `README.md`, `docs/`
- **Evidence**: Comprehensive setup instructions and API documentation

## Design Requirements

### Database ERD
- **Tool**: dbdiagram.io
- **Evidence**: Entity Relationship Diagram showing normalized database structure

### UI Mockups
- **Tool**: Figma
- **Evidence**: Complete UI/UX design mockups for all pages

## Code Quality & Best Practices

### Folder Structure
- **Backend**: Modular Flask structure (`app/`, `models/`, `routes/`)
- **Frontend**: Organized React structure (`components/`, `pages/`, `context/`)

### Error Handling
- **Location**: Throughout application
- **Evidence**: Graceful error handling with user-friendly messages

### Security
- **Evidence**: 
  - JWT token management
  - Input sanitization
  - CORS configuration
  - Environment variable usage for secrets

This mapping demonstrates comprehensive coverage of all bootcamp learning objectives through practical implementation in our Campus Event Management System.