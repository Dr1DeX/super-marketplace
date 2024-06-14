from dataclasses import dataclass

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.sales.models import ProcessedOrders
from app.sales.schema import SalesOrderCreateSchema


@dataclass
class SalesRepository:
    db_session: AsyncSession

    async def create_order(self, body: SalesOrderCreateSchema):
        query = insert(ProcessedOrders).values(
            **body.dict(exclude_none=True)
        )
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()