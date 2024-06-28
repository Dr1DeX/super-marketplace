FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry
RUN poetry install

COPY ../.. .

ENV PYTHONPATH="${PYTHONPATH}:/app"

CMD ["poetry", "run", "python", "workers/orders/orders_rabbitmq_worker.py"]
