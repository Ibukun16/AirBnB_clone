#!/usr/bin/python3
"""
This tasks defines the BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    for other classes in the project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel class"""
        tfmat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, tfmat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return the string representation of the BaseModel
        instance. [<class name>] (<self.id>) <self.__dict>.
        """
        obj = self.__class__.__name__
        return "[{}] ({}) {}".format(obj, self.id, self.__dict__)

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance containing
        all key/value pairs of __dict__
        """
        dicto = self.__dict__.copy()
        dicto["created_at"] = self.created_at.isoformat()
        dicto["updated_at"] = self.updated_at.isoformat()
        dicto["__class__"] = self.__class__.__name__
        return dicto

    def save(self):
        """Update the 'updated_at' attribute with the current timedate"""
        self.updated_at = datetime.now()
        models.storage.save()
