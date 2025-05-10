import pandas as pd
from code import load

def test_load_data():
    df = load.load_data()
    assert not df.empty
    assert 'publisher' in df.columns

def test_get_publisher_counts():
    df = pd.DataFrame({'publisher': ['Marvel Comics', 'DC Comics', 'Marvel Comics']})
    result = load.get_publisher_counts(df)
    assert result['Marvel Comics'] == 2
    assert result['DC Comics'] == 1

def test_get_average_stats():
    df = pd.DataFrame({
        'publisher': ['Marvel Comics', 'Marvel Comics', 'DC Comics'],
        'intelligence': [90, 80, 70],
        'strength': [80, 85, 75],
        'speed': [70, 65, 60],
        'durability': [60, 70, 50],
        'power': [85, 80, 70],
        'combat': [95, 90, 85],
    })
    result = load.get_average_stats(df)
    assert result.loc['Marvel Comics', 'intelligence'] == 85

def test_get_gender_distribution():
    df = pd.DataFrame({
        'publisher': ['Marvel Comics', 'Marvel Comics', 'DC Comics'],
        'gender': ['Male', 'Female', 'Male']
    })
    result = load.get_gender_distribution(df)
    assert result.loc['Marvel Comics', 'Male'] == 1
    assert result.loc['Marvel Comics', 'Female'] == 1
