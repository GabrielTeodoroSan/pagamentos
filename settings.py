from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf8'
    )
    CLIENT_ID: str
    SECRET_KEY: str
    ACCESS_TOKEN: str
    ACCESS_TOKEN_URL: str
    BASE_ORDER_URL: str
    API_BASE_URL: str
    BROKER_URL: str
    BACKEND_URL: str
