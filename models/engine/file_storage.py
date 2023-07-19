#!/usr/bin/python3
"""Module containing FileStorage class
"""
import json
from models.base_model import BaseModel

from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State


class FileStorage:
    """FileStorage class with private class attributes
    and public instance methods
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj : instance of a class
        """
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the
        JSON file (path: __file_path)

        Args:
            None

        Returns:
            None
        """
        temp_dict = {}
        for keys, vals in self.__objects.items():
            temp_dict[keys] = vals.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as fd:
            json.dump(temp_dict, fd)

    def reload(self):
        """This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)

         Args:
            None

        Returns:
            None
        """
        my_cls = ["User", "BaseModel", "City", "Place", "Amenity", "State"]
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as a_file:
                FileStorage.__objects = json.load(a_file)
            for keys, values in FileStorage.__objects.items():
                for name in my_cls:
                    if name in keys:
                        cls = globals()[name]
                        self.__objects[keys] = cls(**values)
                        break
        except FileNotFoundError:
            pass
