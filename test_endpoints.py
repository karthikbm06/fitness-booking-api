import requests

BASE_URL = "http://127.0.0.1:5000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    print("GET /")
    print(response.status_code)
    print(response.json())

def test_classes():
    response = requests.get(f"{BASE_URL}/classes")
    print("GET /classes")
    print(response.status_code)
    print(response.json())

def test_book_valid():
    data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/book", json=data)
    print("POST /book (valid)")
    print(response.status_code)
    print(response.json())

def test_book_invalid():
    data = {
        "class_id": 9999,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/book", json=data)
    print("POST /book (invalid class_id)")
    print(response.status_code)
    print(response.json())

def test_bookings_with_email():
    params = {"email": "test@example.com"}
    response = requests.get(f"{BASE_URL}/bookings", params=params)
    print("GET /bookings with email")
    print(response.status_code)
    print(response.json())

def test_bookings_without_email():
    response = requests.get(f"{BASE_URL}/bookings")
    print("GET /bookings without email")
    print(response.status_code)
    print(response.json())

def test_404():
    response = requests.get(f"{BASE_URL}/nonexistent")
    print("GET /nonexistent (404)")
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    test_root()
    test_classes()
    test_book_valid()
    test_book_invalid()
    test_bookings_with_email()
    test_bookings_without_email()
