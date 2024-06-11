from pydantic import BaseModel


class CartSchema(BaseModel):
    id: int | None = None
    product_id: int
    user_id: int

    class Config:
        from_attributes = True


class CartCreateSchema(BaseModel):
    product_id: int
