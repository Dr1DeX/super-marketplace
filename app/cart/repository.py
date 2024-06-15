from dataclasses import dataclass

from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.cart.models import Cart
from app.products.schema import ProductAddCartSchema


@dataclass
class CartRepository:
    db_session: AsyncSession

    async def add_cart(self, body: ProductAddCartSchema, user_id: int) -> None:
        query = insert(Cart).values(
            product_name=body.product_name,
            product_price=body.product_price,
            user_id=user_id
        )

        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def get_cart(self, user_id: int) -> list[Cart] | None:
        async with self.db_session as session:
            cart: list[Cart] = (await session.execute(select(Cart).where(Cart.user_id == user_id))).scalars().all()
            return cart
