# FastAPI MVC Application

## Project Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn app.main:app --reload`
4. Access the API documentation at `http://127.0.0.1:8000/docs`

## Endpoints

### Auth Endpoints
- **POST /auth/signup**: Register a new user.
- **POST /auth/login**: Obtain a token for an existing user.

### Post Endpoints
- **POST /v1/posts**: Create a new post (requires token).
- **GET /v1/posts/**: Retrieve all posts for the current user (requires token).
- **DELETE /v1/posts/{post_id}**: Delete a specific post (requires token).

## Database Setup
The database will be automatically created when you run the application.

## Caching
The `GET /posts/` endpoint uses in-memory caching with a TTL of 5 minutes.


