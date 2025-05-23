import csv

with open("username.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)