from pydantic import BaseModel
import enum
from typing import Optional, Union


class Shop(BaseModel):
    id: str
    owner_id: str
    name: str
    description: Union[str, None] = None
    logo: Union[str, None] = None
    address: Union[str, None] = None
    phone: Union[str, None] = None


class Manager(BaseModel):
    user_id: str
    shop_id: str
    role: str





