#!/usr/bin/python3
"""This function defines the Amenity class, which is a subclass of BaseModel"""
from models.base_mode import BaseModel


class Amenity(BaseModel):
    """This class is a subclass of BaseModel class with additional
    public class attributes
    (a) name (str) - empty string
    """

    name = ""
