#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) == 0 or roman_string is None:
        return 0
    sum = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        value = roman[roman_string[i]]
        if i + 1 < len(roman_string) and roman[roman_string[i+1]] > value:
            sum -= value
        else:
            sum += value
    return sum
