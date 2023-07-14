#!/usr/bin/python3
"""Module containing FileStorage class
"""
import json
import models


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
        """Serializes __objects to the JSON file"""
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(self.__file_path, mode="w", encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                self.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
