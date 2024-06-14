from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependency import get_cart_service, get_request_user_id
from app.cart.schema import CartSchema
from app.cart.service import CartService

router = APIRouter(prefix='/cart', tags=['cart'])


@router.get(
    '',
    response_model=list[CartSchema]
)
async def get_cart_user(
        cart_service: Annotated[CartService, Depends(get_cart_service)],
        user_id: int = Depends(get_request_user_id)
):
    return await cart_service.get_cart(user_id=user_id)
