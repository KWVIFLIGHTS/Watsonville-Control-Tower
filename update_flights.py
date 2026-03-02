import json
import datetime

current_time = datetime.datetime.now().strftime("%H:%M")

data = {
    "last_updated": current_time,
    "arrivals": [
        # Make sure these 4 fields exist for each flight
        {"ident": "N931E", "type": "BE58", "origin": "KWVI", "time": "18:45"},
        {"ident": "N911MS", "type": "C172", "origin": "KRHV", "time": "18:30"}
    ],
    "departures": [
        {"ident": "N704NQ", "type": "P28A", "destination": "KOAR", "time": "18:55"},
        {"ident": "N180ZR", "type": "C182", "destination": "KPAO", "time": "18:50"}
    ]
}

# SAVE AS Flights.json (Capital F) to match the HTML fetch
with open('Flights.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Updated Flights.json at {current_time}")
