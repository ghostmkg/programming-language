import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
    return df.sort_values('rating', ascending=False)
