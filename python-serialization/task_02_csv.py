#!/usr/bin/python3
'''
My module document
'''


def convert_csv_to_json(data):
    '''
    My function document
    '''

    import csv
    import json

    with open(data, mode='r', newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

    with open('data.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
