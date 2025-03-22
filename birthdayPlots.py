from bokeh.plotting import figure, show, output_file
from collections import Counter
import json


month_names = {
    "01": "Styczeń", "02": "Luty", "03": "Marzec", "04": "Kwiecień",
    "05": "Maj", "06": "Czerwiec", "07": "Lipiec", "08": "Sierpień",
    "09": "Wrzesień", "10": "Październik", "11": "Listopad", "12": "Grudzień"
}

with open('info.json', 'r') as f:
    data = json.load(f)

months = []

for val in data.values():
    month = val.split('-')[1]
    months.append(month_names[month])

months_counter = Counter(months)

months_sorted = [month_names[str(i).zfill(2)] for i in range(1, 13)]
counts = [months_counter[month] for month in months_sorted]

output_file("plot.html")
p = figure(x_range=months_sorted)

p.vbar(x=months_sorted, top=counts, width=0.5)

show(p)