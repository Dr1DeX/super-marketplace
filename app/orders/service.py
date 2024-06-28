from dataclasses import dataclass

from app.orders.repository import OrdersRepository
from app.orders.schema import OrdersSchema, OrdersCreateSchema


@dataclass
class OrdersService:
    orders_repository: OrdersRepository

    async def create_orders(
            self,
            products: OrdersCreateSchema,
            order_id: str,
            user_id: int,
            status: str
    ) -> None:
        await self.orders_repository.create_order(
            products=products,
            order_id=order_id,
            user_id=user_id,
            status=status
        )

    async def get_order(self, user_id: int) -> list[OrdersSchema]:
        orders = await self.orders_repository.get_order(user_id=user_id)
        orders_schema = [OrdersSchema.model_validate(item) for item in orders]
        return orders_schema
