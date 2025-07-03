import pandas as pd


def find_outliers_iqr(
    df: pd.DataFrame, col_name: str, threshold: float = 1.5
) -> pd.DataFrame:
    Q1 = df[col_name].quantile(0.25)
    Q3 = df[col_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    return df[(df[col_name] < lower_bound) | (df[col_name] > upper_bound)]
