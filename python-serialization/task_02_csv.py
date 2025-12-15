def convert_csv_to_json(csv_file_path):
    '''
    My function document
    '''

    import csv
    import json
    import os

    data = []
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

    except FileNotFoundError:
        return False

    except Exception:
        return False

    try:
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

    except Exception:
        return False
