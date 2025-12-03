#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dictionary = a_dictionary.copy()
    try:
        new_dictionary[key] = value

    except:
        new_dictionary.update({key: value})

    return new_dictionary
