import pytest
import os
import json
from unittest.mock import patch
from projectHackworth2026.code import extract

@patch('projectHackworth2026.code.extract.requests.get')
def test_fetch_superhero_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"name": "Spider-Man", "biography": {"publisher": "Marvel Comics"}}]

    data = extract.fetch_superhero_data()
    assert isinstance(data, list)
    assert data[0]['name'] == "Spider-Man"
    assert os.path.exists(extract.RAW_DATA_PATH)
    with open(extract.RAW_DATA_PATH) as f:
        saved = json.load(f)
        assert isinstance(saved, list)