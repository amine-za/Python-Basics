import csv
names = [
    {"f_name": "John", "l_name": "Doe", "age": 30},
    {"f_name": "John", "l_name": "Doe", "age": 28},
    {"f_name": "John", "l_name": "Doe", "age": 30},
    {"f_name": "John", "l_name": "Doe", "age": 30},
]

with open("data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=names[0].keys())
    writer.writerows(names)