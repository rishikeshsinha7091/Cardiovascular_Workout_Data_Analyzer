import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_cardio.csv")

plt.figure(figsize=(8,5))

plt.scatter(
    df["Distance (km)"],
    df["Calories Burned"]
)

plt.title("Calories Burned vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Calories Burned")

plt.tight_layout()

plt.savefig("images/calories_vs_distance.png")

print("Scatter plot saved!")