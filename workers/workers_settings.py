from pydantic_settings import BaseSettings


class WorkersSettings(BaseSettings):
    RABBITMQ_DEFAULT_USER: str = 'guest'
    RABBITMQ_DEFAULT_PASS: str = 'guest'
    RABBIT_HOSTNAME: str = 'localhost'

    @property
    def rabbit_url(self):
        return f'amqp://{self.RABBITMQ_DEFAULT_USER}:{self.RABBITMQ_DEFAULT_PASS}@{self.RABBIT_HOSTNAME}:5672/'
