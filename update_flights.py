import json
import datetime

# Mock data generation for our test run!
current_time = datetime.datetime.now().strftime("%H:%M")

data = {
    "last_updated": current_time,
    "arrivals": [
        {"ident": "N704NQ", "origin": "KOAR"},
        {"ident": "N911MS", "origin": "KRHV"}
    ],
    "departures": [
        {"ident": "N6861F", "destination": "KHWD"},
        {"ident": "N180ZR", "destination": "KPAO"}
    ]
}

# Overwrite the flights.json file with the new data
with open('flights.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Successfully updated flights.json at {current_time}")
