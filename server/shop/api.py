from fastapi import APIRouter, Depends, HTTPException
from ..db import db
from typing import Annotated
from ..user.lib import get_current_user_id
from .models import Shop

router = APIRouter(
    prefix="/shop",
    tags=["Shop"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_shop(user_id:str= Depends(get_current_user_id)):
    try:
        shop = db.collection('shops').document(user_id).get()
        if shop.exists:
            return shop.to_dict()
        else:
            return {'message':'Shop not found'}
    except Exception as e:
        raise e


@router.post("/")
def create_shop(shop: Shop, user_id:str= Depends(get_current_user_id)):
    try:
        db.collection('shops').document(user_id).set(shop.model_dump())
        return {'message':'Shop created successfully'}
    except Exception as e:
        raise e


@router.put("/")
def update_shop(shop:Shop, user_id:str= Depends(get_current_user_id)):
    try:
        db.collection('shops').document(user_id).update(shop.model_dump())
        return {'message':'Shop updated successfully'}
    except Exception as e:
        raise e


