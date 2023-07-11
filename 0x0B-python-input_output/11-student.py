#!/usr/bin/python3
"""Module Student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json func"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """reload from json"""
        for i in json:
            self.__dict__[i] = json[i]
