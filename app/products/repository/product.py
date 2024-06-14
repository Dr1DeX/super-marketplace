from dataclasses import dataclass
from typing import Dict, Optional, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm.base import _T_co

from app.products.models import Products, Categories


@dataclass
class ProductRepository:
    db_session: AsyncSession

    async def get_products(self) -> list[Products]:
        async with self.db_session as session:
            products: list[Products] = (await session.execute(select(Products))).scalars().all()
            return products

    async def get_product(self, product_id) -> Products | None:
        async with self.db_session as session:
            product: Products = (
                await session.execute(select(Products).where(Products.id == product_id))).scalar_one_or_none()
            return product

    async def get_categories(self) -> list[Categories]:
        async with self.db_session as session:
            categories: list[Categories] = (await session.execute(select(Categories))).scalars().all()
            return categories

    async def get_products_by_categories_name(self, category_name: str) -> list[Products]:
        query = (select(Products)
                 .join(Categories, Products.category_id == Categories.id)
                 .where(Categories.name == category_name))

        async with self.db_session as session:
            products: list[Products] = (await session.execute(query)).scalars().all()
            return products

    async def add_product(self, product_id: int) -> Products:
        query = select(Products.product_name, Products.price).where(Products.id == product_id)

        async with self.db_session as session:
            product = (await session.execute(query)).scalar_one_or_none()
            return product

