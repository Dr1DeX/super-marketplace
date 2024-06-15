from fastapi import Depends, security, Security, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.cart.checkout.repository import CheckoutRepository
from app.cart.checkout.service import CheckoutService
from app.cart.repository import CartRepository
from app.cart.service import CartService
from app.exception import TokenExpireExtension
from app.infrastructure.database import get_db_session
from app.infrastructure.database.accessor import AsyncSessionFactory
from app.orders.repository import OrdersRepository
from app.orders.service import OrdersService
from app.products.repository import ProductRepository
from app.products.service import ProductService
from app.sales.repository import SalesRepository
from app.sales.service import SalesService
from app.settings import Settings
from app.users.auth.service import AuthService
from app.users.user_profile.repository import UserRepository
from app.users.user_profile.service import UserService


async def get_products_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> ProductRepository:
    return ProductRepository(db_session=db_session)


async def get_product_service(
        product_repository: ProductRepository = Depends(get_products_repository)
) -> ProductService:
    return ProductService(product_repository=product_repository)


async def get_user_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> UserRepository:
    return UserRepository(db_session=db_session)


async def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
        settings=Settings()
    )


async def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository),
        auth_service: AuthService = Depends(get_auth_service)
) -> UserService:
    return UserService(
        user_repository=user_repository,
        auth_service=auth_service
    )


reusable_oath2 = security.HTTPBearer()


async def get_request_user_id(
        auth_service: AuthService = Depends(get_auth_service),
        token: security.http.HTTPAuthorizationCredentials = Security(reusable_oath2)
) -> int:
    try:
        user_id = auth_service.get_user_id_from_access_token(token=token.credentials)
    except TokenExpireExtension as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )
    return user_id


async def get_cart_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> CartRepository:
    return CartRepository(db_session=db_session)


async def get_cart_service(
        cart_repository: CartRepository = Depends(get_cart_repository)
) -> CartService:
    return CartService(cart_repository=cart_repository)


async def get_checkout_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> CheckoutRepository:
    return CheckoutRepository(db_session=db_session)


async def get_checkout_service(
        checkout_repository: CheckoutRepository = Depends(get_checkout_repository)
) -> CheckoutService:
    return CheckoutService(checkout_repository=checkout_repository)


async def get_sales_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> SalesRepository:
    return SalesRepository(db_session=db_session)


async def get_orders_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> OrdersRepository:
    return OrdersRepository(db_session=db_session)


async def get_orders_service(
        orders_repository: OrdersRepository = Depends(get_orders_repository)
) -> OrdersService:
    return OrdersService(orders_repository=orders_repository)
