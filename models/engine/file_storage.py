#!/usr/bin/python3

"""File storage by converting to json"""

import json
from models.base_model import BaseModel
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """ serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "object_contents.json"
    __objects = {}

    """public instance methods"""
    def all(self):
        """returns dic __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        new_object = {}
        for key in self.__objects:
            new_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as myFile:
            myFile.write(json.dumps(new_object))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "w") as myFile:
                    new_object = json.load(myFile)
                for key, value in new_object.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
            except:
                pass
