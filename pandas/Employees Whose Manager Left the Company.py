import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    valid_ids = set(employees['employee_id'])
    df = employees[~employees['manager_id'].isin(valid_ids) & employees['manager_id'].notna()]
    return df[['employee_id']]
