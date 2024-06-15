from pydantic import BaseModel


class CartSchema(BaseModel):
    id: int | None = None
    product_name: str | None = None
    product_quantity: int | None = None
    product_price: int | None = None
    user_id: int

    class Config:
        from_attributes = True


class CartCreateSchema(BaseModel):
    product_name: str | None = None
    product_quantity: int | None = None
    product_price: int | None = None
