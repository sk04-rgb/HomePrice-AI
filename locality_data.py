import pandas as pd
import json

files = [
    "data/mumbai.csv",
    "data/pune.csv",
    "data/bangalore.csv",
    "data/delhi.csv",
    "data/chennai.csv",
    "data/hyderabad.csv",
    "data/kolkata.csv",
    "data/ahmedabad.csv",
    "data/jaipur.csv",
    "data/chandigarh.csv"
]

city_localities = {}

for file in files:

    df = pd.read_csv(file)

    city = df["city"].iloc[0]

    city_localities[city] = sorted(
        df["locality"].unique().tolist()
    )

with open(
    "static/localities.json",
    "w"
) as f:

    json.dump(
        city_localities,
        f,
        indent=4
    )

print("localities.json created")
