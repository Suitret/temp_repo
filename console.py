#!/usr/bin/python3
"""
This module is dedicated to the command interpreter
of this project, it features the HBNBCommand class
"""

import cmd, sys

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




if __name__ == "__main__":
    HBNBCommand().cmdloop()
