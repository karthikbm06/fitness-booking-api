from app import app
from database import db
from models import FitnessClass
from datetime import datetime

with app.app_context():
    db.create_all()
    classes = [
        FitnessClass(name="Yoga", datetime_ist=datetime(2025, 6, 10, 7, 0), instructor="Anjali", available_slots=10),
        FitnessClass(name="Zumba", datetime_ist=datetime(2025, 6, 10, 9, 0), instructor="Rahul", available_slots=8),
        FitnessClass(name="HIIT", datetime_ist=datetime(2025, 6, 10, 11, 0), instructor="Sneha", available_slots=5),
    ]
    db.session.bulk_save_objects(classes)
    db.session.commit()
    print("Seed data inserted.")
