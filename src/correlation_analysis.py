import pandas as pd

df = pd.read_csv("data/cleaned_cardio.csv")

numeric_df = df.select_dtypes(include=["float64", "int64"])

print("Correlation Matrix:")
print(numeric_df.corr())