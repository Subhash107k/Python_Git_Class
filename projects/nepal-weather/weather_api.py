"""
weather_api.py

Handles interactions with the OpenWeatherMap REST API.
"""
import requests
import config

# OpenWeatherMap API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(lat, lon):
    """
    Fetches current weather data for the given coordinates.
    Raises exceptions if the request fails.
    """
    try:
        api_key = config.get_api_key()
    except ValueError as e:
        raise Exception(f"Configuration Error: {e}")

    # Set up query parameters
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric" # Use metric units for Celsius
    }

    try:
        # Make the HTTP GET request
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse and return the JSON data
        return response.json()
        
    except requests.exceptions.ConnectionError:
        raise Exception("Network Error: Unable to connect to the weather service.\nPlease check your internet connection and try again.")
    except requests.exceptions.Timeout:
        raise Exception("Timeout Error: The weather API took too long to respond.")
    except requests.exceptions.HTTPError as e:
        # Provide more specific error messages based on status codes
        if response.status_code == 401:
            raise Exception("Authentication Error: Invalid API key. Please check your .env file.")
        elif response.status_code == 404:
            raise Exception("Not Found: The specified location could not be found.")
        elif response.status_code == 429:
            raise Exception("Rate Limit Exceeded: Too many requests to the weather API.")
        else:
            raise Exception(f"HTTP Error: An error occurred with the API request ({response.status_code}).")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request Error: An unexpected error occurred: {e}")
    except ValueError:
        raise Exception("Data Error: Received invalid JSON data from the API.")
