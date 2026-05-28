import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

# In production, use pydantic BaseSettings
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI", 
    "postgresql+asyncpg://postgres:postgres@localhost/mir_ecosystem"
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=False,
    future=True,
    pool_size=20,
    max_overflow=10
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db() -> AsyncSession: # type: ignore
    """
    Dependency for FastAPI endpoints to get an async db session.
    """
    async with AsyncSessionLocal() as session:
        yield session
