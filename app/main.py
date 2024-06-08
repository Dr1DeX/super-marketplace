from fastapi import FastAPI

from app.products.handlers import router as product_router

app = FastAPI(title='Super marketplace')

app.include_router(product_router)
