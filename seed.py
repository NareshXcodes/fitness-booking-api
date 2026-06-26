from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import sys
from app.database import SessionLocal
from app.models.user import User
from app.models.fitness_class import FitnessClass
from app.models.booking import Booking

from app.services.auth_service import hash_password

db = SessionLocal()


if db.query(User).count() > 0:
    print("Database already contains seed data.")
    db.close()
    sys.exit()

user1 = User(
    name="John Doe",
    email="john@example.com",
    password=hash_password("Password123")
)

user2 = User(
    name="Alice Smith",
    email="alice@example.com",
    password=hash_password("Password123")
)

db.add_all([user1, user2])
db.commit()

db.refresh(user1)
db.refresh(user2)


IST = ZoneInfo("Asia/Kolkata")

now = datetime.now(IST).replace(
    hour=9,
    minute=0,
    second=0,
    microsecond=0,
)


class1 = FitnessClass(
    name="Yoga Flow",
    instructor="John",
    date_time=(now + timedelta(days=1)).replace(tzinfo=None),
    available_slots=20,
    created_by=user1.id,
)


class2 = FitnessClass(
    name="Zumba",
    instructor="Alex",
    date_time=(now + timedelta(days=1)).replace(tzinfo=None),
    available_slots=10,
    created_by=user2.id,
)


class3 = FitnessClass(
    name="HIIT Session",
    instructor="Fraklin",
    date_time=(now + timedelta(days=2)).replace(tzinfo=None),
    available_slots=5,
    created_by=user2.id,
)


class4 = FitnessClass(
    name="Pilates",
    instructor="Chris",
    date_time=(now + timedelta(days=2)).replace(tzinfo=None),
    available_slots=25,
    created_by=user1.id,
)

class5 = FitnessClass(
    name="Kickboxing",
    instructor="Emma",
    date_time=(now + timedelta(days=3)).replace(tzinfo=None),
    available_slots=15,
    created_by=user1.id,
)

db.add_all([
    class1,
    class2,
    class3,
    class4,
    class5
])

db.commit()

for c in [class1,class2,class3,class4,class5]:
    db.refresh(c)

booking1 = Booking(
    class_id=class1.id,
    user_id=user1.id,
    client_name=user1.name,
    client_email=user1.email,
)

booking2 = Booking(
    class_id=class2.id,
    user_id=user1.id,
    client_name=user1.name,
    client_email=user1.email,
)

class1.available_slots -= 1
class2.available_slots -= 1

db.add_all([booking1, booking2])

db.commit()


print("=" * 50)
print("🌱 Seed completed successfully!")
print("=" * 50)

print("\nTest Users:")
print("-------------------------")
print(f"Email    : {user1.email}")
print("Password : Password123")

print()

print(f"Email    : {user2.email}")
print("Password : Password123")

print("\nInserted:")
print("✓ 2 Users")
print("✓ 5 Fitness Classes")
print("✓ 2 Bookings")
print("=" * 50)

db.close()