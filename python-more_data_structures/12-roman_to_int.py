#!/usr/bin/python3

def roman_to_int(roman_string):
    numbers  = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,"M": 1000}
    total = 0
    tmp = roman_string[0]

    for i in range(1, len(roman_string)): # C X X I V
        if numbers[roman_string[i]] <= numbers[roman_string[i-1]]:
            total += numbers[roman_string[i-1]]
        else:
            total -= numbers[roman_string[i-1]]

    total += numbers[roman_string[-1]]

    return total
