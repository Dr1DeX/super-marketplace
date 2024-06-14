from dataclasses import dataclass

from app.sales.repository import SalesRepository
from app.sales.schema import SalesOrderSchema, SalesOrderCreateSchema

@dataclass
class SalesService:
    sales_repository: SalesRepository

    async def create_order(self, body: SalesOrderCreateSchema):
        order = await self.sales_repository.create_order(body=body)
        print(order)