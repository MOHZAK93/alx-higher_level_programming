#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for y in range(len(roman_string)):
        if y == 0:
            value += dic[roman_string[y]]
        if roman_string[y] == 'I' and y != 0:
            if dic['I'] <= dic[roman_string[y - 1]]:
                value += dic['I']
            else:
                value += dic['I']
                value -= dic[roman_string[y - 1]]
        elif roman_string[y] == 'V' and y != 0:
            if dic['V'] <= dic[roman_string[y - 1]]:
                value += dic['V']
            else:
                value += dic['V']
                value -= dic[roman_string[y - 1]]
        elif roman_string[y] == 'X' and y != 0:
            if dic['X'] <= dic[roman_string[y - 1]]:
                value += dic['X']
            else:
                value += dic['X']
                value -= dic[roman_string[y - 1]]
        elif roman_string[y] == 'L' and y != 0:
            if dic['L'] <= dic[roman_string[y - 1]]:
                value += dic['L']
            else:
                value += dic['L']
                value -= dic[roman_string[y - 1]]
        elif roman_string[y] == 'C' and y != 0:
            if dic['C'] <= dic[roman_string[y - 1]]:
                value += dic['C']
            else:
                value += dic['C']
                value -= dic[roman_string[y - 1]]
        elif roman_string[y] == 'D' and y != 0:
            if dic['D'] <= dic[roman_string[y - 1]]:
                value += dic['D']
            else:
                value += dic['D']
                value -= dic['D']
        elif roman_string[y] == 'M' and y != 0:
            if dic['M'] <= dic[roman_string[y - 1]]:
                value += dic['M']
            else:
                value += dic['M']
                value -= dic[roman_string[y - 1]]
    return (value)
