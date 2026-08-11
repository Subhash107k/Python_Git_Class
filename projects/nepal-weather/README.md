# Nepal District Weather Fetcher

A simple Python command-line application for checking current weather information across districts of Nepal.

The application allows users to browse districts, search for a district by name, and retrieve current weather information from an external weather API.

## Features

* 🇳🇵 Browse Nepal districts
* 🔎 Search districts by name
* 🌤️ Fetch current weather information
* 📍 Uses district coordinates for weather requests
* 🔐 Loads API credentials from environment variables
* 💻 Interactive command-line interface

## Project Structure

```text
nepal-weather-fetcher/
├── main.py              # Application entry point and menu
├── weather_api.py       # Weather API requests and response handling
├── districts.py         # District names and coordinates
├── config.py            # Environment configuration
├── utils.py             # Formatting and input helpers
├── .env.example         # Environment variable template
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Requirements

* Python 3.10+
* Weather API key
* Internet connection

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```bash
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Add your weather API key to `.env`.

> **Never commit `.env` to Git.** Make sure it is included in `.gitignore`.

### 4. Run the Application

```bash
python main.py
```

## How It Works

```text
User
  ↓
CLI Menu
  ↓
Select / Search District
  ↓
District Coordinates
  ↓
Weather API
  ↓
Current Weather
  ↓
Formatted Terminal Output
```

## Example

```text
====================================
     Nepal District Weather
====================================

1. Browse Districts
2. Search District
3. Exit

Enter your choice: 2

Enter district name: Kathmandu

Weather for Kathmandu
Temperature : 24°C
Condition   : Partly Cloudy
Humidity    : 68%
```

*The displayed values depend on the current weather API response.*

## Technologies

* Python
* REST API
* JSON
* `requests`
* Environment variables
* Virtual environments
* Git & GitHub

## Learning Outcomes

This project demonstrates practical use of:

* Python modules and packages
* Functions
* File and configuration management
* API integration
* JSON response processing
* Exception handling
* Environment variables
* Git/GitHub project management
* CLI application design

## Future Improvements

* Add a free weather API option that does not require an API key.
* Add weather forecasts.
* Add temperature unit selection.
* Improve district search and filtering.
* Add colored terminal output.
* Add API error and offline handling.
* Add automated tests.

## License

This project is created for learning and portfolio purposes.
