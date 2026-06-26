# 🏋️ FitBook API

A production-inspired RESTful backend API for managing fitness studio classes and bookings. Built with **FastAPI**, **SQLAlchemy**, **PostgreSQL (Supabase)**, and **JWT Authentication**, the project demonstrates authentication, relational database design, API development, request validation, logging, timezone handling, and clean backend architecture.

---

## ✨ Features

* 🔐 JWT Authentication (Sign Up & Login)
* 👤 Secure user registration and authentication
* 📅 Create fitness classes
* 📋 View upcoming fitness classes
* 🎟️ Book available fitness classes
* 👀 View authenticated user's bookings
* ⛔ Prevent duplicate bookings
* ⛔ Prevent overbooking
* 🕒 Timezone-aware date handling (IST)
* ✅ Request validation using Pydantic V2
* 📝 Structured application logging
* 🌱 Seed script for demo data
* 📖 Interactive Swagger API Documentation

---

# 🛠 Tech Stack

| Category              | Technology                        |
| --------------------- | --------------------------------- |
| Backend               | FastAPI                           |
| Language              | Python 3.13                       |
| Database              | PostgreSQL (Supabase)             |
| ORM                   | SQLAlchemy 2.0                    |
| Validation            | Pydantic V2                       |
| Authentication        | JWT (python-jose)                 |
| Password Hashing      | Passlib + bcrypt                  |
| Environment Variables | python-dotenv + pydantic-settings |
| ASGI Server           | Uvicorn                           |
| Timezone              | zoneinfo                          |
| API Testing           | Swagger UI / Postman              |

---

# 📂 Folder Structure

```text
fitness-booking-api/
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── logger.py
│   ├── database.py
│   ├── config.py
│   ├── dependencies.py
│   └── main.py
│
│
├── seed.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/fitness-booking-api.git
```

```bash
cd fitness-booking-api
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Copy

```bash
.env.example
```

to

```bash
.env
```

and update the values.

---

# ⚙️ Environment Variables

| Variable                    | Description                  | Example                                 |
| --------------------------- | ---------------------------- | --------------------------------------- |
| DATABASE_URL                | PostgreSQL connection string | postgresql://user:password@host:5432/db |
| SECRET_KEY                  | JWT Secret Key               | my-super-secret-key                     |
| ALGORITHM                   | JWT Algorithm                | HS256                                   |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiry in minutes      | 30                                      |

---

# ▶️ Running the Application

Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🌱 Seed Demo Data

Populate the database with sample users, classes and bookings.

```bash
python seed.py
```

### Demo Users

| Email                                         | Password    |
| --------------------------------------------- | ----------- |
| [john@example.com](mailto:john@example.com)   | Password123 |
| [alice@example.com](mailto:alice@example.com) | Password123 |

Seed inserts

* ✅ 2 Users
* ✅ 5 Fitness Classes
* ✅ 2 Bookings

---

# 📌 API Usage

---

## 1️⃣ Register User

**POST**

```
/auth/signup
```

```bash
curl -X POST http://127.0.0.1:8000/auth/signup \
-H "Content-Type: application/json" \
-d '{
"name":"John Doe",
"email":"john@example.com",
"password":"Password123"
}'
```

---

## 2️⃣ Login

**POST**

```
/auth/login
```

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=john@example.com&password=Password123"
```

---

## 3️⃣ Create Fitness Class

**POST**

```
/classes
```

```bash
curl -X POST http://127.0.0.1:8000/classes \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
"name":"Yoga Flow",
"dateTime":"2026-07-15T09:00:00+05:30",
"instructor":"John",
"availableSlots":20
}'
```

---

## 4️⃣ Get Upcoming Classes

**GET**

```
/classes
```

```bash
curl -X GET http://127.0.0.1:8000/classes \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

---

## 5️⃣ Book a Class

**POST**

```
/book
```

```bash
curl -X POST http://127.0.0.1:8000/book \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
"class_id":1,
"client_name":"John Doe",
"client_email":"john@example.com"
}'
```

---

## 6️⃣ View My Bookings

**GET**

```
/bookings
```

```bash
curl -X GET http://127.0.0.1:8000/bookings \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

---

# 📋 Validation Rules

* User email must be unique.
* Password is securely hashed using bcrypt.
* Class date must be in the future.
* Available slots must be greater than zero.
* Duplicate bookings are not allowed.
* Booking is rejected when no slots are available.
* Only authenticated users can access protected endpoints.

---

# 📝 Logging

The application records important events using Python's built-in logging module.

Examples include:

* User registration
* User login
* Fitness class creation
* Booking creation
* Authentication failures
* Duplicate booking attempts
* Validation failures

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 👨‍💻 Author

**Naresh Mahapatra**

GitHub: https://github.com/NareshXcodes
