import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    # Get users who are not banned
    valid_users = users[users["banned"] == "No"]["users_id"]

    # Keep trips where both client and driver are not banned
    df = trips[
        trips["client_id"].isin(valid_users) &
        trips["driver_id"].isin(valid_users)
    ].copy()

    # Keep only required dates
    df = df[
        (df["request_at"] >= "2013-10-01") &
        (df["request_at"] <= "2013-10-03")
    ]

    # Check whether trip was cancelled
    df["cancelled"] = (
        df["status"].isin([
            "cancelled_by_client",
            "cancelled_by_driver"
        ])
    )

    # Calculate cancellation rate
    result = df.groupby("request_at").agg(
        cancelled=("cancelled", "sum"),
        total=("cancelled", "count")
    ).reset_index()

    result["Cancellation Rate"] = (
        result["cancelled"] / result["total"]
    ).round(2)

    return result[
        ["request_at", "Cancellation Rate"]
    ].rename(
        columns={"request_at": "Day"}
    )