# Quality Assurance Checklist

## Pre-Demo Setup

### Database & Seed Data
- [ ] Database is properly initialized with migrations
- [ ] Seed script creates realistic sample data:
  - [ ] 1 admin user (admin@campus.edu)
  - [ ] 2 club leaders (leader1@campus.edu, leader2@campus.edu)
  - [ ] 3 regular users (user1@campus.edu, user2@campus.edu, user3@campus.edu)
  - [ ] 4 clubs with varying descriptions and member counts
  - [ ] 8 events (mix of past/future, different capacities, club/independent)
  - [ ] Sample registrations and club memberships
- [ ] All passwords are consistent for demo (e.g., "password123")

### Environment Setup
- [ ] Backend server running on correct port (5000)
- [ ] Frontend development server running on correct port (3000)
- [ ] Database connection established
- [ ] CORS configured properly
- [ ] Environment variables loaded correctly

## Authentication & Authorization Testing

### User Registration
- [ ] New user can register with valid email/password
- [ ] Duplicate email registration is rejected with proper error message
- [ ] Password validation enforces minimum length requirements
- [ ] Role defaults to 'user' when not specified
- [ ] JWT token is returned upon successful registration

### User Login
- [ ] Valid credentials allow successful login
- [ ] Invalid email/password combinations are rejected
- [ ] JWT token is returned and stored properly
- [ ] User information is available in application state

### Role-Based Access Control
- [ ] Regular users can view events and clubs
- [ ] Regular users can RSVP to events and join clubs
- [ ] Regular users cannot create clubs or events
- [ ] Club leaders can create and manage their clubs
- [ ] Club leaders can create events for their clubs
- [ ] Admin users have access to admin panel
- [ ] Unauthorized access attempts return 403 errors

## Event Management Testing

### Event Listing
- [ ] All events display correctly on events page
- [ ] Event cards show title, date, time, location, capacity
- [ ] Registration count updates accurately
- [ ] Club events show associated club name
- [ ] Pagination works for large event lists

### Event Details
- [ ] Event detail page shows complete information
- [ ] RSVP button is visible to authenticated users
- [ ] Registration list shows current attendees (if applicable)
- [ ] Capacity limits are displayed and enforced
- [ ] Event creator information is shown

### Event Creation
- [ ] Authenticated users can create independent events
- [ ] Club leaders can create club-specific events
- [ ] Form validation prevents invalid dates (past dates)
- [ ] End time must be after start time
- [ ] Capacity must be positive integer
- [ ] Required fields are enforced

### RSVP Functionality
- [ ] Users can RSVP with status: going/interested/declined
- [ ] RSVP status updates immediately in UI
- [ ] Registration count updates after RSVP
- [ ] Users cannot RSVP to same event multiple times (updates existing)
- [ ] Capacity limits prevent over-registration

## Club Management Testing

### Club Listing
- [ ] All clubs display on clubs page
- [ ] Club cards show name, description, member count
- [ ] Search functionality filters clubs by name
- [ ] Club creator information is visible

### Club Details
- [ ] Club detail page shows complete information
- [ ] Member list displays current club members
- [ ] Club events are listed separately
- [ ] Join button is available to non-members
- [ ] Management controls visible to club leaders

### Club Creation
- [ ] Authenticated users can create new clubs
- [ ] Club name and description validation works
- [ ] Creator automatically becomes club leader
- [ ] New club appears in club listing immediately

### Club Membership
- [ ] Users can join clubs successfully
- [ ] Duplicate membership attempts are handled gracefully
- [ ] Member count updates after joining
- [ ] Club membership appears in user dashboard

## User Interface Testing

### Navigation
- [ ] Navbar shows appropriate links based on authentication status
- [ ] Logo/brand links to home page
- [ ] Active page is highlighted in navigation
- [ ] Mobile navigation menu works properly

### Responsive Design
- [ ] Application works on mobile devices (375px width)
- [ ] Tablet layout is functional (768px width)
- [ ] Desktop layout is optimal (1024px+ width)
- [ ] Images and content scale appropriately
- [ ] Touch targets are appropriately sized for mobile

