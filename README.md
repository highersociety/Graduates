# EventHub

**Discover, create and monetize events — all in one platform.**

We built a comprehensive event management platform that connects event organizers with attendees. Our system features ticketing, M-Pesa payments, leader verification, subscription management, and revenue sharing for a complete event marketplace experience.

## Live Demo

- **Frontend**: [Deployed on Netlify/Vercel]
- **Backend API**: [Deployed on Render/Heroku]
- **API Documentation**: [Swagger UI Link]

## Features

Our team focused on creating a comprehensive event marketplace that addresses real-world event management needs:

- **Event Ticketing**: Create paid events with multiple ticket tiers and pricing options
- **M-Pesa Integration**: Seamless mobile money payments for ticket purchases
- **Leader Verification**: Admin-approved verification process for event organizers
- **Subscription System**: Monthly subscription model for verified leaders after 2-month trial
- **Revenue Sharing**: Platform commission system for sustainable business model
- **Club Management**: Organize events under clubs with member management
- **Role-Based Access**: Three-tier system (Admin, Verified Leader, User) with specific permissions
- **Real-time Updates**: Live ticket availability and payment confirmations

## Tech Stack

We chose these technologies based on our learning objectives and industry best practices:

**Backend:**
- Flask + Flask-RESTful
- SQLAlchemy ORM
- PostgreSQL Database
- Marshmallow Serialization
- JWT Authentication
- M-Pesa API Integration
- SendGrid Email Integration
- Cloudinary Image Handling
- Stripe Subscription Management

**Frontend:**
- React 18
- React Router v6
- Context API for State Management
- Tailwind CSS
- React Hook Form
- Axios for API calls

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your database and API keys

# Initialize database
flask db upgrade
python seed.py

# Run server
flask run
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Team Contributors

Our team of six developers collaborated effectively using agile methodologies:

- **Mathew** - Scrum Master & Release Manager - Led project coordination, managed repository setup, handled CI/CD pipeline, and oversaw deployment processes
- **Brenda** - Backend Lead - Architected database models, implemented migrations, developed core API endpoints, and established validation systems
- **Justin** - Club Features Specialist - Built comprehensive club management functionality, created documentation, and prepared demo materials
- **Kish** - Frontend Lead - Designed and implemented event user interfaces, developed RSVP workflows, and integrated Context API
- **Adrian** - QA Lead - Established testing frameworks, created comprehensive seed data, and maintained quality assurance standards
- **Johns** - DevOps & Documentation - Managed deployment infrastructure, created presentation materials, and compiled project documentation

## Database Schema

We designed our database following normalization principles to ensure data integrity:

```sql
User(id, name, email, password_hash, role, verification_status, subscription_status, created_at)
Club(id, name, description, created_by, verification_status, created_at)
Event(id, title, description, date, start_time, end_time, location, club_id, created_by, is_paid, created_at)
Ticket(id, event_id, name, price, quantity, sold_count, created_at)
Purchase(id, user_id, ticket_id, quantity, total_amount, mpesa_code, status, created_at)
Subscription(id, user_id, plan_type, start_date, end_date, status, stripe_subscription_id)
Commission(id, purchase_id, platform_fee, organizer_amount, created_at)
```

## API Endpoints

Our RESTful API follows industry standards for clear and predictable endpoints:

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login

### Clubs
- `GET /api/clubs` - List all clubs
- `POST /api/clubs` - Create new club
- `GET /api/clubs/:id` - Get club details
- `POST /api/clubs/:id/join` - Join club

### Events
- `GET /api/events` - List all events
- `POST /api/events` - Create new event
- `GET /api/events/:id` - Get event details
- `POST /api/events/:id/rsvp` - RSVP to event

## Learning Goals Mapping

This project demonstrates our mastery of key bootcamp concepts:

- **Flask-RESTful APIs**: `backend/routes/*.py`
- **SQLAlchemy ORM**: `backend/models.py`
- **React Router**: `frontend/src/App.jsx`
- **State Management**: `frontend/src/context/AppContext.jsx`
- **Authentication**: `backend/routes/auth.py`
- **Database Design**: Many-to-many relationships in Registration model
- **Responsive Design**: Tailwind CSS throughout frontend
- **Testing**: `tests/` directory with API tests

## Testing

We implemented comprehensive testing to ensure code reliability:

```bash
# Backend tests
cd backend
pytest

# Run with coverage
pytest --cov=app
```

## Deployment

Our deployment strategy focuses on reliability and ease of maintenance:

### Backend (Render/Heroku)
1. Create new service
2. Connect GitHub repo
3. Set environment variables
4. Deploy

### Frontend (Netlify/Vercel)
1. Connect GitHub repo
2. Set build command: `npm run build`
3. Set environment variable: `REACT_APP_API_URL`
4. Deploy

## License

This project is part of Moringa School's Software Development Bootcamp.