import multiprocessing

from pydantic_settings import BaseSettings


class UvicornSettings(BaseSettings):
    host: str = "localhost"
    port: int = 8000
    workers: int = multiprocessing.cpu_count()


class AppSettings(BaseSettings):
    uvicorn: UvicornSettings = UvicornSettings()


app_settings = AppSettings()
