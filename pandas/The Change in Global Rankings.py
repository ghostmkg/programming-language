import pandas as pd

def rank_change(comp1: pd.DataFrame, comp2: pd.DataFrame) -> pd.DataFrame:
    comp1['rank1'] = comp1['score'].rank(ascending=False, method='dense')
    comp2['rank2'] = comp2['score'].rank(ascending=False, method='dense')

    merged = pd.merge(comp1[['player_id', 'rank1']], comp2[['player_id', 'rank2']], on='player_id')
    merged['rank_diff'] = merged['rank1'] - merged['rank2']
    return merged[['player_id', 'rank_diff']]
