#!/usr/bin/python3
"""
This __init__ module contains method for the models directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
