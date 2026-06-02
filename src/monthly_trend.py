# src/monthly_trend.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_cardio.csv")

df["Date"] = pd.to_datetime(df["Date"])

monthly_distance = (
    df.groupby(df["Date"].dt.to_period("M"))["Distance (km)"]
    .sum()
)

monthly_distance.index = monthly_distance.index.astype(str)

plt.figure(figsize=(10,5))
monthly_distance.plot()

plt.title("Monthly Distance Covered")
plt.xlabel("Month")
plt.ylabel("Total Distance (km)")

plt.tight_layout()

plt.savefig("images/monthly_distance_trend.png")

print("Trend chart saved!")