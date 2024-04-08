import os
import pandas as pd

def test_csv_creation():
    # Check if the CSV file is created
    assert os.path.exists('top_20_movies.csv')

def test_csv_data():
    # Check if the CSV file contains the correct data
    df = pd.read_csv('top_20_movies.csv')
    assert len(df) == 20  # Check if there are 20 rows
    assert list(df.columns) == ['Title', 'Year', 'Rating']  # Check if columns are correct

def test_avg_rating_calculation():
    # Check if the average rating is calculated correctly
    df = pd.read_csv('top_20_movies.csv')
    average_rating = df['Rating'].astype(float).mean()
    assert round(average_rating, 2) == 8.87  # Check if average rating is approximately 8.87
