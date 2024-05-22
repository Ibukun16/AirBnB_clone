#!/usr/bin/python3
"""
This function defines the City class, which is a subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is a subclass of the BaseModel class with
    additional public class attributes.
    (a) state_id (str) - empty string: This will be the state.id
    (b) name (str) - empty string
    """
    state_id = ""
    name = ""
