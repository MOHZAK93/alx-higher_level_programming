#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    if a_dictionary is None:
        return (None)
    for key, value in a_dictionary.items():
        if biggest < value:
            biggest = value
    for k, v in a_dictionary.items():
        if v == biggest:
            return (k)
