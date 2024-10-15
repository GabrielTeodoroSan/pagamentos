from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf8'
    )
    CLIENT_ID: str   
    SECRET_KEY: str   
    ACCESS_TOKEN: str   
    ACCESS_TOKE_URL: str     
    BASE_USER: str      
    