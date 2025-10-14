# Team Roles & Detailed Responsibilities

## Mathew — Scrum Master & Release Manager (Project Lead)

**Primary Focus**: Project coordination, code integration, deployment, and final delivery

### Core Responsibilities
- Facilitate daily stand-up meetings and remove development blockers
- Manage GitHub repository with proper branch protection and merge policies
- Review and approve all pull requests before merging to development branch
- Coordinate final merge from development to main branch
- Deploy both backend and frontend to production environments
- Prepare final closure report and ensure all deliverables are complete

### Key Files & Components
- Repository setup and configuration
- CI/CD pipeline configuration
- Pull request reviews for all feature branches
- Final release branch (release/v1.0) management
- Deployment documentation and scripts

### Daily Objectives
- Conduct team stand-up and track progress against timeline
- Review completed work and unblock any development issues
- Ensure continuous integration pipeline remains functional
- Coordinate between team members to prevent merge conflicts

---

## Brenda — Backend Lead (Flask & Database Specialist)

**Primary Focus**: Database architecture, API development, and backend infrastructure

### Core Responsibilities
- Design and implement all database models with proper relationships
- Create Flask application structure with blueprints and configuration
- Develop RESTful API endpoints for events, clubs, and authentication
- Implement Marshmallow schemas for data validation and serialization
- Set up JWT authentication system with role-based permissions
- Configure CORS, database connections, and application factory pattern
- Create comprehensive seed data for testing and demonstration

### Key Files & Components
- `backend/models.py` - All database models and relationships
- `backend/app.py` - Flask application factory and blueprint registration
- `backend/routes/event_routes.py` - Event CRUD operations and RSVP logic
- `backend/routes/auth.py` - Authentication endpoints with JWT implementation
- `backend/schemas.py` - Marshmallow validation schemas
- `backend/seed.py` - Database seeding script
- `backend/config.py` - Application configuration and environment setup

### Daily Objectives
- Complete at least one fully tested API endpoint per day
- Ensure all endpoints include proper validation and error handling
- Maintain database integrity and optimize query performance
- Collaborate with frontend team on API contract definitions

---

## Justin — Club Features Specialist (Full-Stack Club Domain)

**Primary Focus**: Complete club management system and project documentation

### Core Responsibilities
- Implement comprehensive club CRUD operations (backend and frontend)
- Build club administration features with leader permission controls
- Create club detail pages with member management functionality
- Develop club creation and editing forms with proper validation
- Write detailed documentation for club features with screenshots
- Prepare demonstration script for club creation and management workflow
- Ensure club-event relationship functionality works seamlessly

### Key Files & Components
- `backend/routes/club_routes.py` - Club API endpoints with permission checks
- `frontend/src/pages/Clubs.jsx` - Club listing and search functionality
- `frontend/src/pages/ClubDetail.jsx` - Individual club management interface
- `frontend/src/components/CreateClubForm.jsx` - Club creation form component
- `frontend/src/components/ClubCard.jsx` - Club display component
- `docs/CLUB_FEATURES.md` - Comprehensive club feature documentation

### Daily Objectives
- Achieve working integration between club backend and frontend components
- Implement and test club leader permission system
- Create user-friendly interfaces for club management tasks
- Document all club-related features with clear usage instructions

---

## Kish — Frontend Lead (React & User Experience)

**Primary Focus**: Event interfaces, user experience, and frontend architecture

### Core Responsibilities
- Build comprehensive event listing and detail pages
- Implement RSVP functionality with real-time UI updates
- Create user dashboard showing personal events and club memberships
- Develop Context API for global state management
- Integrate API services for seamless backend communication
- Ensure responsive design across all device sizes
- Implement user authentication flows and protected routes

### Key Files & Components
- `frontend/src/pages/Home.jsx` - Landing page with featured events
- `frontend/src/pages/Events.jsx` - Event listing with filtering options
- `frontend/src/pages/EventDetails.jsx` - Event detail page with RSVP functionality
- `frontend/src/components/EventCard.jsx` - Reusable event display component
- `frontend/src/components/RsvpButton.jsx` - Interactive RSVP component
- `frontend/src/context/AppContext.jsx` - Global state management
- `frontend/src/services/api.js` - API integration layer

### Daily Objectives
- Ensure event listing displays real data from backend API
- Complete RSVP workflow with proper state management
- Maintain consistent user experience across all pages
- Optimize component performance and loading states

---

## Adrian — Quality Assurance Lead (Testing & Data Management)

**Primary Focus**: Testing infrastructure, data integrity, and quality assurance

### Core Responsibilities
- Create comprehensive seed script with realistic sample data
- Write unit tests for all critical API endpoints using pytest
- Develop manual testing checklist covering all user workflows
- Perform regression testing after major feature implementations
- Ensure data consistency and proper error handling
- Validate API responses and frontend error states
- Document testing procedures and maintain QA standards

### Key Files & Components
- `backend/seed.py` - Comprehensive database seeding with sample users, clubs, and events
- `tests/test_auth.py` - Authentication endpoint testing
- `tests/test_events.py` - Event CRUD and RSVP testing
- `tests/test_clubs.py` - Club functionality testing
- `docs/QA_CHECKLIST.md` - Manual testing procedures
- Test configuration and fixtures

### Daily Objectives
- Maintain functional seed script that creates realistic demo environment
- Ensure all new features include appropriate test coverage
- Perform daily smoke tests on integrated features
- Document any bugs or issues for immediate resolution

---

## Johns — DevOps & Documentation Specialist (Infrastructure & Presentation)

**Primary Focus**: Deployment, documentation, and presentation materials

### Core Responsibilities
- Deploy backend application to production hosting platform
- Deploy frontend application with proper environment configuration
- Create comprehensive presentation slides with speaker notes
- Compile final closure report with team reflections and lessons learned
- Generate marketing materials and product summary documentation
- Ensure all deployment environments are stable and accessible
- Coordinate final project submission and deliverable organization

### Key Files & Components
- `deployment/README.md` - Deployment procedures and configuration
- `slides/presentation.pdf` - Team presentation with speaker notes
- `Closure_Report.pdf` - Final project summary and team reflections
- `marketing/product_summary.pdf` - Marketing materials and feature overview
- Environment configuration files and deployment scripts

### Daily Objectives
- Maintain accessible deployed backend with at least one working endpoint
- Ensure frontend deployment reflects latest development changes
- Progress on presentation materials and final documentation
- Coordinate with team on deployment requirements and configurations

## Team Collaboration Guidelines

### Communication Protocols
- Daily stand-ups at 9:00 AM (10 minutes maximum)
- Slack for immediate questions and coordination
- GitHub for technical discussions and code reviews
- Weekly progress reviews to assess timeline adherence

### Code Review Process
- All features developed on separate branches
- Pull requests require at least one team member review
- Mathew provides final approval before merging to development
- No direct commits to main branch

### Conflict Resolution
- Technical disagreements escalated to Mathew for final decision
- Blockers addressed immediately in daily stand-ups
- Pair programming encouraged for complex integrations
- Regular check-ins to ensure timeline adherence