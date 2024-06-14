import aio_pika
import json
from app.settings import Settings

settings = Settings()


async def send_to_message(exchange_name: str, routing_key: str, message_body):
    connection = await aio_pika.connect_robust(settings.rabbit_url)
    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange(name=exchange_name, type=aio_pika.ExchangeType.DIRECT)
        message = aio_pika.Message(body=json.dumps(message_body).encode())
        print(f'Sendler to message for stargazer {message_body}')
        await exchange.publish(message=message, routing_key=routing_key)

