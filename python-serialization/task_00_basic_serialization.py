#!/usr/bin/python3
'''
My module document
'''


def serialize_and_save_to_file(data, filename):
    '''
    My function document
    '''

    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    '''
    My function document
    '''

    import json
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
