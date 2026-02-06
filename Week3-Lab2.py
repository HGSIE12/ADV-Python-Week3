import pandas as pd

# Load data
df = pd.read_csv("day12_users.csv")

def standardize_city(df):
    df["city_clean"] = (
        df["city"]
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
    )

    city_map = {
        "ny": "new york",
        "newyork": "new york",
        "nyc": "new york",
        "la": "los angeles",
        "l a": "los angeles"
    }

    df["city_clean"] = df["city_clean"].replace(city_map)
    return df


def parse_and_localize(df):
    df["timestamp_clean"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
        infer_datetime_format=True
    ).dt.tz_localize("UTC")

    return df


df = standardize_city(df)
df = parse_and_localize(df)

print(df[["city", "city_clean", "timestamp", "timestamp_clean"]])
