from fastapi import APIRouter, Depends, HTTPException
from ..db import db
from .models import Subscription, SubscriptionCoupon, Plan
from typing import Annotated
from ..user.lib import get_current_user_id

router = APIRouter(
    prefix="/subscription",
    tags=["subscription"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def subscribe_user(subscription: Subscription, user_id:str= Depends(get_current_user_id)):
    print(subscription)
    try:
        db.collection('subscriptions').document(user_id).set(subscription.model_dump())
        return {'message':'User subscribed successfully'}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))



@router.get("/")
async def check_subscription(user_id:str = Depends(get_current_user_id)):
    subscription = db.collection('subscriptions').document(user_id).get()
    if subscription.exists:
        subscription =  subscription.to_dict()
        plan = db.collection('plans').document(subscription['plan_id']).get()
        plan = plan.to_dict()
        subscription['plan'] = plan
        return subscription
    return {'plan':'free'}


