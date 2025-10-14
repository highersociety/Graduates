# EventHub - Feature Specifications

## Core Platform Features

### 1. User Registration & Role Management

#### User Types
- **Regular User**: Can browse and purchase event tickets
- **Pending Leader**: Applied for leader status, awaiting admin approval
- **Verified Leader**: Admin-approved event organizer with full privileges
- **Admin**: Platform administrator with full system access

#### Registration Process
```
1. User signs up with email/password
2. Option to apply for "Event Organizer" status during registration
3. If applying as organizer:
   - Additional verification form (business details, ID verification)
   - Status set to "pending_leader"
   - Admin notification for approval
4. Regular users can upgrade to organizer later
```

### 2. Leader Verification System

#### Verification Workflow
```
Pending Leader → Admin Review → Approved/Rejected
- Admin dashboard shows pending applications
- Verification includes: ID verification, business registration, contact details
- Email notifications for status changes
- Approved leaders get 2-month free trial
```

#### Admin Verification Controls
- View all pending leader applications
- Approve/reject with reason notes
- Bulk actions for multiple applications
- Verification history tracking

### 3. Event Creation & Ticketing

#### Event Types
- **Free Events**: No tickets required, simple RSVP
- **Paid Events**: Multiple ticket tiers with pricing

#### Ticket Management
```
Ticket Types:
- Early Bird (discounted, limited time)
- General Admission
- VIP/Premium
- Group packages

Ticket Properties:
- Name and description
- Price (KES)
- Quantity available
- Sale start/end dates
- Purchase limits per user
```

#### Event Creation Process
1. Basic event details (title, description, date, location)
2. Choose free or paid event
3. If paid: Create ticket tiers with pricing
4. Upload event banner image
5. Set capacity and sale periods
6. Publish event

### 4. M-Pesa Payment Integration

#### Payment Flow
```
1. User selects tickets and quantity
2. Checkout page shows total amount
3. Enter M-Pesa phone number
4. STK push sent to user's phone
5. User enters M-Pesa PIN
6. Payment confirmation
7. Ticket generation and email delivery
```

#### M-Pesa Configuration
- Sandbox for development
- Production credentials for live payments
- Automatic payment verification
- Refund handling for failed events

### 5. Subscription Management

#### Subscription Plans
```
Trial Period: 2 months free for new verified leaders
Basic Plan: KES 200/month
- Create unlimited events
- Basic analytics
- Standard support

Premium Plan: KES 500/month
- All Basic features
- Advanced analytics
- Priority support
- Custom branding
- Bulk ticket operations
```

#### Subscription Features
- Stripe integration for recurring billing
- Automatic trial expiration handling
- Subscription upgrade/downgrade
- Payment failure handling
- Subscription analytics

### 6. Revenue Sharing & Commission

#### Commission Structure
```
Platform Commission: 5% of ticket sales
- Deducted automatically from each sale
- Real-time commission calculation
- Monthly payout to organizers
- Transparent fee breakdown
```

#### Revenue Dashboard
- Total sales by event
- Commission breakdown
- Payout history
- Revenue analytics and trends
- Export financial reports

### 7. Admin Panel Features

#### User Management
- View all users by role
- Approve/reject leader applications
- Suspend/activate accounts
- User activity monitoring

#### Financial Management
- Platform revenue tracking
- Commission rate configuration
- Payout management
- Financial reporting

#### System Configuration
- Platform settings
- Commission rates
- Subscription pricing
- Email templates

## Technical Implementation

### Database Schema Updates
```sql
-- Updated User model
ALTER TABLE users ADD COLUMN verification_status VARCHAR(20) DEFAULT 'none';
ALTER TABLE users ADD COLUMN subscription_status VARCHAR(20) DEFAULT 'trial';
ALTER TABLE users ADD COLUMN trial_end_date TIMESTAMP;
ALTER TABLE users ADD COLUMN phone_number VARCHAR(15);

-- New Ticket model
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    quantity INTEGER NOT NULL,
    sold_count INTEGER DEFAULT 0,
    sale_start_date TIMESTAMP DEFAULT NOW(),
    sale_end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- New Purchase model
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    ticket_id INTEGER REFERENCES tickets(id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    mpesa_code VARCHAR(50),
    payment_phone VARCHAR(15),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW()
);

-- New Subscription model
CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    plan_type VARCHAR(50) NOT NULL,
    monthly_fee DECIMAL(10,2) NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    stripe_subscription_id VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

-- New Commission model
CREATE TABLE commissions (
    id SERIAL PRIMARY KEY,
    purchase_id INTEGER REFERENCES purchases(id),
    platform_fee_rate DECIMAL(5,4) NOT NULL,
    platform_fee_amount DECIMAL(10,2) NOT NULL,
    organizer_amount DECIMAL(10,2) NOT NULL,
    payout_status VARCHAR(20) DEFAULT 'pending',
    payout_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### API Endpoints

#### Authentication & Verification
```
POST /api/auth/register - User registration with role selection
POST /api/auth/apply-leader - Apply for leader verification
GET /api/admin/pending-leaders - Get pending leader applications
POST /api/admin/verify-leader/:id - Approve/reject leader application
```

#### Ticketing & Payments
```
POST /api/events/:id/tickets - Create ticket tiers for event
GET /api/events/:id/tickets - Get available tickets
POST /api/tickets/:id/purchase - Purchase tickets
POST /api/payments/mpesa/callback - M-Pesa payment callback
GET /api/purchases/my-tickets - User's purchased tickets
```

#### Subscriptions
```
GET /api/subscriptions/plans - Available subscription plans
POST /api/subscriptions/subscribe - Create new subscription
POST /api/subscriptions/cancel - Cancel subscription
GET /api/subscriptions/my-subscription - Current subscription status
```

#### Revenue & Analytics
```
GET /api/analytics/revenue - Revenue dashboard data
GET /api/analytics/events/:id - Event-specific analytics
GET /api/admin/commissions - Platform commission tracking
POST /api/admin/payouts - Process organizer payouts
```

## Figma Design Requirements

### Design System
- Modern, clean interface with event-focused branding
- Mobile-first responsive design
- Consistent color scheme and typography
- Accessible design following WCAG guidelines

### Key Pages
1. **Landing Page**: Hero section, featured events, how it works
2. **Event Discovery**: Grid/list view, filters, search
3. **Event Details**: Full event info, ticket selection, purchase flow
4. **Checkout**: Secure payment form with M-Pesa integration
5. **User Dashboard**: My events, tickets, subscription status
6. **Organizer Dashboard**: Event management, analytics, revenue
7. **Admin Panel**: User management, verification, financial oversight

### Mobile Considerations
- Touch-friendly interface elements
- Optimized payment flow for mobile
- Offline ticket viewing capability
- Push notifications for event updates

## Security & Compliance

### Payment Security
- PCI DSS compliance for card payments
- Secure M-Pesa API integration
- Encrypted payment data storage
- Fraud detection and prevention

### Data Protection
- GDPR-compliant data handling
- User consent management
- Data encryption at rest and in transit
- Regular security audits

### Financial Compliance
- Transaction logging and audit trails
- Tax reporting capabilities
- Anti-money laundering checks
- Regulatory compliance monitoring