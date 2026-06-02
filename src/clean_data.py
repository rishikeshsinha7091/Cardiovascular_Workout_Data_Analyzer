import pandas as pd

# Load dataset
df = pd.read_csv("data/cardioActivities.csv")

print("Original Shape:")
print(df.shape)

# Remove useless columns
df = df.drop(columns=["Friend's Tagged"])

# Remove rows with absurd calorie values
df = df[df["Calories Burned"] < 10000]

print("\nShape After Cleaning:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMaximum Calories:")
print(df["Calories Burned"].max())

# Save cleaned dataset
df.to_csv("data/cleaned_cardio.csv", index=False)

print("\nCleaned dataset saved!")