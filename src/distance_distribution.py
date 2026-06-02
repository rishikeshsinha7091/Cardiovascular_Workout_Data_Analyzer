import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_cardio.csv")

plt.figure(figsize=(8,5))

plt.hist(df["Distance (km)"], bins=20)

plt.title("Workout Distance Distribution")
plt.xlabel("Distance (km)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("images/distance_distribution.png")

print("Distance chart saved!")