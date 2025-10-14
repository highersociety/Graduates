#!/usr/bin/env python3

from datetime import datetime, date, time, timedelta
from app import create_app, db
from models import Student, Club, Event, Registration, ClubMember

def create_sample_data():
    """Create comprehensive sample data for demonstration purposes."""
    
    print("Creating sample users...")
    
    # Create admin user
    admin = Student(
        name="Admin User",
        email="admin@campus.edu",
        role="admin"
    )
    admin.set_password("password123")
    db.session.add(admin)
    
    # Create club leaders
    leader1 = Student(
        name="Sarah Johnson",
        email="leader1@campus.edu",
        role="leader"
    )
    leader1.set_password("password123")
    db.session.add(leader1)
    
    leader2 = Student(
        name="Michael Chen",
        email="leader2@campus.edu",
        role="leader"
    )
    leader2.set_password("password123")
    db.session.add(leader2)
    
    # Create regular users
    users_data = [
        ("Emma Wilson", "user1@campus.edu"),
        ("James Rodriguez", "user2@campus.edu"),
        ("Aisha Patel", "user3@campus.edu"),
        ("David Kim", "user4@campus.edu"),
        ("Maria Garcia", "user5@campus.edu")
    ]
    
    users = []
    for name, email in users_data:
        user = Student(name=name, email=email, role="user")
        user.set_password("password123")
        users.append(user)
        db.session.add(user)
    
    db.session.commit()
    print(f"Created {len(users_data) + 3} users")
    
    print("Creating sample clubs...")
    
    # Create clubs
    clubs_data = [
        {
            "name": "Computer Science Club",
            "description": "A community for CS students to collaborate on projects, share knowledge, and explore the latest in technology.",
            "created_by": leader1.id
        },
        {
            "name": "Photography Society",
            "description": "Capturing moments and developing skills in digital and film photography. Weekly photo walks and workshops.",
            "created_by": leader2.id
        },
        {
            "name": "Environmental Action Group",
            "description": "Dedicated to promoting sustainability on campus through awareness campaigns and green initiatives.",
            "created_by": leader1.id
        },
        {
            "name": "Debate Society",
            "description": "Developing critical thinking and public speaking skills through structured debates and discussions.",
            "created_by": leader2.id
        }
    ]
    
    clubs = []
    for club_data in clubs_data:
        club = Club(**club_data)
        clubs.append(club)
        db.session.add(club)
    
    db.session.commit()
    print(f"Created {len(clubs)} clubs")
    
    print("Creating club memberships...")
    
    # Add club memberships
    memberships = [
        # CS Club members
        ClubMember(club_id=clubs[0].id, student_id=users[0].id, role="member"),
        ClubMember(club_id=clubs[0].id, student_id=users[1].id, role="member"),
        ClubMember(club_id=clubs[0].id, student_id=users[2].id, role="member"),
        
        # Photography Society members
        ClubMember(club_id=clubs[1].id, student_id=users[1].id, role="member"),
        ClubMember(club_id=clubs[1].id, student_id=users[3].id, role="member"),
        
        # Environmental Action Group members
        ClubMember(club_id=clubs[2].id, student_id=users[0].id, role="member"),
        ClubMember(club_id=clubs[2].id, student_id=users[4].id, role="member"),
        
        # Debate Society members
        ClubMember(club_id=clubs[3].id, student_id=users[2].id, role="member"),
        ClubMember(club_id=clubs[3].id, student_id=users[3].id, role="member"),
        ClubMember(club_id=clubs[3].id, student_id=users[4].id, role="member"),
    ]
    
    for membership in memberships:
        db.session.add(membership)
    
    db.session.commit()
    print(f"Created {len(memberships)} club memberships")
    
    print("Creating sample events...")
    
    # Create events (mix of past and future)
    today = date.today()
    
    events_data = [
        # Future events
        {
            "title": "AI in Education Workshop",
            "description": "Explore how artificial intelligence is transforming modern education. Hands-on session with AI tools and practical applications.",
            "date": today + timedelta(days=7),
            "start_time": time(14, 0),
            "end_time": time(16, 0),
            "location": "Computer Lab 201",
            "club_id": clubs[0].id,
            "created_by": leader1.id,
            "capacity": 30
        },
        {
            "title": "Campus Photography Contest",
            "description": "Annual photography competition showcasing the beauty of our campus. Submit your best shots for a chance to win prizes!",
            "date": today + timedelta(days=14),
            "start_time": time(10, 0),
            "end_time": time(17, 0),
            "location": "Student Center Gallery",
            "club_id": clubs[1].id,
            "created_by": leader2.id,
            "capacity": 100
        },
        {
            "title": "Sustainability Fair",
            "description": "Learn about eco-friendly practices and sustainable living. Interactive booths, workshops, and green technology demonstrations.",
            "date": today + timedelta(days=21),
            "start_time": time(9, 0),
            "end_time": time(15, 0),
            "location": "Main Quad",
            "club_id": clubs[2].id,
            "created_by": leader1.id,
            "capacity": 200
        },
        {
            "title": "Inter-University Debate Championship",
            "description": "Competitive debate tournament featuring teams from universities across the region. Come support our debaters!",
            "date": today + timedelta(days=28),
            "start_time": time(13, 0),
            "end_time": time(18, 0),
            "location": "Auditorium A",
            "club_id": clubs[3].id,
            "created_by": leader2.id,
            "capacity": 150
        },
        {
            "title": "Career Fair 2024",
            "description": "Meet with top employers and explore internship and job opportunities. Bring your resume and dress professionally.",
            "date": today + timedelta(days=35),
            "start_time": time(10, 0),
            "end_time": time(16, 0),
            "location": "Sports Complex",
            "club_id": None,  # Independent event
            "created_by": admin.id,
            "capacity": 500
        },
        
        # Past events for demonstration
        {
            "title": "Welcome Week Mixer",
            "description": "Get to know your fellow students and learn about campus organizations. Food, music, and fun activities.",
            "date": today - timedelta(days=30),
            "start_time": time(18, 0),
            "end_time": time(21, 0),
            "location": "Student Center",
            "club_id": None,
            "created_by": admin.id,
            "capacity": 300
        },
        {
            "title": "Python Programming Bootcamp",
            "description": "Intensive 3-day bootcamp covering Python fundamentals, web development, and data analysis.",
            "date": today - timedelta(days=14),
            "start_time": time(9, 0),
            "end_time": time(17, 0),
            "location": "Computer Lab 101",
            "club_id": clubs[0].id,
            "created_by": leader1.id,
            "capacity": 25
        },
        {
            "title": "Nature Photography Walk",
            "description": "Guided photography session in the nearby botanical gardens. Learn composition techniques and nature photography tips.",
            "date": today - timedelta(days=7),
            "start_time": time(8, 0),
            "end_time": time(12, 0),
            "location": "Botanical Gardens",
            "club_id": clubs[1].id,
            "created_by": leader2.id,
            "capacity": 20
        }
    ]
    
    events = []
    for event_data in events_data:
        event = Event(**event_data)
        events.append(event)
        db.session.add(event)
    
    db.session.commit()
    print(f"Created {len(events)} events")
    
    print("Creating sample registrations...")
    
    # Create sample registrations
    registrations_data = [
        # AI Workshop registrations
        (users[0].id, events[0].id, "going"),
        (users[1].id, events[0].id, "going"),
        (users[2].id, events[0].id, "interested"),
        
        # Photography Contest registrations
        (users[1].id, events[1].id, "going"),
        (users[3].id, events[1].id, "going"),
        (users[4].id, events[1].id, "interested"),
        
        # Sustainability Fair registrations
        (users[0].id, events[2].id, "going"),
        (users[4].id, events[2].id, "going"),
        
        # Debate Championship registrations
        (users[2].id, events[3].id, "going"),
        (users[3].id, events[3].id, "going"),
        (users[4].id, events[3].id, "going"),
        
        # Career Fair registrations
        (users[0].id, events[4].id, "going"),
        (users[1].id, events[4].id, "going"),
        (users[2].id, events[4].id, "interested"),
        (users[3].id, events[4].id, "going"),
        (users[4].id, events[4].id, "going"),
        
        # Past event registrations
        (users[0].id, events[5].id, "going"),
        (users[1].id, events[5].id, "going"),
        (users[2].id, events[6].id, "going"),
        (users[1].id, events[7].id, "going"),
        (users[3].id, events[7].id, "going"),
    ]
    
    registrations = []
    for student_id, event_id, status in registrations_data:
        registration = Registration(
            student_id=student_id,
            event_id=event_id,
            status=status
        )
        registrations.append(registration)
        db.session.add(registration)
    
    db.session.commit()
    print(f"Created {len(registrations)} event registrations")
    
    print("\n" + "="*50)
    print("SAMPLE DATA CREATION COMPLETE")
    print("="*50)
    print("\nDemo Login Credentials:")
    print("Admin: admin@campus.edu / password123")
    print("Leader 1: leader1@campus.edu / password123")
    print("Leader 2: leader2@campus.edu / password123")
    print("User 1: user1@campus.edu / password123")
    print("User 2: user2@campus.edu / password123")
    print("User 3: user3@campus.edu / password123")
    print("\nDatabase Summary:")
    print(f"- {Student.query.count()} students")
    print(f"- {Club.query.count()} clubs")
    print(f"- {Event.query.count()} events")
    print(f"- {Registration.query.count()} registrations")
    print(f"- {ClubMember.query.count()} club memberships")

def clear_data():
    """Clear all existing data from the database."""
    print("Clearing existing data...")
    
    # Delete in reverse order of dependencies
    Registration.query.delete()
    ClubMember.query.delete()
    Event.query.delete()
    Club.query.delete()
    Student.query.delete()
    
    db.session.commit()
    print("All data cleared.")

if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        clear_data()
        
        # Create fresh sample data
        create_sample_data()
        
        print("\nSeed script completed successfully!")
        print("You can now start the Flask application and test with the sample data.")