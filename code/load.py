import pandas as pd
import os

CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')
TRANSFORMED_DATA_PATH = os.path.join(CACHE_DIR, 'transformed_data.csv')

def load_data():
    return pd.read_csv(TRANSFORMED_DATA_PATH)

def get_publisher_counts(df):
    return df['publisher'].value_counts()

def get_average_stats(df):
    stat_cols = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
    return df.groupby('publisher')[stat_cols].mean()


def get_gender_distribution(df):
    return df.groupby(['publisher', 'gender']).size().unstack(fill_value=0)