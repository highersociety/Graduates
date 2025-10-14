# EventHub - Final File Assignments by Team Member

## Project Structure Overview
```
EventHub/
├── backend/
├── frontend/
├── docs/
├── tests/
└── deployment/
```

## Team Member File Ownership

### **Mathew (Scrum Master & Release Manager)**
**Primary Responsibility**: Project coordination, deployment, and integration

**Files to Create/Own:**
```
Root Level:
- README.md
- .gitignore
- PROJECT_TIMELINE.md

Backend Core:
- backend/app.py
- backend/config.py
- backend/requirements.txt

Frontend Setup:
- frontend/package.json
- frontend/vite.config.js
- frontend/tailwind.config.js
- frontend/postcss.config.js

Deployment:
- deployment/README.md
- deployment/render.yaml
- deployment/netlify.toml
- .github/workflows/deploy.yml
```

### **Brenda (Backend Lead)**
**Primary Responsibility**: Database models, core APIs, and M-Pesa integration

**Files to Create/Own:**
```
Backend Models & Core:
- backend/models.py (rename from models_updated.py)
- backend/schemas.py
- backend/decorators.py

API Routes:
- backend/routes/__init__.py
- backend/routes/auth.py
- backend/routes/events.py
- backend/routes/users.py

Database:
- backend/migrations/
- backend/seed.py

Services:
- backend/services/email.py
- backend/services/cloudinary.py
```

### **Justin (Ticketing & Payment Specialist)**
**Primary Responsibility**: Payment integration and ticketing system

**Files to Create/Own:**
```
Payment System:
- backend/routes/payments.py
- backend/routes/tickets.py
- backend/services/mpesa.py

Frontend Payment Components:
- frontend/src/components/TicketCard.jsx
- frontend/src/components/CheckoutForm.jsx
- frontend/src/components/PaymentStatus.jsx
- frontend/src/pages/TicketPurchase.jsx

Documentation:
- docs/PAYMENT_INTEGRATION.md
- docs/MPESA_SETUP.md
```

### **Kish (Frontend Lead)**
**Primary Responsibility**: React application, UI/UX, and state management

**Files to Create/Own:**
```
Core React App:
- frontend/src/App.jsx
- frontend/src/main.jsx
- frontend/src/index.css

Context & Services:
- frontend/src/context/AppContext.jsx
- frontend/src/context/PaymentContext.jsx
- frontend/src/services/api.js

Main Pages:
- frontend/src/pages/Home.jsx
- frontend/src/pages/Login.jsx
- frontend/src/pages/Register.jsx
- frontend/src/pages/Events.jsx
- frontend/src/pages/EventDetails.jsx
- frontend/src/pages/Dashboard.jsx
- frontend/src/pages/OrganizerDashboard.jsx

Core Components:
- frontend/src/components/Navbar.jsx
- frontend/src/components/EventCard.jsx
- frontend/src/components/ProtectedRoute.jsx
- frontend/src/components/LoadingSpinner.jsx

Utilities:
- frontend/src/utils/formatters.js
- frontend/src/utils/validators.js
```

### **Adrian (QA Lead)**
**Primary Responsibility**: Testing, quality assurance, and data management

**Files to Create/Own:**
```
Testing Framework:
- tests/__init__.py
- tests/conftest.py
- tests/test_auth.py
- tests/test_events.py
- tests/test_payments.py
- tests/test_subscriptions.py

Quality Assurance:
- QA_CHECKLIST.md
- docs/TESTING.md
- docs/API_TESTING.md

Data Management:
- backend/seed_data/users.json
- backend/seed_data/events.json
- backend/seed_data/sample_data.py

Performance Testing:
- tests/performance/load_tests.py
- tests/performance/stress_tests.py
```

### **Johns (Admin Panel & Documentation)**
**Primary Responsibility**: Admin features, documentation, and final deliverables

**Files to Create/Own:**
```
Admin System:
- backend/routes/admin.py
- backend/routes/subscriptions.py
- frontend/src/pages/AdminPanel.jsx
- frontend/src/pages/AdminDashboard.jsx
- frontend/src/components/AdminSidebar.jsx

Club Management:
- backend/routes/clubs.py
- frontend/src/pages/Clubs.jsx
- frontend/src/pages/ClubDetails.jsx
- frontend/src/components/CreateClubForm.jsx

Documentation:
- CLOSURE_REPORT.md
- LEARNING_GOALS.md
- PRESENTATION_SCRIPT.md
- FIGMA_DESIGN_BRIEF.md
- EVENTHUB_FEATURES.md

Marketing Materials:
- marketing/product_overview.pdf
- marketing/business_model.md
- slides/presentation.pdf
```

## Collaboration Guidelines

### **Cross-Team Files (Shared Ownership)**
```
Shared Backend:
- backend/routes/__init__.py (Brenda + others)
- backend/utils/ (All backend contributors)

Shared Frontend:
- frontend/src/hooks/ (Kish + others)
- frontend/src/styles/ (Kish + Justin for payment styles)

Documentation:
- README.md (Mathew leads, all contribute)
- API documentation (Brenda + Justin for payments)
```

### **File Creation Timeline**
```
Day 1-2: Core structure (Mathew, Brenda, Kish)
Day 3-4: Feature implementation (Justin, Adrian setup)
Day 5-6: Integration and testing (All team members)
Day 7-8: Polish and documentation (Johns, Adrian)
Day 9-10: Final review and deployment (Mathew, all)
```

### **Git Workflow**
```
Branch Structure:
- main (production)
- develop (integration)
- feature/payment-integration (Justin)
- feature/admin-panel (Johns)
- feature/frontend-ui (Kish)
- feature/auth-system (Brenda)
- feature/testing (Adrian)
- deployment/production (Mathew)
```

### **Code Review Assignments**
```
Payment Code: Brenda reviews Justin's work
Frontend Code: Justin reviews Kish's work
Backend APIs: Kish reviews Brenda's work
Admin Features: Adrian reviews Johns's work
Testing Code: Johns reviews Adrian's work
Deployment: All review Mathew's work
```

### **Final Integration Checklist**
```
Mathew: Ensure all branches merge cleanly
Brenda: Verify API endpoints work with frontend
Justin: Test payment flows end-to-end
Kish: Confirm UI/UX consistency across features
Adrian: Run full test suite and QA checklist
Johns: Complete documentation and admin features
```

This structure ensures each team member has clear ownership while maintaining collaborative development practices. The file assignments reflect realistic contributions that would be expected from each role in a professional development environment.