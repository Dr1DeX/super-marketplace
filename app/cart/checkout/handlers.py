from typing import Annotated

from fastapi import APIRouter, status, Depends

from app.dependency import get_checkout_service, get_request_user_id
from app.cart.checkout.schema import UserContactInfoSchema, UserCreateContactInfoSchema
from app.cart.checkout.service import CheckoutService

router = APIRouter(prefix='/checkout', tags=['checkout'])


@router.post(
    '/create-order',
    response_model=UserContactInfoSchema
)
async def create_order(
        checkout_service: Annotated[CheckoutService, Depends(get_checkout_service)],
        body: UserCreateContactInfoSchema,
        product_id: int,
        user_id: int = Depends(get_request_user_id)
):
    order = await checkout_service.create_orders(body=body, user_id=user_id, product_id=product_id)
    return order
