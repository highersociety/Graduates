# Database Schema Design

## Entity Relationship Overview

Our Campus Event Management System uses a normalized database design following Second Normal Form (2NF) principles. The schema supports user authentication, club management, event creation, and event registration workflows.

## Core Models

### Student Model
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'user' CHECK (role IN ('admin', 'leader', 'user')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Purpose**: Stores user account information with role-based access control
**Relationships**: One-to-many with clubs (as creator), events (as creator), and registrations

### Club Model
```sql
CREATE TABLE clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_by INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES students(id) ON DELETE CASCADE
);
```

**Purpose**: Represents student organizations and clubs on campus
**Relationships**: Belongs to student (creator), has many events, has many members through club_members

### Event Model
```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    location TEXT NOT NULL,
    club_id INTEGER,
    created_by INTEGER NOT NULL,
    capacity INTEGER DEFAULT 50,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (club_id) REFERENCES clubs(id) ON DELETE SET NULL,
    FOREIGN KEY (created_by) REFERENCES students(id) ON DELETE CASCADE
);
```

**Purpose**: Stores campus events with scheduling and capacity information
**Relationships**: Belongs to club (optional), belongs to student (creator), has many registrations

### Registration Model (Many-to-Many Junction)
```sql
CREATE TABLE registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    status TEXT DEFAULT 'going' CHECK (status IN ('going', 'interested', 'declined')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
    UNIQUE(student_id, event_id)
);
```

**Purpose**: Manages student event registrations with RSVP status tracking
**Relationships**: Links students and events in many-to-many relationship

### ClubMembers Model (Association Table)
```sql
CREATE TABLE club_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    role TEXT DEFAULT 'member' CHECK (role IN ('leader', 'member')),
    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (club_id) REFERENCES clubs(id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    UNIQUE(club_id, student_id)
);
```

**Purpose**: Tracks club membership and leadership roles
**Relationships**: Links clubs and students with role information

## Database Indexes and Constraints

### Primary Indexes
- All tables include auto-incrementing primary keys
- Unique constraint on `students.email` for authentication
- Composite unique constraints on junction tables to prevent duplicates

### Foreign Key Constraints
- `clubs.created_by` → `students.id` (CASCADE DELETE)
- `events.created_by` → `students.id` (CASCADE DELETE)
- `events.club_id` → `clubs.id` (SET NULL on delete)
- `registrations.student_id` → `students.id` (CASCADE DELETE)
- `registrations.event_id` → `events.id` (CASCADE DELETE)
- `club_members.club_id` → `clubs.id` (CASCADE DELETE)
- `club_members.student_id` → `students.id` (CASCADE DELETE)

### Check Constraints
- `students.role` limited to: 'admin', 'leader', 'user'
- `registrations.status` limited to: 'going', 'interested', 'declined'
- `club_members.role` limited to: 'leader', 'member'

## Normalization Analysis

### First Normal Form (1NF)
- All attributes contain atomic values
- No repeating groups or arrays in any column
- Each row is uniquely identifiable by primary key

### Second Normal Form (2NF)
- Meets 1NF requirements
- All non-key attributes are fully functionally dependent on primary keys
- No partial dependencies exist in our design

### Design Rationale

**Student-Club Relationship**: 
- One-to-many for club creation (students can create multiple clubs)
- Many-to-many for membership through `club_members` table

**Student-Event Relationship**:
- One-to-many for event creation (students can create multiple events)
- Many-to-many for registration through `registrations` table

**Club-Event Relationship**:
- One-to-many (clubs can host multiple events)
- Optional relationship (events can be independent of clubs)

## Sample Data Structure

### Users with Different Roles
```sql
-- Admin user
INSERT INTO students (name, email, password_hash, role) 
VALUES ('Admin User', 'admin@campus.edu', 'hashed_password', 'admin');

-- Club leaders
INSERT INTO students (name, email, password_hash, role) 
VALUES ('Club Leader', 'leader@campus.edu', 'hashed_password', 'leader');

-- Regular students
INSERT INTO students (name, email, password_hash, role) 
VALUES ('Student User', 'student@campus.edu', 'hashed_password', 'user');
```

### Clubs and Events
```sql
-- Sample club
INSERT INTO clubs (name, description, created_by) 
VALUES ('Computer Science Club', 'For CS students and enthusiasts', 2);

-- Sample event
INSERT INTO events (title, description, date, start_time, end_time, location, club_id, created_by, capacity) 
VALUES ('Tech Talk: AI in Education', 'Discussion on AI applications', '2024-02-15', '14:00', '16:00', 'Room 101', 1, 2, 30);

-- Sample registration
INSERT INTO registrations (student_id, event_id, status) 
VALUES (3, 1, 'going');
```

This schema design ensures data integrity while supporting all required functionality for our campus event management system.