# ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer
# Author: Randall McKendry
# Run with: python3 explore.py

# start code for lab 13:

import pandas as pd

print("--- Exercise 1 ---")

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


print("--- Exercise 2 ---")

south = df[df["region"] == "South"]

print(len(south))
print(south.head())

print("--- Exercise 3 ---")

top_5 = df.sort_values("revenue", ascending=False).head(5)

print(top_5)


print("--- Exercise 4 ---")

big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print(len(big_south))
print(big_south.head())


print("--- Exercise 5 ---")

df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())
print(df["per_unit"].mean())

print("--- Exercise 6 ---")

print(df["region"].unique())
print(df["region"].value_counts())


print("--- Exercise 7 ---")

small_df = df[["region", "product", "revenue"]]

print(small_df.shape)


print("--- Exercise 8 ---")

df.to_csv("data/explored.csv", index=False)

print("Saved data/explored.csv")

# Reflection Questions: Answer the following questions in 2-3 sentences each.
# 1. Without looking at your code, can you explain what a boolean filter does in plain English? Practice saying it out loud.
# 

# 2. What is the difference between df["revenue"] and df[["revenue"]]? When does the distinction matter?
# 

# 3. If a colleague who only knows Excel asked you to explain why you would choose pandas for this task, what is the single most compelling reason you would give?
# 
