#!/usr/bin/python3
'''
My module document
'''


def load_from_json_file(filename):
    '''
    My function document
    '''
    import json
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
