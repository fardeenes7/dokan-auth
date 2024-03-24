from pydantic import BaseModel
import enum
from typing import Optional, Union


class Shop(BaseModel):
    name: str
    description: Union[str, None] = None
    logo: Union[str, None] = None
    address: Union[str, None] = None
    phone: Union[str, None] = None
