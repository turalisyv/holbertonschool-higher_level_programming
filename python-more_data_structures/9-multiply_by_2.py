#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key, value in new_dictionary.items():
        if type(value) is int:
            new_dictionary[key] *= 2

    return new_dictionary
