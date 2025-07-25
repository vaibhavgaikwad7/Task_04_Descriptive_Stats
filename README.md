﻿# Task_04_Descriptive_Stats

This research task analyzes political social media activity during the 2024 U.S. presidential election. The goal is to generate descriptive statistics using **pure Python**, **Pandas**, and **Polars** across identical datasets.

Dataset link - https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view

## 📁 Repository Structure

scripts/
├── pure_python_stats.py # Stats using built-in libraries
├── pandas_stats.py # Stats using Pandas
├── polars_stats.py # Stats using Polars
.gitignore # Ignores large data files
README.md # Summary and instructions


> 🚫 Datasets are excluded as they exceed GitHub’s upload limits.  
> ✅ Add them locally in a `data/` folder to run the scripts.

---

## 🚀 How to Run

> Ensure you have the dataset placed in `data/` before running any script.

```bash
# Pure Python analysis
python scripts/pure_python_stats.py

# Pandas analysis
python scripts/pandas_stats.py

# Polars analysis
python scripts/polars_stats.py

```


## 🧪 Summary of Insights
The dataset includes ~250K Facebook ads/posts with features like page_id, ad_id, spend, impressions, and various topic flags.

Group-by analysis was performed on:

page_id

page_id + ad_id

Polars offered noticeably faster performance on group-by aggregations.

Pure Python required significantly more code to match Pandas/Polars outputs.

Polars needed careful handling of schemas and data types (e.g., deduplication, group-by API quirks).


## 📝 Reflection on Descriptive Statistics Findings
In this analysis, we explored a large dataset of U.S. political Facebook ads using three different methods—Pandas, Polars, and pure Python. Each approach helped us validate results across tools and compare computational performance. Below are the key findings:

🔑 1. Dominant Page and Ad Distribution
A small number of Facebook pages account for the majority of ads. For example, one page (page_id) posted 55,000+ ads, indicating potential coordinated or high-budget campaigns.

Conversely, ad IDs were mostly unique, with top counts capped at 1—confirming that each ad is usually published once and tracked individually.

🔑 2. Spend Distribution Patterns
Grouping by page_id, the average estimated_spend varied significantly across pages, with some pages spending orders of magnitude more than others.

When grouped by both page_id and ad_id, we found high variance in spending, which suggests a mixed strategy of both micro-targeted and broad-reach ads.

🔑 3. Audience and Platform Breakdown
The currency used was overwhelmingly USD (99%+), with some minor international presence (INR, GBP, EUR).

publisher_platforms were primarily Facebook and Instagram, and most ads targeted both platforms jointly.

Demographic and regional fields like delivery_by_region and demographic_distribution often had nested dictionaries or were sparsely filled, which may point to partial data availability or limited targeting metadata.

## 🔍 Tools Comparison (Brief Insight)
Pandas is more intuitive for data exploration and readable output.

Polars demonstrated significantly faster performance on this large dataset (~250k rows), though it required minor syntax adjustments (e.g., handling deprecated functions).

Pure Python was slower and more limited in functionality, but it offered transparency into the underlying logic for learning purposes.
