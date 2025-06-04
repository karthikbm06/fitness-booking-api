from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import db
from models import FitnessClass, Booking
from utils import ist_to_timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/classes", methods=["GET"])
def get_classes():
    timezone_str = request.args.get("timezone", "Asia/Kolkata")
    classes = FitnessClass.query.all()
    result = []
    for c in classes:
        converted_time = ist_to_timezone(c.datetime_ist, timezone_str)
        result.append({
            "id": c.id,
            "name": c.name,
            "datetime": converted_time.strftime('%Y-%m-%d %H:%M'),
            "instructor": c.instructor,
            "available_slots": c.available_slots
        })
    return jsonify(result)

@app.route("/book", methods=["POST"])
def book_class():
    data = request.get_json()
    if not all(k in data for k in ("class_id", "client_name", "client_email")):
        return jsonify({"error": "Missing fields"}), 400

    fitness_class = FitnessClass.query.get(data["class_id"])
    if not fitness_class:
        return jsonify({"error": "Class not found"}), 404
    if fitness_class.available_slots <= 0:
        return jsonify({"error": "Class is fully booked"}), 400

    booking = Booking(class_id=data["class_id"], client_name=data["client_name"], client_email=data["client_email"])
    db.session.add(booking)
    fitness_class.available_slots -= 1
    db.session.commit()
    return jsonify({"message": "Booking successful"})

@app.route("/bookings", methods=["GET"])
def get_bookings():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400
    bookings = Booking.query.filter_by(client_email=email).all()
    result = [{
        "class_id": b.class_id,
        "client_name": b.client_name
    } for b in bookings]
    return jsonify(result)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Welcome to the Fitness Booking API. Available endpoints: /classes, /book, /bookings"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "The requested URL was not found on the server."}), 404

if __name__ == "__main__":
    app.run(debug=True)
