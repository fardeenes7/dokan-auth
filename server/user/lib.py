from fastapi import FastAPI, Depends, HTTPException, Request
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError
from fastapi import APIRouter
from ..db import db
from typing import Annotated



def _authenticate(request: Request) -> str:
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            raise HTTPException(status_code=401, detail="Authorization header is missing")
        token = auth_header.replace('Bearer ', '')
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except KeyError:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token format")
    except FirebaseError as e:
        raise HTTPException(status_code=401, detail=f"Firebase authentication error: {e}")
    except Exception as e:  # Catch other unexpected errors
        raise e


def _get_user_role(uid: str):
    try:
        user = db.collection('users').document(uid).get()
        if user.exists:
            return user.to_dict().get('role')
    except Exception as e:
        raise e


async def check_subscription(user_id: str):
    subscription = db.collection('subscriptions').document(user_id).get()
    if subscription.exists:
        return subscription.to_dict()
    return {'plan': 'free'}



async def get_current_user_id(request: Request):
    return "H3LU71CrQ3cPsoDqt4shFTtFwPv1"
    try:
        user_id = _authenticate(request)
        return user_id
    except Exception as e:
        raise e


async def get_current_user(user_id:str = Depends(get_current_user_id)):
    try:
        print("get_current_user Code is here")
        user = db.collection('users').document(user_id).get().to_dict()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        user['subscription'] = await check_subscription(user_id)
        return user
    except Exception as e:
        raise e


async def get_user_by_id(user_id: str, current_user_id:str= Depends(get_current_user_id)):
    try:
        allowed_roles = ['admin']
        if _get_user_role(current_user_id) not in allowed_roles:
            return HTTPException(status_code=401, detail="Unauthorized")
        user = db.collection('users').document(user_id).get().to_dict()
        if user is None:
            return HTTPException(status_code=404, detail="User not found")
        user['subscription'] = await check_subscription(user_id)
        return user
    except Exception as e:
        raise e




