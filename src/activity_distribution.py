import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_cardio.csv")

activity_counts = df["Type"].value_counts()

plt.figure(figsize=(8,5))
activity_counts.plot(kind="bar")

plt.title("Workout Type Distribution")
plt.xlabel("Workout Type")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/activity_distribution.png")

print("Chart saved!")