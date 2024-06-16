from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependency import get_cart_service, get_request_user_id
from app.cart.schema import CartSchema
from app.cart.service import CartService
from app.exception import ProductOutOfStockException, ProductNotFoundException, UpdateMethodNotFoundException

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


@router.get(
    '/update_product',
    response_model=list[CartSchema],
    description='Increment or decrement quantity, availability methods: plus and minus'
)
async def update_product_quantity(
        product_id: int,
        method: str,
        cart_service: Annotated[CartService, Depends(get_cart_service)],
        user_id: int = Depends(get_request_user_id)
):
    try:
        return await cart_service.update_product_quantity(
            user_id=user_id,
            product_id=product_id,
            method=method
        )
    except ProductOutOfStockException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.detail
        )
    except ProductNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    except UpdateMethodNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.detail
        )
