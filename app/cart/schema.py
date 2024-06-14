from pydantic import BaseModel


class CartSchema(BaseModel):
    id: int | None = None
    product_name: str | None = None
    quantity: int | None = None
    price: int | None = None
    user_id: int

    class Config:
        from_attributes = True


class CartCreateSchema(BaseModel):
    name: str | None = None
    quantity: int | None = None
    price: int | None = None
