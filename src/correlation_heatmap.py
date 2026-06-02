import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_cardio.csv")

numeric_df = df.select_dtypes(include=["float64", "int64"])

corr = numeric_df.corr()

plt.figure(figsize=(8, 6))

plt.imshow(corr)

plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png")

print("Heatmap saved!")