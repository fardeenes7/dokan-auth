from fastapi import FastAPI, Depends, HTTPException, Request
from firebase_admin import auth, firestore
from fastapi import APIRouter
from ..db import db
from typing import Annotated
from .lib import get_user_by_id, get_current_user_id, check_subscription, get_current_user

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)




@router.get("/me")
async def get_user(user:dict=Depends(get_current_user)):
    try:
        return user
    except Exception as e:
        raise e


@router.get("/{user_id}")
async def get_user(user_id:str, current_user_id:str = Depends(get_current_user_id)):
    user = await get_user_by_id(user_id, current_user_id)
    return user