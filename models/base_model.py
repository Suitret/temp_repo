#!/usr/bin/python3
"""
This module devises a class named BaseModel
"""
import uuid
import datetime
import models


class BaseModel:
    """This is the BaseModel class that defines
    all common attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """This is BaseModel class constructor

        Args:
          args (tuple): used for non key-worded arguments
          kwargs (dict): used for key-worded arguments
        Returns:
            None
        """

        if kwargs and kwargs is not None and type(kwargs) is not None:
            if "__class__" in kwargs.keys():
                kwargs.pop("__class__")
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" in kwargs.keys():
                kwargs["created_at"] = datetime.datetime.strptime(
                    kwargs["created_at"], date_format
                )
            if "updated_at" in kwargs.keys():
                kwargs["updated_at"] = datetime.datetime.strptime(
                    kwargs["updated_at"], date_format
                )
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """An instance method that prints
        [<class name>] (<self.id>) <self.__dict__>

        Returns:
            None
        """
        to_be_returned = f"{[self.__class__.__name__]} " f"({self.id}) {self.__dict__}"
        return to_be_returned

    def save(self):
        """A public instance method that updates the public
        instance attribute updated_at with the current datetime

        Args:
            None

        Returns:
            None
        """
        self.updated_at = datetime.datetime.now()
        # models.storage.save()

    def to_dict(self):
        """A public instance method that returns a dictionary
        containing all keys/values of __dict__ of the instance.

        Args:
            None

        Returns:
            None
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()

        return self.__dict__
