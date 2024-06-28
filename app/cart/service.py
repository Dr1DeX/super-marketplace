from dataclasses import dataclass

from app.cart.repository import CartRepository
from app.cart.schema import CartSchema, CartCreateSchema
from app.products.schema import ProductAddCartSchema


@dataclass
class CartService:
    cart_repository: CartRepository

    async def add_cart(self, body: ProductAddCartSchema, user_id: int) -> list[CartSchema]:
        await self.cart_repository.add_cart(body=body, user_id=user_id)
        cart_items = await self.cart_repository.get_cart(user_id=user_id)
        cart_schema = [CartSchema.model_validate(item) for item in cart_items]
        return cart_schema

    async def get_cart(self, user_id: int) -> list[CartSchema]:
        cart_items = await self.cart_repository.get_cart(user_id=user_id)
        cart_schema = [CartSchema.model_validate(item) for item in cart_items]
        return cart_schema

    async def update_product_quantity(self, user_id: int, product_id: int, method: str) -> list[CartSchema]:
        await self.cart_repository.update_quantity(
            user_id=user_id,
            product_id=product_id,
            method=method
        )
        products = await self.cart_repository.get_cart(user_id=user_id)
        cart_schema = [CartSchema.model_validate(item) for item in products]
        return cart_schema
