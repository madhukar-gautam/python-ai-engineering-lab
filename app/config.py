from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Python AI Engineering Lab"
    environment: str = "development"
    log_level: str = "INFO"
    openai_api_key: str = ""
    openai_model: str = "gpt-5.6"
    llm_timeout_seconds: float = 30.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
