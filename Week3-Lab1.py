import pandas as pd
import numpy as np

df = pd.read_csv("/mnt/data/day11_income.csv")

def winsorize_series(s, lower_q, upper_q):
    lower = s.quantile(lower_q)
    upper = s.quantile(upper_q)
    return s.clip(lower, upper)

def remove_upper_tail(s, upper_q):
    upper = s.quantile(upper_q)
    return s[s <= upper]

df["winsorized"] = winsorize_series(df["income"], 0.01, 0.99)
df["removed"] = remove_upper_tail(df["income"], 0.99)

print("Original:")
print(df["income"].describe())

print("\nWinsorized:")
print(df["winsorized"].describe())

print("\nRemoved:")
print(df["removed"].describe())
