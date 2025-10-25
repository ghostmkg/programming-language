import pandas as pd

def order_columns_independently(df: pd.DataFrame) -> pd.DataFrame:
    df['col1'] = sorted(df['col1'])
    df['col2'] = sorted(df['col2'])
    return df
