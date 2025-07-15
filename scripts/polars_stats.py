import polars as pl

df = pl.read_csv("data/2024_fb_ads_president_scored_anon.csv")

print("===== Full Dataset Stats =====")
print(df.describe())

cat_cols = [col for col, dtype in df.schema.items() if dtype == pl.Utf8]

for col in cat_cols:
    print(f"\nTop 5 Value Counts for '{col}':")
    print(
        df.group_by(col)
          .agg(pl.count().alias("count"))
          .sort("count", descending=True)
          .limit(5)
    )

print("\n===== Grouped by page_id =====")
print(df.group_by("page_id").agg([
    pl.count(),
    pl.mean("estimated_spend"),
    pl.min("estimated_spend"),
    pl.max("estimated_spend")
]))

print("\n===== Grouped by page_id and ad_id =====")
print(df.group_by(["page_id", "ad_id"]).agg([
    pl.count(),
    pl.mean("estimated_spend"),
    pl.min("estimated_spend"),
    pl.max("estimated_spend")
]))
