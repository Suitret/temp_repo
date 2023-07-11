#!/usr/bin/python3
"""Module containing FileStorage class
"""
import json


class FileStorage:
    """FileStorage class with private class attributes
       and public instance methods
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj : instance of a class
        """
        key = obj.__name__ + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        json_str = json.dump(self.__objects)
        with open(self.__file_path, "a") as file:
            file.write(json_str)

    
