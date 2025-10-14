# EventHub - Presentation Script

**Total Duration: 7-8 minutes**

## Introduction — Mathew (Scrum Master) — 45 seconds

"Good morning everyone. We're Team EventHub from Moringa School, and I'm Mathew, the Scrum Master for this project. Over the past sprint, our team of six developers built EventHub - a comprehensive event marketplace platform that connects organizers with attendees through ticketing, M-Pesa payments, and subscription management.

Our primary objectives were to demonstrate mastery of Flask-RESTful APIs, M-Pesa payment integration, React with financial state management, and implement a complete revenue-sharing business model. We also focused on creating a production-ready marketplace with subscription management.

Today we'll walk you through our architecture, demonstrate the core functionality, and share the key lessons we learned during development."

*[Show slide with project goals and tech stack diagram]*

---

## Architecture & Data Model — Brenda (Backend Lead) — 60 seconds

"Hi everyone, I'm Brenda, and I led the backend development. Let me quickly explain our technical architecture.

We built our backend using Flask with SQLAlchemy ORM and integrated M-Pesa payment APIs. Our database follows Second Normal Form normalization with seven core models: User, Club, Event, Ticket, Purchase, Subscription, and Commission.

The Purchase table handles the complete payment flow from ticket sales to commission calculations. We implemented RESTful endpoints for payment processing, subscription management, and leader verification, secured with JWT authentication for financial transactions.

Our role-based access control supports three user types: regular users who can RSVP and join clubs, leaders who can create and manage clubs, and admins with full system access. All API endpoints include proper validation and return structured error messages.

You can see our complete implementation in the backend/models.py file and our route definitions across the backend/routes directory."

*[Show ER diagram and code snippet of model relationships]*

---

## Ticketing & Payment Demo — Justin (Payment Specialist) — 120 seconds

"Hello, I'm Justin, and I focused on the ticketing and payment system. Let me demonstrate creating a paid event and processing M-Pesa payments.

*[Begin live demo]*

First, I'll log in as a verified organizer and create a paid event. *[Navigate to create event page]* As you can see, I can set up multiple ticket tiers with different pricing. *[Fill out event form with ticket options]* 

Now that the event is created, I can access the event management page where I can track ticket sales and revenue. *[Navigate to organizer dashboard]* Here I can see real-time sales data, revenue analytics, and upcoming payouts from the platform.

Let me demonstrate the ticket purchase flow. *[Navigate to event as customer]* Users can select ticket types and quantities, then proceed to M-Pesa payment. *[Show checkout process]* The system sends an STK push to their phone for secure payment.

The system handles the complete payment flow - from ticket selection to M-Pesa confirmation to automatic commission calculation. You can see this implementation in our backend/routes/payments.py file where we process STK push callbacks and update ticket inventory.

This demonstrates our role-based access control in action, ensuring that club management features are only available to authorized users."

*[Show successful payment processing, ticket confirmation, and revenue tracking]*

---

## Organizer Dashboard & Revenue Analytics — Kish (Frontend Lead) — 90 seconds

"Hi everyone, I'm Kish, and I built the organizer dashboard and payment interfaces. Let me demonstrate the revenue tracking and subscription management features.

*[Switch to events page]*

Organizers can access their dashboard to see real-time revenue analytics, subscription status, and payout history. Each event shows ticket sales, revenue generated, and commission breakdown. *[Navigate to organizer dashboard]*

On the dashboard, organizers can track their subscription status, view upcoming payments, and see their trial period remaining. *[Show subscription panel]* The system automatically handles the transition from trial to paid subscription. 

*[Demonstrate revenue updates]* Notice how the revenue updates in real-time as tickets are sold - this is our payment Context API in action, providing immediate feedback on sales performance. Commission calculations update instantly as payments are processed.

*[Navigate to analytics section]* The analytics section shows detailed breakdowns of platform fees, organizer earnings, and payout schedules. This gives organizers complete transparency into their revenue streams.

