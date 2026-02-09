import pandas as pd

data = pd.read_csv("day15_real_dataset_large.csv")
df = pd.DataFrame(data)

def clean_data_project(df_raw):
    df = df_raw.copy()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["income"] = pd.to_numeric(df["income"],
    errors="coerce")
    df["signup_time"] = pd.to_datetime(df["signup_time"],
    errors="coerce")

    df["age_missing"] = df["age"].isna().astype(int)
    df["age"] = df["age"].fillna(df["age"].median())
    df["income_missing"] = df["income"].isna().astype(int)
    df["income"] = df["income"].fillna(df["income"].median())

    df["income"] = df["income"].clip(upper=df["income"].quantile(0.99))

    df["city"] = df["city"].str.strip().str.lower()
    df["signup_time"] = df["signup_time"].dt.tz_localize("UTC")
    return df

cleaning_decisions = {
    "age": "I converted the age to a whole number,"
           " removed any numbers that had no value,"
           " and changed them to the average value.",

    "income": "I converted the input to an integer,"
        " removed any numbers with no value and changed them to the mean value,"
        " and then removed the outliers.",

    "signup_time": "I converted the login time to real time,"
                   " then converted it to UTC.",

    "city" : "I removed all the capital letters,"
             " and also removed the spaces."

}

print(clean_data_project(df))
df_clean = clean_data_project(df)
print("info\n",df_clean.info())
print("Describe\n",df_clean[["age", "income"]].describe())
print("value count\n",df_clean["city"].value_counts().head())
print("sign time",df_clean["signup_time"].dt.tz)
