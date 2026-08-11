# Nepal District Weather Fetcher

This project is a small command-line weather app for Nepal. It lets you browse districts, search by name, and view current weather information from an external weather service.

## Project files

- [main.py](main.py) — the app entry point and menu flow
- [weather_api.py](weather_api.py) — API requests and response parsing
- [districts.py](districts.py) — district names and coordinates
- [config.py](config.py) — environment variable loading
- [utils.py](utils.py) — formatting and input helpers
- [.env.example](.env.example) — example environment configuration
- [requirements.txt](requirements.txt) — project dependencies

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy [.env.example](.env.example) to `.env` and add your weather API key.
4. Run the app:
   ```bash
   python main.py
   ```

## Notes

- The project uses environment variables for the API key.
- The app is interactive and works from the terminal.
- A good next step is to replace the current weather service with a free alternative if you want to avoid API-key setup.
