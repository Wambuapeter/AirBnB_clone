#!/usr/bin/python3

"""contains the entry point of the CI"""

import cmd
import re
from shlex import split
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """defines the characteristics of our command interpreter"""
    prompt = '(hbnb)'
    file = None

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """signal to exit the program"""
        print("")
        return True

    def emptyLine(self):
        """execute nothing in case of empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
