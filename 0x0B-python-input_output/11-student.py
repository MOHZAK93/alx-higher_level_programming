#!/usr/bin/python3
"""Student to JSON module"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a json representation of a Student Instance"""
        dcopy = self.__dict__.copy()
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) != str:
                    return dcopy
            dattrs = {}
            for attr in attrs:
                if attr in dcopy:
                    dattrs[attr] = dcopy[attr]
            return dattrs
        return dcopy

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for attr in json:
            if attr in self.__dict__:
                self.__dict__[attr] = json[attr]
