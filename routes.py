from fastapi import APIRouter, HTTPException, Depends, Header
from models.user_model import User
from database.connection import db
from utils.auth import hash_password, verify_password, create_token, verify_token

router = APIRouter()

@router.post("/register")
def register(user: User):
    existing_user = db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user.password = hash_password(user.password)
    db.users.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    db_user = db.users.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token({"email": user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/profile")
def profile(authorization: str = Header(...)):
    token = authorization.split(" ")[1]
    decoded = verify_token(token)
    user = db.users.find_one({"email": decoded["email"]}, {"_id": 0, "password": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
