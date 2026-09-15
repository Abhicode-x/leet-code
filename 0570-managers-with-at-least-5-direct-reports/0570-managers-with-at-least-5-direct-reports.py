import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee["managerId"].value_counts()
    
    managers = managers[managers >= 5].index
    
    return employee[
        employee["id"].isin(managers)
    ][["name"]]