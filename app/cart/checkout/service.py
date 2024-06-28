from dataclasses import dataclass
from app.cart.checkout.repository import CheckoutRepository
from app.cart.checkout.schema import CheckoutSchema, CheckoutCreateSchema
from workers.utils.publisher_rq import send_to_message


@dataclass
class CheckoutService:
    checkout_repository: CheckoutRepository

    async def create_order(self, body: CheckoutCreateSchema, user_id: int) -> list[CheckoutSchema]:
        order = await self.checkout_repository.create_order(checkout_data=body, user_id=user_id)
        order_schema = [CheckoutSchema.model_validate(item) for item in order]
        await send_to_message(
            exchange_name='user_info',
            routing_key='sales',
            message_body=order
        )
        return order_schema
