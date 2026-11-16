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