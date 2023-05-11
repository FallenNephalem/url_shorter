from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = 'env.properties'
    DATABASE_URL: str
    DOMAIN: str = 'localhost'


@lru_cache
def get_settings():
    return Settings()
