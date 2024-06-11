from pydantic import BaseModel


class UserContactInfoSchema(BaseModel):
    id: int | None = None
    product_id: int
    user_id: int
    country: str | None = None
    email: str | None = None
    address: str | None = None
    tel_number: str | None = None

    class Config:
        from_attributes = True


class UserCreateContactInfoSchema(BaseModel):
    country: str | None = None
    email: str | None = None
    address: str | None = None
    tel_number: str | None = None
