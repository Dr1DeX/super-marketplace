from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    product_count: int | None = None
    category_id: int

    class Config:
        from_attributes = True


class CategorySchema(BaseModel):
    id: int | None = None
    name: str | None = None

    class Config:
        from_attributes = True