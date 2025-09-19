from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Shams — Audio to Light AI"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()