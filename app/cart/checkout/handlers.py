from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependency import get_checkout_service, get_request_user_id
from app.cart.checkout.schema import CheckoutSchema, CheckoutCreateSchema
from app.cart.checkout.service import CheckoutService

router = APIRouter(prefix='/checkout', tags=['checkout'])


@router.post(
    '/create-order',
    response_model=list[CheckoutSchema]
)
async def create_order(
        checkout_service: Annotated[CheckoutService, Depends(get_checkout_service)],
        body: CheckoutCreateSchema,
        user_id: int = Depends(get_request_user_id)
):
    return await checkout_service.create_order(body=body, user_id=user_id)
