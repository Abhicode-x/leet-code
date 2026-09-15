import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        bonus,
        on="empId",
        how="left"
    )

    result = df[
        (df["bonus"].isna()) |
        (df["bonus"] < 1000)
    ]

    return result[["name", "bonus"]]