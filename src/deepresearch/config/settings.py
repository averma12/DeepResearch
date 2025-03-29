"""
Application settings configuration.
"""

import os
from typing import Optional

from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    
    # API Keys
    OPENAI_API_KEY: Optional[str] = None
    SEARCH_API_KEY: Optional[str] = None
    
    # Model Settings
    DEFAULT_MODEL: str = "gpt-4"
    MAX_TOKENS: int = 2000
    
    # Research Settings
    MAX_SEARCH_RESULTS: int = 5
    MAX_MEMORY_FACTS: int = 100
    
    # Logging Settings
    LOG_LEVEL: str = "INFO"
    LOG_FILE: Optional[str] = None
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True

def get_settings() -> Settings:
    """
    Get application settings.
    
    Returns:
        Settings instance
    """
    return Settings() 