import json 
import pandas as pd
import os 

CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')
RAW_DATA_PATH = os.path.join(CACHE_DIR, 'raw_data.json')
TRANSFORMED_DATA_PATH = os.path.join(CACHE_DIR, 'transformed_data.csv')

def load_raw_data():
    with open(RAW_DATA_PATH, 'r') as f:
        return json.load(f)

def transform_data():
    raw_data = load_raw_data()
    df = pd.json_normalize(raw_data)

    df = df[['name', 'slug', 'biography.publisher', 'biography.alignment', 'appearance.gender',
             'appearance.race', 'powerstats.intelligence', 'powerstats.strength',
             'powerstats.speed', 'powerstats.durability', 'powerstats.power',
             'powerstats.combat']]

    df.columns = [col.split('.')[-1] for col in df.columns]  # simplify column names
    df = df[df['publisher'].isin(['Marvel Comics', 'DC Comics'])]  # filter only Marvel/DC
    df = df.dropna(subset=['intelligence', 'strength', 'speed', 'durability', 'power', 'combat'])

    df.to_csv(TRANSFORMED_DATA_PATH, index=False)
    return df

if __name__ == '__main__':
    print(f"Transforming raw data and saving to {TRANSFORMED_DATA_PATH}...")
    transform_data()
    print("Done.")