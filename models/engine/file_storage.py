#!/usr/bin/python3
"""Module containing FileStorage class
"""
import json
import models.base_model


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
        for keys, vals in self.__objects.items():
            self.__objects[keys] = vals.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as fd:
            json.dump(self.__objects, fd)

    def reload(self):
        """This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)

         Args:
            None

        Returns:
            None
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as a_file:
                self.__objects = json.load(a_file)
            for keys, values in self.__objects.items():
                self.__objects[keys] = models.base_model.BaseModel(**values)
        except FileNotFoundError:
            pass
