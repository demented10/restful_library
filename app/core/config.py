import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Library API"
    PROJECT_VERSION: str = "0.1.0"
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://library_user:library_password@localhost:5432/library_db"
    )
    
    # API
    API_V1_PREFIX: str = "/api"
    
    # Application
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()