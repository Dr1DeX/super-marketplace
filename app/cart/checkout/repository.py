from dataclasses import dataclass

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.cart.checkout.models import UserContactInfo
from app.cart.checkout.schema import UserCreateContactInfoSchema
from app.cart.models import CartItem
from app.products.models import Products


@dataclass
class CheckoutRepository:
    db_session: AsyncSession

    async def create_order(self, body: UserCreateContactInfoSchema, user_id: int, product_id: int) -> int:
        prd_id = select(CartItem.product_id).where(CartItem.product_id == product_id)
        query = insert(UserContactInfo).values(
            user_id=user_id,
            product_id=prd_id,
            **body.dict(exclude_none=True)
        ).returning(UserContactInfo.id)

        async with self.db_session as session:
            order_id: int = (await session.execute(query)).scalar()
            await session.commit()
            await session.flush()
            return order_id

    async def get_order(self, order_id: int, user_id: int) -> UserContactInfo:
        query = select(UserContactInfo).where(UserContactInfo.id == order_id).where(UserContactInfo.user_id == user_id)

        async with self.db_session as session:
            order: UserContactInfo = (await session.execute(query)).scalar_one_or_none()
            return order
