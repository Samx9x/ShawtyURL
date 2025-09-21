# URL Shortener Microservice (Backend)

This is a Django-based backend microservice that provides functionality to shorten URLs, track usage, and fetch analytics.  
It was built as per the assignment requirements.

---

## 🚀 Features
- Generate short URLs with **custom or auto-generated shortcodes**
- Set **expiry time** (default: 30 minutes)
- Redirect to the original URL if valid, otherwise return an error
- Track click statistics (IP, timestamp, user agent, referrer)
- Logging middleware that sends logs to the evaluation server

---

## 🛠 Tech Stack
- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite (default DB)
- Requests (for log API)

---

## 📦 Setup Instructions

### 1. Clone repo & enter project
```bash
git clone <your_repo_url>
cd url_shortener
```
### 2. Setup virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
pip freeze > requirements.txt
```
### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Start server
```bash
python manage.py runserver
````
Server runs at: http://127.0.0.1:8000/
## 📌 API Endpoints
1. Create Short URL

Endpoint: POST /shorturls
Description: Create a new short URL with a specified validity period.

Request Body:

{
  "url": "https://www.google.com",
  "validity": 10,
  "shortcode": "goog1"
}


Response:

{
  "shortLink": "http://127.0.0.1:8000/goog1",
  "expiry": "2025-09-21T15:10:00Z"
}


Notes:

validity is in minutes.

shortcode must be unique.

2. Redirect Short URL

Endpoint: GET /<shortcode>
Description: Redirects to the original URL if it is still valid.

Examples:

http://127.0.0.1:8000/goog1

Responses:

Success: Redirects to the original URL.

Expired URL:

{
  "error": "URL expired"
}


Invalid shortcode:

{
  "error": "Shortcode not found"
}

3. Stats for Short URL

Endpoint: GET /shorturls/<shortcode>
Description: Retrieves details and click statistics for a short URL.

Response:

{
  "url": {
    "shortcode": "goog1",
    "original_url": "https://www.google.com",
    "expiry": "2025-09-21T15:10:00Z",
    "created_at": "2025-09-21T14:40:00Z",
    "clicks": 2
  },
  "clicks": [
    {
      "timestamp": "2025-09-21T14:41:00Z",
      "referrer": null,
      "ip": "127.0.0.1",
      "ua": "PostmanRuntime/7.39.0"
    }
  ]
}

📝 Logging Middleware

All requests are logged to the evaluation service for monitoring and debugging.

Logging Endpoint: POST http://20.244.56.144/evaluation-service/logs

Payload Example:

{
  "stack": "backend",
  "level": "info",
  "package": "middleware",
  "message": "POST /shorturls -> 201"
}

## sample outputs:
api alling:
<img width="1295" height="715" alt="image" src="https://github.com/user-attachments/assets/a7064e85-a159-40a2-abcd-55887216983b" />
default values:
<img width="1452" height="794" alt="image" src="https://github.com/user-attachments/assets/b8fd2a7a-15e4-4575-a004-fe4c27ce3602" />
<img width="1244" height="643" alt="image" src="https://github.com/user-attachments/assets/e6d828ab-8979-4d3b-a68c-9a3da9b8189d" />
get request:
<img width="1354" height="734" alt="image" src="https://github.com/user-attachments/assets/450bb70b-cda8-46d8-9128-1b563188c360" />


