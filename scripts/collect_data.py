import statsapi
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parent.parent

data_batting = statsapi.get("stats", {
    "stats":      "season",
    "group":      "hitting",
    "season":     2025,
    "playerPool": "ALL",     
    "limit":      300,
})

b_rows = []
for entry in data_batting["stats"][0]["splits"]:
    if entry["stat"]["atBats"]>=50:
        row = entry["stat"].copy()
        row["name"] = entry["player"]["fullName"]
        row["team"] = entry["team"]["name"]
        b_rows.append(row)

df_b = pd.DataFrame(b_rows)
df_b.to_csv(root / "data/raw/batting_raw.csv", index=False)
print(df_b.shape)   
print(df_b.head())

data_pitching = statsapi.get("stats", {
    "stats":      "season",
    "group":      "pitching",
    "season":     2025,
    "playerPool": "ALL",     
    "limit":      300,
})

p_rows = []

for entry in data_pitching["stats"][0]["splits"]:
    if float(entry["stat"]["inningsPitched"]) >= 10.0:
        row = entry["stat"].copy()
        row["name"] = entry["player"]["fullName"]
        row["team"] = entry["team"]["name"]
        p_rows.append(row)

df_p = pd.DataFrame(p_rows)
df_p.to_csv(root / "data/raw/pitching_raw.csv", index=False)

print(df_p.shape)   
print(df_p.head())


data_standings = statsapi.standings_data("103,104",season=2025)

s_rows = []

for div_id,div_data in data_standings.items():
    division_name = div_data["div_name"]
    for team in div_data["teams"]:
        w = int(team['w'])
        l = int(team['l'])
        pct = round(w / (w + l), 3) if (w + l) > 0 else 0.0
        s_rows.append(
            {
                "Division": division_name,
                "Team": team["name"],
                "W": team["w"],
                "L": team["l"],
                "GB": team["gb"],
                "Win%": pct,
            }
        )

df_s = pd.DataFrame(s_rows)
df_s.to_csv(root / "data/raw/standings_raw.csv", index=False)

print(df_s.shape)   
print(df_s.head())

