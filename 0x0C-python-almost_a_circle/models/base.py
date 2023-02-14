#!/usr/bin/python3
"""Base Class"""


import json
import os
import csv
import time
from random import randrange


class Base:
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
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: list of instances who inherits from Base
        """

        file = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(file, "w") as file_obj:
            file_obj.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation

        Args:
            json_string: string to decode
        """

        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of intances"""

        file = "{}.json".format(cls.__name__)
        instances = []
        if os.path.isfile(file):
            with open(file, "r", endcoding="utf-8") as file_obj:
                for dictionary in cls.from_json_string(file_obj.read()):
                    instances.append(cls.create(**dictionary))
        return instances
