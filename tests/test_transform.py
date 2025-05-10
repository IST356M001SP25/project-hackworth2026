import json
import os
import pandas as pd
from projectHackworth2026.code import transform

def test_transform_data():
    # Create dummy raw_data.json
    dummy_data = [{
        "name": "Batman",
        "slug": "batman",
        "biography": {"publisher": "DC Comics", "alignment": "good"},
        "appearance": {"gender": "Male", "race": "Human"},
        "powerstats": {
            "intelligence": 100, "strength": 26, "speed": 27,
            "durability": 50, "power": 47, "combat": 100
        }
    }]
    os.makedirs(os.path.dirname(transform.RAW_DATA_PATH), exist_ok=True)
    with open(transform.RAW_DATA_PATH, 'w') as f:
        json.dump(dummy_data, f)

    df = transform.transform_data()
    assert not df.empty
    assert 'name' in df.columns
    assert df['publisher'].iloc[0] == "DC Comics"
    assert os.path.exists(transform.TRANSFORMED_DATA_PATH)