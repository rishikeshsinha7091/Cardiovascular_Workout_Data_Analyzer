# src/heartrate_vs_distance.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_cardio.csv")

# Remove rows where heart rate is missing
df = df.dropna(subset=["Average Heart Rate (bpm)"])

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Distance (km)"],
    df["Average Heart Rate (bpm)"]
)

plt.title("Heart Rate vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Average Heart Rate (bpm)")

plt.tight_layout()

plt.savefig("images/heartrate_vs_distance.png")

print("Heart rate chart saved!")