Our frontend uses React Hook Form for payment validation, Tailwind CSS for responsive design, and Context API for financial state management. The implementation is in frontend/src/pages/OrganizerDashboard.jsx and our payment context in frontend/src/context/PaymentContext.jsx."

*[Show real-time revenue updates and subscription management]*

---

## Quality Assurance & Testing — Adrian (QA Lead) — 45 seconds

"I'm Adrian, and I handled quality assurance and testing for our application. 

For demonstration purposes, we created a comprehensive seed script that populates our database with realistic sample data: admin users, club leaders, regular students, multiple clubs with varying member counts, and events spanning past and future dates with different capacity limits.

We implemented API testing using pytest with Flask's test client, covering all critical endpoints including authentication, event CRUD operations, club management, and RSVP functionality. Our test suite includes both happy path scenarios and edge cases like capacity limits and permission violations.

We also created a manual QA checklist covering cross-browser compatibility, mobile responsiveness, and user workflow validation. All tests pass locally, and our seed script creates a realistic demo environment that showcases the full range of our application's capabilities.

The testing implementation is available in our tests directory, and the seed script is in backend/seed.py with clear setup instructions in our README."

*[Show test output or seed script execution]*

---

## Admin Panel & Platform Management — Johns (Admin Developer) — 45 seconds

"I'm Johns, and I built the admin panel for platform management and leader verification.

The admin dashboard allows platform administrators to verify organizer applications, monitor subscription payments, and track commission revenue. Admins can approve or reject leader applications with detailed review processes.

I implemented the complete verification workflow where pending organizers submit documentation, admins review applications, and approved leaders automatically receive their 2-month trial period. 

The admin panel also provides revenue analytics, showing platform commission earnings, organizer payouts, and subscription revenue. This gives complete oversight of the platform's financial performance and user management.

The implementation includes secure admin routes in backend/routes/admin.py and a comprehensive admin interface in frontend/src/pages/AdminPanel.jsx with role-based access controls."

*[Show admin dashboard with verification queue and revenue analytics]*

---

## Wrap-up & Lessons Learned — Mathew (Scrum Master) — 30 seconds

"Thank you for your attention. This project significantly strengthened our full-stack development skills with fintech integration and marketplace development capabilities.

Our key lessons included the complexity of payment integration with M-Pesa APIs, the importance of secure financial data handling, and the challenges of building subscription management systems with trial periods and automated billing.

We're proud of delivering a fully functional event marketplace with real payment processing and revenue sharing. The complete codebase demonstrates fintech integration skills and we're happy to walk through any payment flow implementations or business model questions.

Are there any questions about EventHub?"

*[Open for Q&A session]*

---

## Q&A Preparation

**Potential Questions & Responses:**

**Q: How did you handle M-Pesa payment integration?**
A: We implemented STK push payments with callback handling through our Purchase model. This allows us to process real-time payments, handle confirmations, and automatically calculate commission splits while maintaining financial data integrity.

**Q: What security measures did you implement for payments?**
A: We used JWT tokens for financial transactions, implemented secure M-Pesa API integration with proper credential management, validated all payment data using Marshmallow schemas, and encrypted sensitive financial information.

**Q: How did you ensure mobile responsiveness?**
A: We used Tailwind CSS with a mobile-first approach, tested across different screen sizes, and implemented responsive navigation and card layouts that adapt to various device widths.

**Q: What would you add if you had more time?**
A: We'd implement automated payout systems to organizer bank accounts, add fraud detection for suspicious transactions, create advanced revenue analytics with forecasting, and integrate additional payment methods like card payments.

## Speaker Notes

- **Timing**: Each section has strict time limits - practice with a timer
- **Transitions**: Smooth handoffs between speakers with clear cues
- **Demo Preparation**: Have backup screenshots in case of technical issues
- **Code References**: Be ready to show specific files and line numbers
- **Confidence**: Speak clearly and maintain eye contact with the audience