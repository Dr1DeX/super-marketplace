from app.infrastructure.database.accessor import AsyncSessionFactory
from app.orders.repository import OrdersRepository
from app.orders.service import OrdersService
from app.sales.repository import SalesRepository
from app.sales.service import SalesService


def get_sales_service() -> SalesService:
    sales_repository = SalesRepository(db_session=AsyncSessionFactory())
    return SalesService(sales_repository=sales_repository)


def get_orders_service() -> OrdersService:
    orders_repository = OrdersRepository(db_session=AsyncSessionFactory())
    return OrdersService(orders_repository=orders_repository)
