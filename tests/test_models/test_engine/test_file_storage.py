#!/usr/bin/python3
"""defines all unnittest tests for the file_storage.py module"""
import unittest
import os
import models
import pep8
from datetime import datetime
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """unittest tests for the FileStorage model class"""

    def test_FileStorage_instantiation_with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_None_as_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all_method_with_None_as_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_all_method(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_FileStorage__file_path_is_type_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_dictionary(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_type(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_new_method(self):
        base = BaseModel()
        models.storage.new(base)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        storage = models.storage.all()
        self.assertIn(f'BaseModel.{base.id}', storage.keys())
        self.assertIn(base, storage.values())
        self.assertIn(f'User.{user.id}', storage.keys())
        self.assertIn(user, storage.values())
        self.assertIn(f'State.{state.id}', storage.keys())
        self.assertIn(state, storage.values())
        self.assertIn(f'Place.{place.id}', storage.keys())
        self.assertIn(place, storage.values())
        self.assertIn(f'City.{city.id}', storage.keys())
        self.assertIn(city, storage.values())
        self.assertIn(f'Amenity.{amenity.id}', storage.keys())
        self.assertIn(amenity, storage.values())
        self.assertIn(f'Review.{review.id}', storage.keys())
        self.assertIn(review, storage.values())

    def test_new_method_with_two_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(User(), 12121212)

    def test_save_method(self):
        base = BaseModel()
        models.storage.new(base)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()
        with open("file.json", "r") as file:
            json = file.read()
        self.assertIn(f'BaseModel.{base.id}', json)
        self.assertIn(f'User.{user.id}', json)
        self.assertIn(f'State.{state.id}', json)
        self.assertIn(f'Place.{place.id}', json)
        self.assertIn(f'City.{city.id}', json)
        self.assertIn(f'Amenity.{amenity.id}', json)
        self.assertIn(f'Review.{review.id}', json)

    def test_save_method_with_None_as_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reolad_method(self):
        base = BaseModel()
        models.storage.new(base)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        kp_objs = FileStorage._FileStorage__objects
        self.assertIn(f'BaseModel.{base.id}', kp_objs)
        self.assertIn(f'User.{user.id}', kp_objs)
        self.assertIn(f'State.{state.id}', kp_objs)
        self.assertIn(f'City.{city.id}', kp_objs)
        self.assertIn(f'Place.{place.id}', kp_objs)
        self.assertIn(f'Amenity.{amenity.id}', kp_objs)
        self.assertIn(f'Review.{review.id}', kp_objs)


if __name__ == '__main__':
    unittest.main()
