from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.cart.checkout.schema import CheckoutCreateSchema
from app.cart.models import Cart

import uuid


@dataclass
class CheckoutRepository:
    db_session: AsyncSession

    async def create_order(self, checkout_data: CheckoutCreateSchema, user_id: int) -> list[dict]:
        cart_user = select(Cart).where(Cart.user_id == user_id)

        async with self.db_session as session:
            items = (await session.execute(cart_user)).scalars().all()
            products = []

            for item in items:
                product_data = {
                    'id': item.id,
                    'product_name': item.product_name,
                    'product_quantity': item.product_quantity,
                    'product_price': item.product_price,
                    'user_id': item.user_id
                }
                products.append(product_data)

            order = [{
                'order_id': str(uuid.uuid4()),
                'user_id': user_id,
                'status': 'Created',
                **checkout_data.dict(exclude_none=True),
                'products': products
            }]

            return order
