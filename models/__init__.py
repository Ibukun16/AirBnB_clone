#!/usr/bin/python3
"""This module contains init file that inintializes the models' directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
