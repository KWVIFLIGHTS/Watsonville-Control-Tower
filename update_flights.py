import json
import datetime
import requests
from bs4 import BeautifulSoup

def fetch_live_flights():
    url = "https://www.airnav.com/airport/KWVI"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    current_time = datetime.datetime.now().strftime("%H:%M")
    
    # Initialize empty data structure
    data = {
        "last_updated": current_time,
        "arrivals": [],
        "departures": []
    }

    try:
        # 1. Fetch the website
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # 2. Find all tables on the AirNav page
        tables = soup.find_all('table')
        
        for table in tables:
            rows = table.find_all('tr')
            if len(rows) < 2:
                continue
                
            # 3. Look for the specific Flight Activity table
            header_text = rows[0].get_text().lower()
            if 'flight' in header_text and 'aircraft' in header_text:
                
                # 4. Extract data from each row
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) >= 5:
                        ident = cols[0].get_text(strip=True)
                        ac_type = cols[1].get_text(strip=True)
                        origin = cols[2].get_text(strip=True)
                        dest = cols[3].get_text(strip=True)
                        time_str = cols[4].get_text(strip=True) # Usually Departure/Arrival Time
                        
                        # 5. Sort into Arrivals or Departures
                        if 'WVI' in origin or 'Watsonville' in origin:
                            data["departures"].append({
                                "ident": ident, "type": ac_type, "destination": dest, "time": time_str
                            })
                        elif 'WVI' in dest or 'Watsonville' in dest:
                            data["arrivals"].append({
