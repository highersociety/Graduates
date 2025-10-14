# EventHub - Figma Design Brief

## Design System Overview

### Brand Identity
- **Name**: EventHub
- **Tagline**: "Discover, create and monetize events — all in one platform"
- **Personality**: Professional, trustworthy, modern, accessible
- **Target Audience**: Event organizers, event attendees, general public

### Color Palette
```
Primary Colors:
- Primary Blue: #3B82F6 (Main CTA buttons, links)
- Primary Dark: #1D4ED8 (Hover states, emphasis)
- Primary Light: #EFF6FF (Backgrounds, subtle highlights)

Secondary Colors:
- Success Green: #10B981 (Success states, confirmations)
- Warning Orange: #F59E0B (Warnings, pending states)
- Error Red: #EF4444 (Errors, destructive actions)
- Gray Scale: #F8FAFC to #1F2937 (Text, backgrounds, borders)

Accent Colors:
- Gold: #F59E0B (Premium features, verified badges)
- Purple: #8B5CF6 (Special events, promotions)
```

### Typography
```
Primary Font: Inter (Google Fonts)
- Headings: Inter Bold (700)
- Subheadings: Inter SemiBold (600)
- Body Text: Inter Regular (400)
- Captions: Inter Medium (500)

Font Sizes:
- H1: 32px (Mobile: 24px)
- H2: 24px (Mobile: 20px)
- H3: 20px (Mobile: 18px)
- Body: 16px (Mobile: 14px)
- Caption: 14px (Mobile: 12px)
- Small: 12px (Mobile: 11px)
```

### Spacing System
```
Base Unit: 4px
Spacing Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96px

Component Spacing:
- Button Padding: 12px 24px
- Card Padding: 20px
- Section Margins: 48px (Mobile: 32px)
- Element Gaps: 16px (Mobile: 12px)
```

## Page Designs Required

### 1. Landing Page
**Purpose**: Convert visitors to users and organizers

**Sections**:
- Hero section with value proposition
- Featured events grid (6 events)
- How it works (3 steps)
- Organizer benefits section
- Testimonials
- CTA section
- Footer

**Key Elements**:
- Primary CTA: "Find Events" / "Start Organizing"
- Search bar with location and category filters
- Trust indicators (user count, events hosted)
- Mobile-responsive hero image

### 2. Event Discovery Page
**Purpose**: Help users find and filter events

**Layout**:
- Header with search and filters
- Sidebar filters (category, date, price, location)
- Event grid/list toggle
- Pagination
- Map view option

**Event Card Design**:
- Event image (16:9 ratio)
- Event title and date
- Location and time
- Price range or "Free"
- Organizer name with verification badge
- Quick action buttons (Save, Share)

### 3. Event Details Page
**Purpose**: Provide complete event information and enable ticket purchase

**Sections**:
- Event hero image and basic info
- Ticket selection with pricing tiers
- Event description and agenda
- Organizer information
- Location with map
- Similar events
- Reviews/ratings (future feature)

**Ticket Selection**:
- Ticket type cards with descriptions
- Quantity selectors
- Price breakdown
- Total calculation
- Secure checkout button

### 4. Checkout & Payment Page
**Purpose**: Secure and smooth payment experience

**Flow**:
- Order summary
- User information form
- M-Pesa payment integration
- Payment confirmation
- Ticket delivery

**M-Pesa Integration**:
- Phone number input with validation
- STK push notification display
- Payment status indicators
- Success/failure states

### 5. User Dashboard
**Purpose**: Personal event management for attendees

**Sections**:
- Welcome message with quick stats
- Upcoming events I'm attending
- Past events with feedback options
- Saved/bookmarked events
- Account settings

**Features**:
- Ticket QR codes for entry
- Event reminders and notifications
- Download tickets as PDF
- Share events with friends

### 6. Organizer Dashboard
**Purpose**: Event management and analytics for organizers

**Sections**:
- Revenue overview with charts
- My events (draft, published, past)
- Ticket sales analytics
- Subscription status
- Quick actions (Create Event, View Analytics)

**Analytics Cards**:
- Total revenue this month
- Tickets sold vs. available
- Top performing events
- Upcoming payouts

### 7. Event Creation Flow
**Purpose**: Streamlined event creation process

**Steps**:
1. Basic information (title, description, date, location)
2. Event type (free or paid)
3. Ticket configuration (if paid)
4. Media upload (images, videos)
5. Preview and publish

