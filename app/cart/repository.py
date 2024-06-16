from dataclasses import dataclass

from sqlalchemy import select, update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.cart.models import Cart
from app.exception import ProductOutOfStockException, ProductNotFoundException, UpdateMethodNotFoundException
from app.products.models import Products
from app.products.schema import ProductAddCartSchema


@dataclass
class CartRepository:
    db_session: AsyncSession

    async def add_cart(self, body: ProductAddCartSchema, user_id: int) -> None:
        async with self.db_session as session:
            existing_cart_item = await session.execute(
                select(Cart).where(Cart.product_name == body.product_name, Cart.user_id == user_id)
            )
            existing_cart_item = existing_cart_item.scalar_one_or_none()

            if existing_cart_item:
                query = (
                    update(Cart)
                    .where(Cart.id == existing_cart_item.id)
                    .values(product_quantity=existing_cart_item.product_quantity + 1)
                )
                await session.execute(query)
            else:
                query = insert(Cart).values(
                    product_name=body.product_name,
                    product_price=body.product_price,
                    user_id=user_id
                )
                await session.execute(query)

            await session.commit()

    async def update_quantity(self, user_id: int, product_id: int, method: str) -> None:
        async with self.db_session as session:
            exist_product = await session.execute(
                select(Products)
                .join(Cart, Products.product_name == Cart.product_name)
                .where(Cart.user_id == user_id)
            )
            exist_product = exist_product.scalar_one_or_none()

            if exist_product:
                if method == 'plus':
                    if exist_product.product_count > 0:
                        await self._increment_quantity(
                            session=session,
                            exist_product=exist_product,
                            user_id=user_id,
                            product_id=product_id
                        )
                    else:
                        raise ProductOutOfStockException
                elif method == 'minus':
                    await self._decrement_quantity(
                        session=session,
                        exist_product=exist_product,
                        user_id=user_id,
                        product_id=product_id
                    )
                else:
                    raise UpdateMethodNotFoundException
            else:
                raise ProductNotFoundException

    async def _increment_quantity(
            self,
            session: AsyncSession,
            exist_product: Products,
            user_id: int,
            product_id: int
    ):
        query = (
            update(Cart)
            .where(Cart.user_id == user_id, Cart.product_name == exist_product.product_name)
            .values(product_quantity=Cart.product_quantity + 1)
        )
        product_query = (
            update(Products)
            .where(Products.id == product_id, Products.product_count >= 0)
            .values(product_count=Products.product_count - 1)
        )
        await session.execute(query)
        await session.execute(product_query)
        await session.commit()

    async def _decrement_quantity(
            self,
            session: AsyncSession,
            exist_product: Products,
            user_id: int,
            product_id: int
    ):
        cart_item = await session.execute(
            select(Cart)
            .where(Cart.user_id == user_id, Cart.product_name == exist_product.product_name)
        )
        cart_item = cart_item.scalar_one_or_none()
        if cart_item.product_quantity <= 1:
            await session.execute(
                delete(Cart)
                .where(Cart.user_id == user_id, Cart.product_name == exist_product.product_name)
            )
            await session.execute(
                update(
                    Products
                )
                .where(Products.id == product_id)
                .values(product_count=Products.product_count + 1)
            )
            await session.commit()
        else:
            query = (
                update(Cart)
                .where(
                    Cart.user_id == user_id,
                    Cart.product_name == exist_product.product_name
                )
                .values(product_quantity=Cart.product_quantity - 1)
            )
            product_query = (
                update(Products)
                .where(Products.id == product_id)
                .values(product_count=Products.product_count + 1)
            )

            await session.execute(query)
            await session.execute(product_query)
            await session.commit()

    async def get_cart(self, user_id: int) -> list[Cart] | None:
        async with self.db_session as session:
            cart: list[Cart] = (await session.execute(select(Cart).where(Cart.user_id == user_id))).scalars().all()
            return cart
