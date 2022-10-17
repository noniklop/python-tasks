import csv
import json


def read_csv():
    with open('cars.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_cars.append(row)

    cars_json = json.dumps(list_cars, indent=2)
    return cars_json


def write_json(cars_json):
    with open('cars.json', "w") as json_file:
        json_file.write(cars_json)


if __name__ == '__main__':
    list_cars = []
    write_json(read_csv())
