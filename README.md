# Fitness Studio Booking API

## Setup Instructions

```bash
pip install -r requirements.txt
python seed_data.py
python app.py
```

## Sample API Requests

### View Classes (IST to UTC):
```bash
curl http://127.0.0.1:5000/classes?timezone=UTC
```

### Book a Class:
```bash
curl -X POST http://127.0.0.1:5000/book -H "Content-Type: application/json" -d "{\"class_id\": 2, \"client_name\": \"Karthik B M\", \"client_email\": \"karthikbm@example.com\"}"

```

### Get Bookings by Email:
```bash
curl http://127.0.0.1:5000/bookings?email=karthikbm@example.com
```
