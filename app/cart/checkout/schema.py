from app.cart.schema import CartSchema

from pydantic import BaseModel


class CheckoutSchema(BaseModel):
    order_id: str | None
    user_id: int
    country: str | None = None
    tel_num: str | None = None
    email: str | None = None
    products: list[CartSchema] = []

    class Config:
        from_attributes = True


class CheckoutCreateSchema(BaseModel):
    country: str | None = None
    tel_num: str | None = None
    email: str | None = None
