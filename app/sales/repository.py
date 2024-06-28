from dataclasses import dataclass

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.sales.models import ProcessedOrders
from app.sales.schema import SalesOrderCreateSchema
from app.users.user_profile.models import UserProfile


@dataclass
class SalesRepository:
    db_session: AsyncSession

    async def create_order(self, body: SalesOrderCreateSchema):
        async with self.db_session as session:
            for item in body:
                for product in item['products']:
                    query = insert(ProcessedOrders).values(
                        order_id=item['order_id'],
                        user_id=item['user_id'],
                        country=item['country'],
                        tel_num=item['country'],
                        email=item['email'],
                        product_name=product['product_name'],
                        product_quantity=product['product_quantity'],
                        product_price=product['product_price'],
                        status=product.get('status') or 'Created'
                    )
                    await session.execute(query)
            await session.commit()

    async def get_order(self, username: str) -> list[ProcessedOrders]:
        query = (
            select(ProcessedOrders)
            .join(UserProfile, ProcessedOrders.user_id == UserProfile.id)
            .where(UserProfile.username == username)
        )

        async with self.db_session as session:
            order: list[ProcessedOrders] = (await session.execute(query)).scalars().all()
            return order
