from pydantic import BaseModel

from app.cart.schema import CartSchema


class SalesOrderSchema(BaseModel):
    id: int | None = None
    order_id: str | None = None
    user_id: int
    country: str | None = None
    tel_num: str | None = None
    email: str | None = None
    products: list[CartSchema] = []

    class Config:
        from_attributes = True


class SalesOrderCreateSchema(BaseModel):
    order_id: str | None = None
    user_id: int
    country: str | None = None
    tel_num: str | None = None
    email: str | None = None
    products: list[CartSchema] = []
