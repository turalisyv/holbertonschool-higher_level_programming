#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    try:
        a_dictionary[key] = value

    except KeyError:
        a_dictionary.update({key: value})

    return a_dictionary
