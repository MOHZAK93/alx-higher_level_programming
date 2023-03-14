#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    if a_dictionary == {}:
        return (None)
    for key, value in a_dictionary.items():
        if biggest < value:
            biggest = value
    return ()
