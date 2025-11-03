import sqlite3
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from queries import *
from config_backend import DB_NAME, UserSignup, UserLogin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Piggie Bank Backend", version="1.0.0")
# connect to the database
connect_db = get_connection(db_name=DB_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup")
async def signup(user: UserSignup):
    print("🔄 Received signup request for user:", user.email)
    try:
        # Ensure table exists
        create_table_user(connect_db)

        # Generate unique identifiers
        user_id = str(uuid.uuid4())
        session_token = str(uuid.uuid4())

        # Insert user into DB
        insert_user(conn=connect_db, user=user)

    except sqlite3.IntegrityError as e:
        # Handle duplicate email error
        if "UNIQUE constraint failed: users.email" in str(e):
            print("❌ Email already exists:", user.email)
            raise HTTPException(status_code=400, detail="Email already exists.")
        else:
            print("❌ Database integrity error:", e)
            raise HTTPException(status_code=400, detail="Database integrity error.")
    except Exception as e:
        print("❌ Error creating user:", e)
        raise HTTPException(status_code=500, detail=str(e))

    # Return useful session info
    return {
        "message": "User created successfully",
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "token": session_token
    }


@app.post("/login")
async def login(data: UserLogin):
    print("🔄 Received login request for:", data.email)
    
    # Retrieve the user from the database
    user_row = get_user_by_email(connect_db, data.email)
    print("🔍 Fetched user data:", user_row)

    if not user_row:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Since your get_user_by_email currently doesn't return password, fetch it separately
    cursor = connect_db.execute("SELECT password FROM users WHERE email = ?", (data.email,))
    row = cursor.fetchone()
    if not row or row[0] != data.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Generate a session token
    session_token = str(uuid.uuid4())

    return {
        "message": "User logged in successfully",
        "user_id": user_row["user_id"],
        "name": user_row["name"],
        "email": user_row["email"],
        "token": session_token
    }


