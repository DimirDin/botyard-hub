from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    owner_chat_id: int
    domain: str = "https://hub.botyard.site"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
