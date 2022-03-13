#!/usr/bin/python3

"""contains the entry point of the CI"""

import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """defines the characteristics of our command interpreter"""
    prompt = '(hbnb)'
    classes = [BaseModel, User, State, City, Amenity, Place, Review]
    class_dict = dict()
    for c in classes:
        class_dict[c.__name__] = c
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

    def do_create(self, line):
        """creates a new insatnce of the BaseModel"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        else:
            new = self.class_dict[args[0]]()
            storage.save()
            print(new.id)

    def do_show(self, line):
        """Prints str rep of an instance based on the class name and id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            all_keys = storage.all()
            key = args[0] + "." + args[1]

            if key not in all_keys.keys():
                print("** no instance found **")

            else:
                print(all_keys[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            all_keys = storage.all()
            key = args[0] + "." + args[1]

            if key not in all_keys.keys():
                print("** no instance found **")

            else:
                del all_keys[key]
                storage.save()

    def all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        args = line.split()

        if len(args) == 0:
            print([str(v) for v in storage.all().values()])

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        else:
            print([str(v) for v in storage.all().values()
                  if v.__class__.__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the
        class name and id by adding or updating attribute"""
        args = line.split()
        int_attrs = ("number_rooms", "number_bathrooms",
                     "max_guest", "price_by_night")
        flt_attrs = ("latitude", "longitude")

        if (len(args) == 0):
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            all_keys = storage.all()
            key = args[0] + "." + args[1]

            if key not in all_keys.keys():
                print("** no instance found **")

            else:
                if len(args) == 2:
                    print("** attribute name missing **")

                elif len(args) == 3:
                    print("** value missing **")

                else:
                    args[3] = args[3].strip('"')
                    if args[2] in int_attrs:
                        value = int(args[3])
                    elif args[2] in flt_attrs:
                        value = float(args[3])
                    # currently no check or error message for wrong format --
                    # deafults to string; int() or float() fail crashes
                    else:
                        value = args[3]
                    all_keys[key].__dict__[args[2]] = value
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
