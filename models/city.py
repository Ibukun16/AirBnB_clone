#!/usr/bin/python3
"""This function defines the City class, which is a subclass of BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class with additional public class attributes.

    Attributes:
        state_id (str) - empty string: This will be the state.id
        name (str) - empty string: This is the name of the city.
    """
    state_id = ""
    name = ""
