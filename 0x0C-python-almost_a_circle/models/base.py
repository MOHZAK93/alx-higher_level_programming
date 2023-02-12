#!/usr/bin/python3
"""Base Class"""
import json


class Base():
    """Parent Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation
            of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
            of list_objs to a file"""

        with open("Rectangle.json", "w") as file_obj:
            file_obj.write('[')
            for i in range(len(list_objs)):
                file_obj.write(Base.to_json_string(list_objs[i].__dict__))
                if i != len(list_objs) - 1:
                    file_obj.write(', ')
            file_obj.write(']')

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string
            representation"""
        return json.load(json_string)
