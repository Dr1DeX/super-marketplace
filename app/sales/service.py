from dataclasses import dataclass

from app.sales.repository import SalesRepository
from app.sales.schema import SalesOrderSchema, SalesOrderCreateSchema


@dataclass
class SalesService:
    sales_repository: SalesRepository

    async def create_order(self, body: SalesOrderCreateSchema) -> None:
        await self.sales_repository.create_order(body=body)

    async def get_order(self, order_id: str) -> list[SalesOrderSchema]:
        orders = await self.sales_repository.get_order(order_id=order_id)
        orders_schema = [SalesOrderSchema.model_validate(item) for item in orders]
        return orders_schema
