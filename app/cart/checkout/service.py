from dataclasses import dataclass

from app.cart.checkout.repository import CheckoutRepository
from app.cart.checkout.schema import UserCreateContactInfoSchema, UserContactInfoSchema


@dataclass
class CheckoutService:
    checkout_repository: CheckoutRepository

    async def create_orders(
            self,
            body: UserCreateContactInfoSchema,
            user_id: int,
            product_id: int) -> UserContactInfoSchema:

        order_id = await self.checkout_repository.create_order(body=body, user_id=user_id, product_id=product_id)
        order = await self.checkout_repository.get_order(order_id=order_id, user_id=user_id)
        return UserContactInfoSchema.model_validate(order)

    async def get_order(self, order_id: int, user_id: int) -> UserContactInfoSchema:
        order = await self.checkout_repository.get_order(order_id=order_id, user_id=user_id)
        return UserContactInfoSchema.model_validate(order)

