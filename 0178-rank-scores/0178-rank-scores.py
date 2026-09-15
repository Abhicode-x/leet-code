import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(
        method="dense",
        ascending=False
    )

    scores["rank"] = scores["rank"].astype(int)

    return scores[["score", "rank"]].sort_values(
        by=["score", "rank"],
        ascending=[False, True]
    )