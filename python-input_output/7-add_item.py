#!/usr/bin/python3

if __name__=="__main__":
    '''
    And God said "let there run code!"
    '''
    import sys
    import json
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        data = load_from_json_file("add_item.json")

    except FileNotFoundError:
        with open("add_item.json", "w") as f:
            f.close()
        data = []
        save_to_json_file(data, "add_item.json")

    for i in range(1, len(sys.argv)):
        data.append(sys.argv[i])

    save_to_json_file(data, "add_item.json")
