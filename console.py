#!/usr/bin/python3
"""
This module is dedicated to the command interpreter
of this project, it features the HBNBCommand class
"""

import cmd
import sys
import json
from models import storage
from models.base_model import BaseModel

from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    """This is class is the command interpreter
    wrapper classs

    Attributes:
        prompt : configure the cmd prompt
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """This is the documentation for the quit function
        The function called to quit the command line interpreter

        Args:
            line: the argument passed when quit is called
            within the command line interpreter
        """
        return True

    def help_quit(self):
        """This is the documentation for help with quit as argument"""
        print(
            "\n".join(
                [
                    "Call this function to quit the command line interpreter",
                    "Call it whenever you want",
                    'Just type on an empty line "quit"',
                ]
            )
        )

    def do_EOF(self, line):
        """This is the documentation for the EOF function
        Call it whenever you want on an empty line with ^D

        Args:
            line: the argument passed when quit is called
            within the command line interpreter
        """
        print(line)
        return True

    def help_EOF(self):
        """This is the documentation for help with EOF as argument"""
        print(
            "\n".join(
                [
                    "Call this function to quit the command line interpreter",
                    "Call it whenever you want",
                    'Just type on an empty "^D"',
                ]
            )
        )

    def emptyline(self):
        """Method called when an
        empty line is entered in response to the prompt.

        Args:
            None
        """
        return False

    def cmdloop(self, intro=None):
        """Override cmd.Cmd's default behavior to read from stdin or file
        Args:
            intro (string): first sentence on output
        """
        try:
            if not sys.stdin.isatty():
                lines = sys.stdin.readlines()
                for line in lines:
                    self.onecmd(line.strip())
                return
        except KeyboardInterrupt:
            sys.exit(0)

        return cmd.Cmd.cmdloop(self, intro)

    def do_create(self, cls):
        """This is the documentation for the create function
        The function called to create a new instance of BaseModel,
        save it (to the JSON file) and print the id

        Args:
            cls: the argument passed when create is called
            within the command line interpreter
        """
        my_cls = ["User", "BaseModel", "City", "Place", "Amenity", "State"]
        if not cls:
            print("** class name missing **")
        elif cls not in my_cls:
            print("** class doesn't exist **")
        else:
            cls = globals()[cls]
            instance = cls()
            storage.new(instance)
            storage.save()
            print("{}".format(instance.id))

    def do_show(self, args):
        """This is the documentation for the show function
        The function called to print the string representation
        of an instance based on the class name and id

        Args:
            args: the arguments passed when show is called
            within the command line interpreter
        """
        my_cls = ["User", "BaseModel", "City", "Place", "Amenity", "State"]
        arguments = args.split()
        if not args:
            print("** class name missing **")
        elif arguments[0] not in my_cls:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            obj_dict = storage.all()
            key = arguments[0] + "." + arguments[1]
            try:
                value = obj_dict[key]
                print("{}".format(value))
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """This is the documentation for the destroy function
        The function called to delete an instance based on
        the class name and id (save the change into the JSON file)

        Args:
            args: the arguments passed when destroy is called
            within the command line interpreter
        """
        my_cls = ["User", "BaseModel", "City", "Place", "Amenity", "State"]
        arguments = args.split()
        if not args:
            print("** class name missing **")
        elif arguments[0] not in my_cls:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            obj_dict = storage.all()
            key = arguments[0] + "." + arguments[1]
            try:
                del obj_dict[key]
            except KeyError:
                print("** no instance found **")
            storage.save()

    def do_all(self, args):
        """This is the documentation for the all function
        The function called to print all string representation of all
        instances based or not on the class name

        Args:
            args: the arguments passed when all is called
            within the command line interpreter
        """
        my_cls = ["User", "BaseModel", "City", "Place", "Amenity", "State"]
        args = args.split()
        storage.reload()
        obj_dic = storage.all()
        if not args:
            tab = [str(obj_dic[k]) for k in obj_dic.keys()]
            print(tab)
        elif args[0] not in my_cls:
            print("** class doesn't exist **")
        else:
            tab = [str(obj_dic[k]) for k in obj_dic.keys() if args[0] in k]
            print(tab)

    def do_update(self, args):
        """This is the documentation for the update function
        The function called to update an instance based on the
        class name and id by adding or updating attribute

        Args:
            args: the arguments passed when all is called
            within the command line interpreter
        """
        my_cls = ["User", "BaseModel", "City", "Place", "Amenity", "State"]
        args = args.split()
        storage.reload()
        obj_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()
 

if __name__ == "__main__":
    HBNBCommand().cmdloop()
