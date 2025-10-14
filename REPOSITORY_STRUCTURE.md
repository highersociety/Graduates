# EventHub - Complete Repository Structure

## Repository Overview
This is the complete EventHub project repository with all files organized for team collaboration.

## Project Structure
```
EventHub/
├── README.md
├── PROJECT_TIMELINE.md
├── TEAM_ROLES.md
├── LEARNING_GOALS.md
├── CLOSURE_REPORT.md
├── PRESENTATION_SCRIPT.md
├── QA_CHECKLIST.md
├── EVENTHUB_FEATURES.md
├── DATABASE_SCHEMA.md
├── API_SPECIFICATION.md
├── FIGMA_DESIGN_BRIEF.md
├── FINAL_FILE_ASSIGNMENTS.md
├── .gitignore
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py (rename from models_updated.py)
│   ├── schemas.py
│   ├── requirements.txt
│   ├── seed.py
│   ├── .env.example
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── events.py
│   │   ├── clubs.py
│   │   ├── payments.py
│   │   ├── admin.py
│   │   └── subscriptions.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── mpesa.py
│   │   └── cloudinary.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_events.py
│   │   ├── test_payments.py
│   │   └── test_admin.py
│   └── migrations/
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── index.html
│   ├── public/
│   │   └── favicon.ico
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── index.css
│       ├── components/
│       │   ├── Navbar.jsx
│       │   ├── EventCard.jsx
│       │   ├── TicketCard.jsx
│       │   ├── CheckoutForm.jsx
│       │   ├── ProtectedRoute.jsx
│       │   ├── CreateClubForm.jsx
│       │   └── LoadingSpinner.jsx
│       ├── pages/
│       │   ├── Home.jsx
│       │   ├── Login.jsx
│       │   ├── Register.jsx
│       │   ├── Events.jsx
│       │   ├── EventDetails.jsx
│       │   ├── Clubs.jsx
│       │   ├── ClubDetails.jsx
│       │   ├── Dashboard.jsx
│       │   ├── OrganizerDashboard.jsx
│       │   └── AdminPanel.jsx
│       ├── context/
│       │   ├── AppContext.jsx
│       │   └── PaymentContext.jsx
│       ├── services/
│       │   └── api.js
│       └── utils/
│           ├── formatters.js
│           └── validators.js
├── docs/
│   ├── PAYMENT_INTEGRATION.md
│   ├── MPESA_SETUP.md
│   ├── TESTING.md
│   └── DEPLOYMENT.md
└── deployment/
    ├── README.md
    ├── render.yaml
    └── netlify.toml
```

## Team Access Instructions

### 1. Repository Setup (Mathew)
```bash
# Initialize repository
git init
git add .
git commit -m "Initial EventHub project setup"
git branch -M main
git remote add origin https://github.com/your-username/eventhub.git
git push -u origin main

# Create development branch
git checkout -b develop
git push -u origin develop
```

### 2. Team Member Setup
Each team member should:
```bash
# Clone repository
git clone https://github.com/your-username/eventhub.git
cd eventhub

# Create feature branch
git checkout develop
git checkout -b feature/your-feature-name

# Install dependencies
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
```

### 3. File Ownership by Team Member

#### Mathew (Scrum Master)
```
Primary Files:
- README.md
- PROJECT_TIMELINE.md
- backend/app.py
- backend/config.py
- frontend/package.json
- frontend/vite.config.js
- deployment/
```

#### Brenda (Backend Lead)
```
Primary Files:
- backend/models.py
- backend/schemas.py
- backend/routes/auth.py
- backend/routes/events.py
- backend/seed.py
- backend/services/email.py
```

#### Justin (Payment Specialist)
```
Primary Files:
- backend/routes/payments.py
- backend/services/mpesa.py
- frontend/src/components/TicketCard.jsx
- frontend/src/components/CheckoutForm.jsx
- docs/PAYMENT_INTEGRATION.md
```

#### Kish (Frontend Lead)
```
Primary Files:
- frontend/src/App.jsx
- frontend/src/context/AppContext.jsx
- frontend/src/pages/Login.jsx
- frontend/src/pages/Events.jsx
- frontend/src/pages/Dashboard.jsx
- frontend/src/components/Navbar.jsx
```

#### Adrian (QA Lead)
```
Primary Files:
- QA_CHECKLIST.md
- backend/tests/
- docs/TESTING.md
- backend/seed.py (collaborate with Brenda)
```

#### Johns (Admin & Documentation)
```
Primary Files:
- backend/routes/admin.py
- backend/routes/subscriptions.py
- frontend/src/pages/AdminPanel.jsx
- CLOSURE_REPORT.md
- PRESENTATION_SCRIPT.md
- FIGMA_DESIGN_BRIEF.md
```

## Development Workflow

### Branch Strategy
```
main (production)
├── develop (integration)
├── feature/payment-integration (Justin)
├── feature/admin-panel (Johns)
├── feature/frontend-ui (Kish)
├── feature/auth-system (Brenda)
└── feature/testing (Adrian)
```

### Daily Workflow
1. Pull latest changes from develop
2. Work on assigned files
3. Commit changes with descriptive messages
4. Push to feature branch
5. Create PR to develop branch
6. Request review from assigned reviewer

### Code Review Assignments
- Payment code: Brenda reviews Justin
- Frontend code: Justin reviews Kish
- Backend APIs: Kish reviews Brenda
- Admin features: Adrian reviews Johns
- Testing: Johns reviews Adrian
- Integration: Mathew reviews all

## Environment Setup

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
flask db upgrade
python seed.py
flask run
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Important Notes

### File Naming Conventions
- Use kebab-case for files: `user-dashboard.jsx`
- Use PascalCase for React components: `UserDashboard`
- Use snake_case for Python files: `user_routes.py`

### Commit Message Format
```
type(scope): description

Examples:
feat(payment): add M-Pesa STK push integration
fix(auth): resolve JWT token expiration issue
docs(readme): update setup instructions
test(payment): add M-Pesa callback tests
```

### Environment Variables Required
```
# Backend (.env)
DATABASE_URL=postgresql://username:password@localhost/eventhub
JWT_SECRET_KEY=your-secret-key
MPESA_CONSUMER_KEY=your-mpesa-key
MPESA_CONSUMER_SECRET=your-mpesa-secret
SENDGRID_API_KEY=your-sendgrid-key
CLOUDINARY_URL=your-cloudinary-url

# Frontend (.env)
VITE_API_URL=http://localhost:5000/api
VITE_MPESA_SHORTCODE=174379
```

## Getting Started Checklist

### For Each Team Member:
- [ ] Clone repository
- [ ] Create feature branch
- [ ] Install dependencies
- [ ] Set up environment variables
- [ ] Run application locally
- [ ] Review assigned files
- [ ] Start development on assigned features

### For Project Setup:
- [ ] Create GitHub repository
- [ ] Set up branch protection rules
- [ ] Configure CI/CD pipeline
- [ ] Set up deployment environments
- [ ] Create project board
- [ ] Invite all team members

This structure ensures everyone has clear ownership while maintaining collaborative development practices.