**Ticket Configuration**:
- Multiple ticket tiers
- Early bird pricing
- Group discounts
- Sale periods
- Capacity limits

### 8. Admin Panel
**Purpose**: Platform management and oversight

**Sections**:
- Dashboard with key metrics
- User management (verification queue)
- Event moderation
- Revenue analytics
- System settings

**Verification Interface**:
- Pending applications list
- User details and documents
- Approve/reject actions with reasons
- Bulk actions for efficiency

### 9. Mobile App Screens
**Purpose**: Native mobile experience

**Key Screens**:
- Splash screen with branding
- Onboarding flow (3 screens)
- Bottom navigation (Discover, My Events, Create, Profile)
- Event discovery with location services
- Mobile-optimized checkout
- Ticket wallet with QR codes

## Component Library

### Buttons
```
Primary Button:
- Background: Primary Blue
- Text: White
- Padding: 12px 24px
- Border Radius: 8px
- Font Weight: 600

Secondary Button:
- Background: Transparent
- Border: 2px Primary Blue
- Text: Primary Blue
- Same padding and radius

Ghost Button:
- Background: Transparent
- Text: Gray 600
- Hover: Gray 100 background
```

### Cards
```
Event Card:
- Border Radius: 12px
- Shadow: 0 4px 6px rgba(0,0,0,0.1)
- Padding: 0 (image full width)
- Content Padding: 16px

Info Card:
- Border Radius: 8px
- Border: 1px Gray 200
- Padding: 20px
- Background: White
```

### Forms
```
Input Fields:
- Border: 1px Gray 300
- Border Radius: 6px
- Padding: 12px 16px
- Focus: Primary Blue border
- Error: Red border with error message

Select Dropdowns:
- Same styling as inputs
- Chevron icon on right
- Custom dropdown styling
```

### Navigation
```
Header:
- Height: 64px
- Background: White
- Border Bottom: 1px Gray 200
- Logo on left, navigation center, user menu right

Mobile Navigation:
- Bottom tab bar
- 4-5 main sections
- Active state indicators
```

## Responsive Design Guidelines

### Breakpoints
```
Mobile: 320px - 767px
Tablet: 768px - 1023px
Desktop: 1024px - 1439px
Large Desktop: 1440px+
```

### Mobile Considerations
- Touch targets minimum 44px
- Thumb-friendly navigation
- Simplified layouts
- Optimized images
- Fast loading times
- Offline capabilities for tickets

### Accessibility Requirements
- WCAG 2.1 AA compliance
- Color contrast ratios 4.5:1 minimum
- Keyboard navigation support
- Screen reader compatibility
- Alt text for all images
- Focus indicators

## Animation & Interactions

### Micro-interactions
- Button hover states (0.2s ease)
- Loading spinners for async actions
- Success checkmarks for completed actions
- Smooth page transitions
- Card hover effects (subtle lift)

### Loading States
- Skeleton screens for content loading
- Progress bars for multi-step processes
- Spinner for quick actions
- Shimmer effects for image loading

## Design Deliverables

### Figma Files Structure
```
1. Design System
   - Colors, typography, spacing
   - Component library
   - Icon set

2. Desktop Designs
   - All 8 main pages
   - Key user flows
   - Admin interfaces

3. Mobile Designs
   - Mobile versions of all pages
   - Native app screens
   - Touch interactions

4. Prototypes
   - User journey flows
   - Interactive prototypes
   - Micro-interaction demos
```

### Assets to Export
- Logo variations (light, dark, icon only)
- Icon set (SVG format)
- Images and illustrations
- Style guide PDF
- Developer handoff specifications

## User Experience Flows

### New User Registration
1. Landing page → Sign up
2. Choose user type (attendee/organizer)
3. Fill registration form
4. Email verification
5. Welcome onboarding

### Event Discovery & Purchase
1. Browse events or search
2. Filter and sort results
3. View event details
4. Select tickets and quantity
5. Checkout with M-Pesa
6. Receive confirmation and tickets

### Event Creation (Organizer)
1. Dashboard → Create Event
2. Multi-step event form
3. Configure tickets and pricing
4. Upload media and preview
5. Publish and promote

### Leader Verification
1. Apply during registration
2. Submit verification documents
3. Admin review process
4. Approval notification
5. Trial period activation

This design brief ensures a cohesive, professional, and user-friendly experience across all touchpoints of the EventHub platform.