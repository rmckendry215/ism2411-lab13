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
