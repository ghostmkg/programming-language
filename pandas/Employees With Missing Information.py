import pandas as pd

def find_employees(employee: pd.DataFrame, salary: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, salary, on='employee_id', how='outer')
    missing = df[df.isna().any(axis=1)][['employee_id']]
    missing = missing.sort_values('employee_id')
    return missing
