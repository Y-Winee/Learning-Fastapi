from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from ..config import database_settings

async_engine = create_async_engine(
    url=database_settings.POSTGRES_URL,
    echo=True
)


async def create_db_tables():
    async with async_engine.begin() as conn:
        from .model import Shipment
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        yield session