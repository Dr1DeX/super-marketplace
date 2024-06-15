from typing import Annotated

from fastapi import APIRouter, Depends

from app.orders.schema import OrdersSchema
from app.dependency import get_orders_service, get_request_user_id
from app.orders.service import OrdersService

router = APIRouter(prefix='/orders', tags=['orders'])


@router.get(
    '/my-order',
    response_model=list[OrdersSchema]
)
async def get_orders(
        orders_service: Annotated[OrdersService, Depends(get_orders_service)],
        user_id: int = Depends(get_request_user_id)
):
    return await orders_service.get_order(user_id=user_id)
