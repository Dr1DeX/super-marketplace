from dataclasses import dataclass

from app.cart.repository import CartRepository
from app.cart.schema import CartSchema, CartCreateSchema
from app.products.schema import ProductSchema


@dataclass
class CartService:
    cart_repository: CartRepository

    async def add_cart(self, cart_item: CartCreateSchema, user_id: int) -> list[CartSchema]:
        await self.cart_repository.add_cart(cart_item=cart_item, user_id=user_id)
        cart_items = await self.cart_repository.get_cart(user_id=user_id)
        cart_schema = [CartSchema.model_validate(items) for items in cart_items]
        return cart_schema

    async def get_cart(self, user_id: int) -> list[ProductSchema]:
        cart_items = await self.cart_repository.get_cart(user_id=user_id)
        cart_items_schema = [ProductSchema.model_validate(items) for items in cart_items]
        return cart_items_schema