### User Experience
- [ ] Loading states are shown during API calls
- [ ] Success messages appear for completed actions
- [ ] Error messages are clear and actionable
- [ ] Form validation provides immediate feedback
- [ ] Toast notifications appear and disappear appropriately

## Dashboard & Personal Data

### User Dashboard
- [ ] Shows upcoming events user has registered for
- [ ] Displays clubs user has joined
- [ ] Shows events user has created (if any)
- [ ] Links to detailed pages work correctly

### Data Consistency
- [ ] User actions reflect immediately in UI
- [ ] Page refreshes maintain correct state
- [ ] Data persists across browser sessions
- [ ] Logout clears all user-specific data

## API Testing

### Authentication Endpoints
- [ ] POST /api/auth/register creates new user
- [ ] POST /api/auth/login returns valid JWT
- [ ] GET /api/auth/me returns current user info
- [ ] Invalid tokens return 401 errors

### Event Endpoints
- [ ] GET /api/events returns paginated event list
- [ ] GET /api/events/:id returns event details
- [ ] POST /api/events creates new event (auth required)
- [ ] POST /api/events/:id/rsvp updates registration

### Club Endpoints
- [ ] GET /api/clubs returns club list
- [ ] GET /api/clubs/:id returns club details with members
- [ ] POST /api/clubs creates new club (auth required)
- [ ] POST /api/clubs/:id/join adds user to club

### Error Handling
- [ ] 404 errors for non-existent resources
- [ ] 400 errors for invalid request data
- [ ] 403 errors for unauthorized actions
- [ ] 500 errors handled gracefully

## Performance & Security

### Performance
- [ ] Page load times are acceptable (<3 seconds)
- [ ] API responses are reasonably fast (<1 second)
- [ ] Images load efficiently
- [ ] No memory leaks in browser console

### Security
- [ ] Passwords are hashed in database
- [ ] JWT tokens expire appropriately
- [ ] Sensitive data not exposed in client
- [ ] CORS configured for production domains
- [ ] Input sanitization prevents XSS

## Cross-Browser Compatibility

### Desktop Browsers
- [ ] Chrome (latest version)
- [ ] Firefox (latest version)
- [ ] Safari (latest version)
- [ ] Edge (latest version)

### Mobile Browsers
- [ ] Mobile Chrome (Android)
- [ ] Mobile Safari (iOS)
- [ ] Samsung Internet (Android)

## Deployment Verification

### Backend Deployment
- [ ] API endpoints accessible via production URL
- [ ] Database migrations applied successfully
- [ ] Environment variables configured correctly
- [ ] Health check endpoint returns 200 status

### Frontend Deployment
- [ ] Application loads from production URL
- [ ] API calls connect to production backend
- [ ] Static assets load correctly
- [ ] Routing works with direct URL access

## Demo Preparation

### Sample Data Verification
- [ ] Admin login works: admin@campus.edu / password123
- [ ] Leader login works: leader1@campus.edu / password123
- [ ] User login works: user1@campus.edu / password123
- [ ] Events span past and future dates
- [ ] Clubs have realistic member counts
- [ ] Some events are at capacity for testing

### Demo Flow Testing
- [ ] Complete user registration flow
- [ ] Club creation and event creation by leader
- [ ] RSVP flow with status changes
- [ ] Dashboard updates after actions
- [ ] Admin panel access (if implemented)

## Final Checklist

- [ ] All critical bugs resolved
- [ ] Performance is acceptable
- [ ] Documentation is complete
- [ ] Deployment is stable
- [ ] Demo data is prepared
- [ ] Team is ready for presentation

## Bug Tracking

| Issue | Severity | Status | Assigned To | Notes |
|-------|----------|--------|-------------|-------|
| | | | | |

## Test Results Summary

**Total Test Cases**: ___
**Passed**: ___
**Failed**: ___
**Blocked**: ___

**Overall Status**: ✅ Ready for Demo / ⚠️ Minor Issues / ❌ Major Issues

**QA Sign-off**: _________________ Date: _________