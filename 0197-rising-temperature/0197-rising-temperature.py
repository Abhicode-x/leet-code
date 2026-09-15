import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["date"] = pd.to_datetime(weather["recordDate"])

    weather = weather.sort_values("date").reset_index(drop=True)

    weather["prev_temp"] = weather["temperature"].shift(1)
    weather["prev_date"] = weather["date"].shift(1)

    result = weather[
        (weather["temperature"] > weather["prev_temp"]) &
        ((weather["date"] - weather["prev_date"]).dt.days == 1)
    ]

    return result[["id"]]