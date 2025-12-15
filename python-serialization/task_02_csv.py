#!/usr/bin/python3
'''
My module document
'''


def convert_csv_to_json(data):
    '''
    My function document
    '''

    import json
    import csv

    json_data = []

    with open(data, mode='r', newline='') as file:

        csv = csv.reader(file)
        csv = list(csv)
        for i in csv[1:]:
            json_data.append(dict(zip(csv[0], i)))

    with open("data.json", mode="w") as f:
        json.dump(json_data, f, indent=4)
