#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for x in a_dictionary:
        if x == key:
            del a_dictionary[key]
            return (a_dictionary)
    return (a_dictionary)
