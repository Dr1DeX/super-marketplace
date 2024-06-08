from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db_session
from app.products.repository import ProductRepository
from app.products.service import ProductService


async def get_products_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> ProductRepository:
    return ProductRepository(db_session=db_session)


async def get_product_service(
        product_repository: ProductRepository = Depends(get_products_repository)
) -> ProductService:
    return ProductService(product_repository=product_repository)
