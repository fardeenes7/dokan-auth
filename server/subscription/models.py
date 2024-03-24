from pydantic import BaseModel
import enum
from typing import Optional

class Plan(BaseModel):
    name: str
    price: float
    duration: int
    max_products: int    


class Subscription(BaseModel):
    plan_id:str
    status:str
    start_date:str
    end_date:str
    note:str


class SubscriptionCoupon(BaseModel):
    id: int
    code: str
    discount: float
    discount_type: str = 'percentage'
    max_uses: int
    start_date: Optional[str]
    end_date: str

