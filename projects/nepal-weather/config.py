"""
config.py

Handles environment variable loading and configuration for the application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Attempt to get the API key from the environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_api_key():
    """
    Returns the OpenWeatherMap API key.
    Raises ValueError if the key is missing or empty.
    """
    if not API_KEY or API_KEY == "your_api_key_here":
        raise ValueError(
            "API Key missing. Please configure OPENWEATHER_API_KEY in your .env file."
        )
    return API_KEY
