from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """Application settings."""
    
    test_data_file: str = "test_data.csv"
    
    class Config:
        env_file = ".env"


class Config:
    """Main configuration class."""
    
    app_config = AppConfig()


config = Config()
