from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from app.dependency import get_product_service
from app.exception import ProductNotFoundException, ProductByCategoryNameException
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
