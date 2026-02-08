import pandas as pd

def clean_types(df):
    df = df.copy()
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df

def clean_missing(df):
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())
    return df

def handle_outliers(df):
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df[col] = df[col].clip(lower, upper)

    return df

def clean_strings_and_dates(df):
    df = df.copy()

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip().str.lower()

        try:
            df[col] = pd.to_datetime(df[col], errors="ignore")
        except:
            pass

    return df

def validate_cleaned(df):
    print("Missing values:\n", df.isna().sum())
    print("\nData types:\n", df.dtypes)
    print("\nBasic statistics:\n", df.describe())

def clean_data(df):
    df = clean_types(df)
    df = clean_missing(df)
    df = handle_outliers(df)
    df = clean_strings_and_dates(df)
    validate_cleaned(df)
    return df

data = pd.read_csv("day14_users_raw.csv")
df = pd.DataFrame(data)
print(clean_data(df))
