import csv
from collections import defaultdict, Counter
from statistics import mean, stdev

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

filename = "data/2024_fb_ads_president_scored_anon.csv"

with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

column_data = defaultdict(list)
for row in data:
    for col, val in row.items():
        if val:
            column_data[col].append(val)

for col, values in column_data.items():
    print(f"\n--- Column: {col} ---")
    if all(is_float(v) for v in values):
        num_vals = list(map(float, values))
        print(f"Count: {len(num_vals)}")
        print(f"Mean: {mean(num_vals):.2f}")
        print(f"Min: {min(num_vals)}")
        print(f"Max: {max(num_vals)}")
        if len(num_vals) > 1:
            print(f"Std Dev: {stdev(num_vals):.2f}")
    else:
        counts = Counter(values)
        print(f"Unique: {len(counts)}")
        most_common = counts.most_common(1)[0]
        print(f"Most Frequent: {most_common[0]} ({most_common[1]} times)")
