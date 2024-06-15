import aio_pika
import asyncio
import json

from workers.utils.publisher_rq import send_to_message
from workers.workers_dependency import get_sales_service
from workers.workers_settings import WorkersSettings

settings = WorkersSettings()

sales_service = get_sales_service()


async def get_message_from_queue(queue):
    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                order_data = json.loads(message.body)
                print(f'Received order data: {order_data}')
                return order_data


async def main():
    connection = await aio_pika.connect_robust(settings.rabbit_url)
    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange(name='user_info', type=aio_pika.ExchangeType.DIRECT)

        queue = await channel.declare_queue('user_info_queue', durable=True)
        await queue.bind(exchange=exchange, routing_key='sales')

        order_data = await get_message_from_queue(queue)
        await sales_service.create_order(body=order_data)

        order_send = []

        for data in order_data:
            order_info = {
                'order_id': data['order_id'],
                'user_id': data['user_id'],
                'status': data['status'],
                'products': data['products']
            }
            order_send.append(order_info)

        await send_to_message(
            exchange_name='orders_info',
            routing_key='user_orders',
            message_body=order_send
        )

if __name__ == '__main__':
    print('[x] Sales Stargazer worker active')
    asyncio.run(main())
