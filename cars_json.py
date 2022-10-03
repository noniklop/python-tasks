import csv
import json

list_cars = []
with open('cars.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_cars.append(row)

cars_json = json.dumps(list_cars, indent=2)
print(cars_json)

with open('cars.json', "w") as json_file:
    json_file.write(cars_json)
