#!/usr/bin/python3

def roman_to_int(roman_string):
    numbers  = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,"M": 1000}
    total = numbers[roman_string[0]]

    for i in range(1, len(roman_string)):
        if numbers[roman_string[i-1]] >= numbers[roman_string[i]]:
            total += numbers[roman_string[i]]

        else:
            total -= numbers[roman_string[i]]

    return abs(total)
