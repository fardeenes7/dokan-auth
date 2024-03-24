from fastapi import FastAPI
from .subscription.api import router as subscription_router
from .user.api import router as user_router
from .shop.api import router as shop_router


app = FastAPI()
app.include_router(user_router)
app.include_router(shop_router)
app.include_router(subscription_router)
