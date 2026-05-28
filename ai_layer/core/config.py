import os
from pydantic_settings import BaseSettings

class AISettings(BaseSettings):
    # LLM Providers
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    
    # Default Routing
    DEFAULT_COMPLEX_MODEL: str = "openai/gpt-4o"
    DEFAULT_FAST_MODEL: str = "openai/gpt-3.5-turbo"
    DEFAULT_CLAUDE_MODEL: str = "anthropic/claude-3-5-sonnet-20240620"
    
    # Memory Systems
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
    
    POSTGRES_URI: str = os.getenv(
        "SQLALCHEMY_DATABASE_URI", 
        "postgresql+asyncpg://postgres:postgres@localhost/mir_ecosystem"
    )

    class Config:
        env_file = ".env"

settings = AISettings()
