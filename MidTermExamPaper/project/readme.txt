Vehicle Rental System - FastAPI

Name: Naba Yousuf
Roll Number: SE231020

Domain: Vehicle Rental System

Database Filename: vehicle_rental.db

Installation

Clone or download the project folder.

Install required packages:

pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt]


Run the application:

uvicorn main:app --reload


API Base URL: http://127.0.0.1:8000

Access Swagger UI for testing at: http://127.0.0.1:8000/docs

Test Credentials

Admin User:

Username: admin_1020

Password: adminpass

Regular User:

Username: naba_1020

Password: pass


API Endpoints

POST /auth/register

Register a new user (admin or regular).

Request Body: username, email, password, full_name

Response: User object (without password)

POST /auth/token

Login endpoint.

Request Body: username and password (OAuth2PasswordRequestForm)

Response: JWT access_token and token_type

GET /auth/profile

Retrieve the currently authenticated user's profile.

Requires Bearer token.

POST /api/items/

Create a new vehicle.

Request Body: vehicle_name, registration_no, vehicle_type, daily_rate, is_available, seating_capacity

Requires Bearer token.

GET /api/items/

List all vehicles.

Admin sees all, regular users see only their vehicles.

Supports pagination: skip and limit query parameters.

GET /api/items/{item_id}

Retrieve a single vehicle by ID.

Ownership checks enforced.

PATCH /api/items/{item_id}

Update an existing vehicle.

Ownership checks enforced.

Only changed fields need to be sent in request body.

DELETE /api/items/{item_id}

Delete a vehicle.

Ownership checks enforced.

Response: {"message": "Item deleted successfully"}

Testing Steps (Part G)

Register admin and regular users using /auth/register.

Login using /auth/token to get JWT tokens.

Create 4 vehicles:

2 vehicles as admin

2 vehicles as regular user

Test /api/items/ endpoints:

List vehicles as admin → should see all 4

List vehicles as regular → should see only own 2

Get a vehicle by ID → check ownership rules

Update a vehicle → verify only owner/admin can update

Delete a vehicle → verify only owner/admin can delete

Test unauthorized access (no token) → should return 401

Test forbidden access (accessing others' vehicles) → should return 403

Notes

SECRET_KEY includes roll number: fastapi-secret-se23102

Usernames must include last 4 digits of roll: admin_3102, user_3102

Database file: vehicle_rental.db in project folder

All timestamps are in UTC

Minimum 4 screenshots required for submission:

Folder structure

User registration

Login response

Create item

List items

Get single item

Update item

Delete item

Unauthorized error

Forbidden error