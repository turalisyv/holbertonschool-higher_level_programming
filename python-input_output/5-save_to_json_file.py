#!/usr/bin/python3
'''
My module document
'''


def save_to_json_file(my_obj, filename):
    '''
    My function document
    '''
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
