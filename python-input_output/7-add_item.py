#!/usr/bin/python3
'''
My module document
'''


if __name__=="__main__":
    '''
    My document
    '''
    import sys
    import json
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        data = load("add_item.json")

    except FileNotFoundError:
        with open("add_item.json", "w") as f:
            f.close()
        data = []
        save(data, "add_item.json")

    for i in range(1, len(sys.argv)):
        data.append(sys.argv[i])

    save(data, "add_item.json")
