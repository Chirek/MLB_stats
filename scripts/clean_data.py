import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parent.parent

batting_df = pd.read_csv(root / "data/raw/batting_raw.csv")
batting_df = batting_df[["name","team","gamesPlayed","atBats","avg","homeRuns","rbi","obp","slg","ops"]]
batting_df = batting_df.dropna(subset=["name"])
batting_df = batting_df.rename(columns={
    "name": "Name",
    "team": "Team",
    "gamesPlayed": "G",
    "atBats": "AB",
    "avg": "AVG",
    "homeRuns": "HR",
    "rbi": "RBI",
    "obp": "OBP",
    "slg": "SLG",
    "ops": "OPS"
})
batting_df = batting_df.fillna(0)
batting_df[["AVG","OBP","SLG","OPS"]] = batting_df[["AVG","OBP","SLG","OPS"]].round(3)
batting_df = batting_df.sort_values(["OPS"],ascending=False).reset_index(drop=True)
print(batting_df.head())
batting_df.to_csv(root / "data/processed/batting_clean.csv",index=False)

pitching_df = pd.read_csv(root / "data/raw/pitching_raw.csv")
pitching_df = pitching_df[["name","team","gamesPlayed","era","strikeOuts","baseOnBalls","whip","wins","losses"]]
pitching_df = pitching_df.dropna(subset=["name"])
pitching_df = pitching_df.rename(columns={
    "name": "Name",
    "team": "Team",
    "gamesPlayed": "G",
    "era": "ERA",
    "strikeOuts": "SO",
    "baseOnBalls": "BB",
    "whip": "WHIP",
    "wins": "W",
    "losses": "L"
})
pitching_df = pitching_df.fillna(0)
pitching_df[["ERA","WHIP"]] = pitching_df[["ERA","WHIP"]].round(2)
pitching_df = pitching_df.sort_values(["ERA"],ascending=True).reset_index(drop=True)
print(pitching_df.head())
pitching_df.to_csv(root / "data/processed/pitching_clean.csv",index=False)

standings_df = pd.read_csv(root / "data/raw/standings_raw.csv")
standings_df = standings_df[["Division","Team","W","L","Win%","GB"]]
standings_df = standings_df.rename(columns={
    "Win%": "W-L%"
})
standings_df = standings_df.sort_values(["Division","W-L%"],ascending=[True,False]).reset_index(drop=True)
print(standings_df.head())
standings_df.to_csv(root / "data/processed/standings_clean.csv",index=False)