from dataclasses import dataclass

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.cart.models import CartItem
from app.cart.schema import CartCreateSchema


@dataclass
class CartRepository:
    db_session: AsyncSession

    async def add_cart(self, cart_item: CartCreateSchema, user_id: int) -> None:
        query = insert(CartItem).values(
            user_id=user_id,
            product_id=cart_item.product_id,
        )

        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def get_cart(self, user_id: int) -> list[CartItem]:
        query = select(CartItem).where(CartItem.user_id == user_id)

        async with self.db_session as session:
            cart_items: list[CartItem] = (await session.execute(query)).scalars().all()
            return cart_items
