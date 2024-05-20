#!/usr/bin/python3
"""This module contains the State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This defines the representation of a state

    Attributes:
        name (str): The name of the state.
    """
    name = ""
