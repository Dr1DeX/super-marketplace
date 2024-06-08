import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from app.settings import Settings
from utils.autoimport import get_all_models

from app.infrastructure.database import Base


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


get_all_models()

target_metadata = Base.metadata


def run_migrations_offline(connection):
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        compare_type=True,
        dialect_opts={'paramstyle': 'named'},
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True,
        version_table_schema=target_metadata.schema
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_async_engine(Settings().db_url, future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations_offline)


asyncio.run(run_migrations_online())
