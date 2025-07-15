import pandas as pd

df = pd.read_csv("data/2024_fb_ads_president_scored_anon.csv")

print("===== Full Dataset Stats =====")
print(df.describe(include='all'))

for col in df.select_dtypes(include=['object']).columns:
    print(f"\nValue Counts for {col}:\n", df[col].value_counts().head(5))

print("\n===== Grouped by page_id =====")
numeric_cols = df.select_dtypes(include='number').columns
print(df.groupby("page_id")[numeric_cols].agg(["count", "mean", "min", "max"]).head())

print("\n===== Grouped by page_id and ad_id =====")
print(df.groupby(["page_id", "ad_id"])[numeric_cols].agg(["count", "mean", "min", "max"]).head())
