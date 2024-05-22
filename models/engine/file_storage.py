#!/usr/bin/python3
"""This module is the FileStorage class."""
import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This module represents an abstracted storage engine containing

    Private Class Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects

    Public Instance Methods:
        (a) all(self): Return the dictionary __objects
        (b) new(self, obj): set the obj with key <obj class name>.
        (c) save(self): serializes __objects to JSON file (path: __file_path)
        (d) reload(self): deserializes the JSON file
            to __objects (only if the JSON)
        """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        kv = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[kv] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdic = FileStorage.__objects
        dictn = {key: val.to_dict() for key, val in objdic.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictn, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            for item in json.load(f).values():
                self.new(eval(item["__class__"])(**item))
        except FileNotFoundError:
            return

        def attributes(self):
            """
            This returns the valid attributes with the corresponding
            types for classname
            """
            attributes = {
                "BaseModel":
                         {"id": str,
                          "created_at": datetime.datetime,
                          "updated_at": datetime.datetime},
                "User":
                         {"email": str,
                          "password": str,
                          "first_name" str,
                          "last_name": str},
                "State":
                         {"name": str},
                "City":
                         {"state_id": str,
                          "name": str},
                "Amenity":
                         {"name": str},
                "Place":
                         {"city_id": str,
                          "user_id": str,
                          "name": str,
                          "description": str,
                          "number_rooms": int,
                          "number_bathrooms": int,
                          "max_guest": int,
                          "price_by_night": int,
                          "latitude": float,
                          "longitude": float,
                          "amenity_ids": list},
                "Review":
                         {"place_id": str,
                          "user_id": str,
                          "text": str}
            }
            return attributes
