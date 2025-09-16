class AppConfig:
    """Application settings."""
    
    test_data_file: str = "test_data.csv"


class Config:
    """Main configuration class."""
    
    app_config = AppConfig()


config = Config()
