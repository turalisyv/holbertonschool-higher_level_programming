#!/usr/bin/python3
'''
My module document
'''


def convert_csv_to_json(csv_file_path):
    '''
    My function document
    '''

    import json
    import csv
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True

    except Exception:
        return False
