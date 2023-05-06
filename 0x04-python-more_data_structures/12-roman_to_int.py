#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    value = 0
    if roman_string is None or not isinstance(roman_string, str):
        return (0)
    for i in range(len(roman_string) - 1, -1, -1):
        value = dic[roman_string[i]]
        if i < len(roman_string) - 1 and dic[roman_string[i + 1]] > value:
            result -= value
        else:
            result += value
    return (result)
