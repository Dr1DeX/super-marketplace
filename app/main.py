from fastapi import FastAPI

from app.products.handlers import router as product_router
from app.users.user_profile.handlers import router as user_profile_router
from app.users.auth.handlers import router as auth_router
from app.cart.handlers import router as cart_router
from app.cart.checkout.handlers import router as checkout_router
from app.orders.handlers import router as orders_router

app = FastAPI(title='Super marketplace')

app.include_router(product_router)
app.include_router(user_profile_router)
app.include_router(auth_router)
app.include_router(cart_router)
app.include_router(checkout_router)
app.include_router(orders_router)
