"""
utils.py

Provides utility functions for formatting the CLI output, handling user input,
and other common tasks.
"""
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Prints a formatted header."""
    print("=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)
    print()

def get_user_choice(prompt, valid_choices):
    """
    Prompts the user for a choice until a valid one is provided.
    """
    while True:
        try:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid choice. Please select an option from {', '.join(valid_choices)}.\n")
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nExiting program...")
            exit(0)

def display_weather(district, province, weather_data):
    """
    Formats and prints the weather data.
    """
    print()
    print_header("CURRENT WEATHER")
    
    print(f"District       : {district}")
    if province:
        print(f"Province       : {province}")
    print()
    
    # Extract data from the JSON response
    temp = weather_data.get('main', {}).get('temp', 'N/A')
    feels_like = weather_data.get('main', {}).get('feels_like', 'N/A')
    humidity = weather_data.get('main', {}).get('humidity', 'N/A')
    pressure = weather_data.get('main', {}).get('pressure', 'N/A')
    
    # Weather conditions (usually a list of dictionaries)
    weather_list = weather_data.get('weather', [])
    condition = weather_list[0].get('description', 'N/A').title() if weather_list else 'N/A'
    
    wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
    clouds = weather_data.get('clouds', {}).get('all', 'N/A')
    visibility = weather_data.get('visibility', 'N/A')
    if visibility != 'N/A':
        visibility = f"{visibility / 1000:.1f} km"

    print(f"Temperature    : {temp}°C")
    print(f"Feels Like     : {feels_like}°C")
    print(f"Condition      : {condition}")
    print(f"Humidity       : {humidity}%")
    print(f"Wind Speed     : {wind_speed} m/s")
    print(f"Pressure       : {pressure} hPa")
    print(f"Cloud Cover    : {clouds}%")
    print(f"Visibility     : {visibility}")
    
    print("\n" + "=" * 40)
