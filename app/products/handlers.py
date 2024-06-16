from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from app.cart.schema import CartSchema
from app.cart.service import CartService
from app.dependency import get_product_service, get_cart_service, get_request_user_id
from app.exception import ProductNotFoundException, ProductByCategoryNameException, ProductOutOfStockException
from app.products.schema import ProductSchema, CategorySchema
from app.products.service import ProductService

router = APIRouter(prefix='/product', tags=['product'])


@router.get(
    '/all',
    response_model=list[ProductSchema]
)
async def get_products(
        product_service: Annotated[ProductService, Depends(get_product_service)]
):
    return await product_service.get_products()


@router.get(
    '/{product_id}',
    response_model=ProductSchema
)
async def get_product(
        product_id: int,
        product_service: Annotated[ProductService, Depends(get_product_service)]
):
    try:
        return await product_service.get_product(product_id=product_id)
    except ProductNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )


@router.get(
    '/categories/all',
    response_model=list[CategorySchema]
)
async def get_categories(
        product_service: Annotated[ProductService, Depends(get_product_service)]
):
    return await product_service.get_categories()


@router.get(
    '/categories/{category_name}',
    response_model=list[CategorySchema]
)
async def get_products_by_category_name(
        category_name: str,
        product_service: Annotated[ProductService, Depends(get_product_service)]
):
    try:
        return await product_service.get_products_by_category_name(category_name=category_name)
    except ProductByCategoryNameException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )


@router.post(
    '/add_product/{product_id}',
    response_model=list[CartSchema]
)
async def add_product(
        product_id: int,
        cart_service: Annotated[CartService, Depends(get_cart_service)],
        product_service: Annotated[ProductService, Depends(get_product_service)],
        user_id: int = Depends(get_request_user_id)
):
    try:
        product = await product_service.add_product(product_id=product_id)
    except ProductNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    except ProductOutOfStockException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.detail
        )
    return await cart_service.add_cart(body=product, user_id=user_id)
