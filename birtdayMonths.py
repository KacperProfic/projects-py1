from collections import Counter
import json

with open('info.json', 'r') as f:
    data = json.load(f)

months = []

for val in data.values():
    month = val.split('-')[1]
    months.append(month)

months_counter = Counter(months)

for month, count in months_counter.items():
    print(f"Month: {month}, Count: {count}")