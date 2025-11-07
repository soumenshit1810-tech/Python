from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Database simulation
users = {}

# Data Model
class User(BaseModel):
    name: str
    email: str
    age: int

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Backend!"}

# Create user
@app.post("/users/")
def create_user(user: User):
    if user.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.email] = user
    return {"message": "User created successfully", "user": user}

# Get all users
@app.get("/users/")
def get_users():
    return {"users": list(users.values())}

# Get a single user
@app.get("/users/{email}")
def get_user(email: str):
    if email not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[email]

# Update user
@app.put("/users/{email}")
def update_user(email: str, updated_user: User):
    if email not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[email] = updated_user
    return {"message": "User updated", "user": updated_user}

# Delete user
@app.delete("/users/{email}")
def delete_user(email: str):
    if email not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[email]
    return {"message": "User deleted successfully"}
