#!/usr/bin/python3
"""
This module is dedicated to the command interpreter
of this project, it features the HBNBCommand class
"""
import ast
import cmd
import sys
from models import storage
from models.base_model import BaseModel
import models
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
    className = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

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
        if not cls:
            print("** class name missing **")
        elif cls not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.className[cls]()
            HBNBCommand.className[cls].save(obj)
            print(obj.id)

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
            obj_value = obj_dic[key]
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

    def default(self, arg):
        """Default command that handles class cmds: <class name>.func()"""
        """
        <class name>.all(): retrieve all instances of a class
        <class name>.count(): retrieve the number of instances of a class
        <class name>.show(<id>): retrieve an instance based on its ID
        <class name>.destroy(<id>): destroy an instance based on his ID
        <class name>.update(<id>, <attribute name>, <attribute value>):
        update an instance based on his ID
        <class name>.update(<id>, <dictionary representation>):
        update an instance based on his ID
        Note: d = ast.literal_eval(re.search('({.+})', update_dict).group(0))
        """
        args = arg.split(".", 1)
        # print("default: {}".format(args))
        if args[0] in HBNBCommand.className.keys():
            if args[1].strip("()") == "all":
                self.do_all(args[0])
            elif args[1].strip("()") == "count":
                self.obj_count(args[0])
            elif args[1].split("(")[0] == "show":
                self.do_show(args[0] + " " + args[1].split("(")[1].strip(")"))
            elif args[1].split("(")[0] == "destroy":
                self.do_destroy(args[0] + " " + args[1].split("(")[1]
                                .strip(")"))
            elif args[1].split("(")[0] == "update":
                arg0 = args[0]
                if ", " not in args[1]:
                    arg1 = args[1].split("(")[1].strip(")")
                    self.do_update(arg0 + " " + arg1)
                elif ", " in args[1] and "{" in args[1] and ":" in args[1]:
                    arg1 = args[1].split("(")[1].strip(")").split(", ", 1)[0]
                    attr_dict = ast.literal_eval(
                        args[1].split("(")[1].strip(")").split(", ", 1)[1]
                    )
                    # Note: json.loads NOT working here w/ single-quoted values
                    # attr_dict = json.loads(args[1].split('(')[1].strip(')')\
                    # .split(', ', 1)[1])
                    for key, value in attr_dict.items():
                        self.do_update(arg0 + " " + arg1 + " " + key +
                                       " " + str(value))
                elif (
                    ", " in args[1]
                    and len(args[1].split("(")[1].strip(")").split(", ")) == 2
                ):
                    arg1 = args[1].split("(")[1].strip(")").split(", ")[0]
                    arg2 = args[1].split("(")[1].strip(")").split(", ")[1]
                    self.do_update(arg0 + " " + arg1 + " " + arg2)
                elif (
                    ", " in args[1]
                    and len(args[1].split("(")[1].strip(")").split(", ")) >= 3
                ):
                    print(args[1])
                    arg1 = args[1].split("(")[1].strip(")").split(", ")[0]
                    print(arg1)
                    arg2 = args[1].split("(")[1].strip(")").split(", ")[1]
                    print(arg2)
                    arg3 = args[1].split("(")[1].strip(")").split(", ")[2]
                    print(arg3)
                    self.do_update(arg0 + " " + arg1 + " " + arg2 + " " + arg3)
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("** class doesn't exist **")

    @staticmethod
    def obj_count(arg):
        """Obj_count command to print the number of instances of a class"""
        """
        Usage: <class name>.count(), retrieve the number of instances
        of a class
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            counter = 0
            for key, obj in models.storage._FileStorage__objects.items():
                if arg == key.split(".")[0]:
                    counter += 1
            print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
