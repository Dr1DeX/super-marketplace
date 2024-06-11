from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependency import get_cart_service, get_request_user_id
from app.cart.schema import CartSchema, CartCreateSchema
from app.cart.service import CartService
from app.products.schema import ProductSchema

router = APIRouter(prefix='/cart', tags=['cart'])


@router.post(
    '/add',
    response_model=list[CartSchema]
)
async def add_cart(
        cart_item: CartCreateSchema,
        cart_service: Annotated[CartService, Depends(get_cart_service)],
        user_id: int = Depends(get_request_user_id)
):
    return await cart_service.add_cart(cart_item=cart_item, user_id=user_id)


@router.get(
    '',
    response_model=list[ProductSchema]
)
async def get_cart_with_product_info(
        cart_service: Annotated[CartService, Depends(get_cart_service)],
        user_id: int = Depends(get_request_user_id)
):
    return await cart_service.get_cart(user_id=user_id)
