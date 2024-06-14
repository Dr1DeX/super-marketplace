from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int | None = None
    product_name: str | None = None
    product_count: int | None = None
    category_id: int
    price: int | None = None

    class Config:
        from_attributes = True


class ProductAddCartSchema(BaseModel):
    product_name: str | None = None
    price: int | None = None

    class Config:
        from_attributes = True


class CategorySchema(BaseModel):
    id: int | None = None
    name: str | None = None

    class Config:
        from_attributes = True
