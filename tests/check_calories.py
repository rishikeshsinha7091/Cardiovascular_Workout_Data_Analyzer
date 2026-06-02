# src/check_calories.py

import pandas as pd

df = pd.read_csv("data/cleaned_cardio.csv")

print(df["Calories Burned"].describe())

print("\nTop 10 Largest Values:\n")
print(df["Calories Burned"].sort_values(ascending=False).head(10))