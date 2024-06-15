import aio_pika
import asyncio
import json

from workers.workers_dependency import get_orders_service
from workers.workers_settings import WorkersSettings


settings = WorkersSettings()
orders_service = get_orders_service()


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
        exchange = await channel.declare_exchange(name='orders_info', type=aio_pika.ExchangeType.DIRECT)

        queue = await channel.declare_queue('user_orders_info', durable=True)
        await queue.bind(exchange=exchange, routing_key='user_orders')

        order_data = await get_message_from_queue(queue)
        for data in order_data:
            await orders_service.create_orders(
                products=data['products'],
                order_id=data['order_id'],
                user_id=data['user_id'],
                status=data['status']
            )

if __name__ == '__main__':
    print('[x] Orders Stargazer worker active')
    asyncio.run(main())
