from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import credentials, firestore, initialize_app, auth
from pydantic import BaseModel
from typing import Optional
import os
import requests
app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize Firestore
cred = credentials.Certificate(os.path.join(BASE_DIR,"service-account.json"))
firebase = initialize_app(cred)
db = firestore.client()



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@app.get("/login/social/{provider}")
async def social_login(provider:str, request:Request):
    # parse token from request header
    token = request.headers.get('Authorization').split('Bearer ')[1]
    # validate token with social provider
    try:
        decoded_token = auth.verify_id_token(token)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # return  decoded_token(user info)
    return decoded_token


@app.get("/users/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        token = token.split('Bearer ')[1]
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
    except:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # get user data from firestore
    user = db.collection('users').document(uid).get()
    return user.to_dict()


