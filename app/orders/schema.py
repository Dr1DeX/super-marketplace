from pydantic import BaseModel

from app.cart.schema import CartSchema


class OrdersSchema(BaseModel):
    id: int
    user_id: int
    order_id: str | None = None
    status: str | None = None
    product_name: str | None = None
    product_quantity: int | None = None
    product_price: int | None = None

    class Config:
        from_attributes = True


class OrdersCreateSchema(BaseModel):
    status: str | None = None
    products: list[CartSchema] = []
