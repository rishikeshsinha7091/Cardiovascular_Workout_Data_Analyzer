import pandas as pd

df = pd.read_csv("data/cardioActivities.csv")

print("=" * 50)
print("DATASET INFO")
print("=" * 50)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumerical Summary:")
print(df.describe())

print("\nWorkout Types:")
print(df["Type"].value_counts())