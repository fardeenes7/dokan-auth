from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import credentials, firestore, initialize_app
from pydantic import BaseModel
from typing import Optional
import os
import requests
app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize Firestore
cred = credentials.Certificate(os.path.join(BASE_DIR,"service-account.json"))
initialize_app(cred)
db = firestore.client()



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@app.post("/login/social/{provider}")
async def social_login(provider:str, request:Request):
    # parse token from request header
    token = request.headers.get('Authorization').replace("Bearer ", "")
    # validate token with social provider

    # exchange token with auth backend
    # return access token from auth backend


    # # Assuming the collection name is "users"
    # users_ref = db.collection("users")
    # user_doc = users_ref.where("provider", "==", provider).where("token", "==", token).limit(1).get()

    # if not user_doc:
    #     raise HTTPException(status_code=401, detail="Invalid credentials")

    # user_data = user_doc[0].to_dict()

    # return user_data

    return {'provider': provider, 'token': token}

# Dummy endpoint for demonstration purposes
@app.get("/users/me")
async def read_current_user(token: str = Depends(oauth2_scheme)):
    # Assuming the collection name is "users"
    users_ref = db.collection("users")
    user_doc = users_ref.where("token", "==", token).limit(1).get()

    if not user_doc:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_data = user_doc[0].to_dict()
    return user_data
