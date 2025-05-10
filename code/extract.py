import requests
import json
import os

CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')
RAW_DATA_PATH = os.path.join(CACHE_DIR, 'raw_data.json')

def fetch_superhero_data(url='https://akabab.github.io/superhero-api/api/all.json'):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(RAW_DATA_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    return data

if __name__ == '__main__':
    print(f"Fetching and saving superhero data to {RAW_DATA_PATH}...")
    fetch_superhero_data()
    print("Done.")