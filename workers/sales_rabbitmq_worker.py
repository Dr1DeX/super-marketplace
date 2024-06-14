import aio_pika
import asyncio
import json

from app.settings import Settings

settings = Settings()


async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        order_data = json.loads(message.body)
        print(f'Received order data: {order_data}')


async def main():
    connection = await aio_pika.connect_robust(settings.rabbit_url)
    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange(name='user_info', type=aio_pika.ExchangeType.DIRECT)

        queue = await channel.declare_queue('user_info_queue', durable=True)
        await queue.bind(exchange=exchange, routing_key='sales')

        await queue.consume(on_message)

if __name__ == '__main__':
    print('[x] Stargazer worker active')
    asyncio.run(main())
