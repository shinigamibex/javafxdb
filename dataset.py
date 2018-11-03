import pandas as pd

def load_dataset(filename = 'data/games.csv'):
    df = pd.read_csv(filename)
    return df[['winner', 'moves']]
