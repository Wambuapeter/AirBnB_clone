#!/usr/bin/python3

import uuid
import datetime
import models

"""defines all common attributes and methods for other classes"""


class BaseModel:
    """the base class"""

    def __init__(self, *args, **kwargs):
        """public instance attributes"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """ prints [<class name>] (<self.id>) <self.__dict__>"""
        className = self.__class__.__name__
        print("{} {} {}".format(className, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        newDict = self.__dict__.copy()
        newDict['created_at'] = self.created_at.isoformat()
        newDict['updated_at'] = self.updated_at.isoformat()
        newDict['__class__'] = self.__class__.__name__
        return newDict
