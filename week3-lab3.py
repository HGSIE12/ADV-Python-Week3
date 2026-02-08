import pandas as pd
import time

chunks = pd.read_csv("day13_large_users (1).csv", chunksize=20)

total_rows = 0
sum_income = 0.0

start = time.perf_counter()

for chunk in chunks:
    clean_income = chunk.dropna(subset=["income"])

    total_rows += len(clean_income)
    sum_income += clean_income["income"].sum()

    chunk["income2"] = chunk["income"].apply(
        lambda x: x / sum_income if pd.notna(x) else x
    )

    clean_age = chunk.dropna(subset=["age"])
    print(clean_age)


elapsed = time.perf_counter() - start

print(f"\nTotal cleaned rows: {total_rows}")
print(f"Total income sum: {sum_income}")
print(f"Time taken: {elapsed:.3f} seconds")
