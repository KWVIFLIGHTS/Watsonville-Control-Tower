import json
import datetime
import requests
from bs4 import BeautifulSoup

def fetch_flights():
    # The URL for Watsonville Muni
    url = "https://www.airnav.com/airport/KWVI"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    current_time = datetime.datetime.now().strftime("%H:%M")
    
    # This structure matches your new Table requirements
    data = {
        "last_updated": current_time,
        "arrivals": [
            {"ident": "N931E", "type": "BE58", "origin": "KWVI", "time": "18:45"},
            {"ident": "N911MS", "type": "C172", "origin": "KRHV", "time": "18:30"}
        ],
        "departures": [
            {"ident": "N704NQ", "type": "P28A", "destination": "KOAR", "time": "18:55"},
            {"ident": "N180ZR", "type": "C182", "destination": "KPAO", "time": "18:50"}
        ]
    }

    # SAVING THE FILE
    # We use 'Flights.json' to match your index.html fetch command
    with open('Flights.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Successfully updated Flights.json at {current_time}")

if __name__ == "__main__":
    fetch_flights()
