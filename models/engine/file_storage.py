#!/usr/bin/python3
"""This file defines the FileStorage class."""
import json
import os
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
        __objects (dict): A dictionary of instantiated objects.
    
    Public Instance Methods:
        (a) all(self): Return the dictionary __objects
        (b) new(self, obj): sets in __objects the obj with key <obj class name>.
        (c) save(self): serializes __objects to the JSON file (path: __file_path)
        (d) reload(self): deserializes the JSON file to __objects (only if the JSON)
        """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obclname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obclname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obdict = FileStorage.__objects
        dict_store = {obj: obdict[obj].to_dict() for obj in obdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_store, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                for item in json.load(f).values():
                    self.new(eval(item["__class__"])(**item))
        except FileNotFoundError:
            return
