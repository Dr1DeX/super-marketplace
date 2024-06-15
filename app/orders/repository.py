from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from app.orders.models import Orders
from app.orders.schema import OrdersCreateSchema


@dataclass
class OrdersRepository:
    db_session: AsyncSession

    async def create_order(self, products: OrdersCreateSchema, order_id: str, user_id: int, status: str) -> None:
        async with self.db_session as session:
            for product in products:
                query = insert(Orders).values(
                    user_id=user_id,
                    order_id=order_id,
                    status=status,
                    product_name=product['product_name'],
                    product_price=product['product_price'],
                    product_quantity=product['product_quantity']
                )
                await session.execute(query)
            await session.commit()

    async def get_order(self, user_id: int) -> list[Orders]:
        query = select(Orders).where(Orders.user_id == user_id)

        async with self.db_session as session:
            orders: list[Orders] = (await session.execute(query)).scalars().all()
            return orders
