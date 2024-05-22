#!/usr/bin/python3
"""
This module that contains the test suite for the BaseModel class
"""
import unittest
from time import sleep
import os
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model.BaseModel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        This function checks if instance has an id assigned on initialization
        """
        b_mod = BaseModel()
        self.assertTrue(hasattr(b_mod, "id"))


    def test_str_representation(self):
        """
        This function checks if the string representation is appropriate
        """
        b_mod = BaseModel()
        self.assertEqual(str(b_mod),
                         "[BaseModel] ({}) {}".format(b_mod.id, b_mod.__dict__))


    def test_ids_is_unique(self):
        """
        This function checks if id is generated randomly and uniquely
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


    def test_type_of_id_is_str(self):
        """
        This function checks if the id generated is a str object
        """
        b_mod = BaseModel()
        self.assertTrue(type(b_mod.id) is str)


    def test_created_at_is_datetime(self):
        """
        This function checks if the attribute 'created_at' is a datetime object
        """
        b_mod = BaseModel()
        self.assertTrue(type(b_mod.created_at) is datetime)


    def test_updated_at_is_datetime(self):
        """
        This function checks if the attribute 'updated_at' is a datetime object
        """
        bmod = BaseModel()
        self.assertTrue(type(bmod.updated_at) is datetime)

    
    def test_two_models_diffrent_created_at(self):
        """
        This function checks if the attribute 'created_at' of 2 models are different
        """
        bm1 = BaseModel()
        sleep(0.02)
        bm2 = BaseModel()
        sleep(0.02)
        self.assertLess(bm1.created_at, bm2.created_at)


    def test_args_unused(self):
        """
        This function checks if the attribute 'args' is not used.
        """
        b_mod = BaseModel(None)
        self.assertNotIn(None, b_mod.__dict__.values())


    def test_that_save_func_update_update_at_attr(self):
        """
        This function checks that save() method updates the updated_at attribute
        """
        bmod = BaseModel()
        bmod.save()
        self.assertNotEqual(bmod.created_at, bmod.updated_at)
        self.assertGreater(bmod.updated_at.microsecond,
                           bmod.created_at.microsecond)


    def test_if_to_dict_returns_dict(self):
        """
        This function checks if BaseModel.to_dict() returns a dictionary object
        """
        b_mod = BaseModel()
        self.assertTrue(type(b_mod.to_dict()) is dict)


    def test_if_to_dict_returns_class_dunder_method(self):
        """
        This function checks if BaseModel.to_dict() contains __class__
        """
        bmod = BaseModel()
        self.assertTrue("__class__" in bmod.to_dict())


    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """
        This function checks that created_at is stored as a str obj in ISO format
        """
        bmod = BaseModel()
        self.assertEqual(bmod.to_dict()["created_at"], bmod.created_at.isoformat())


    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """
        This function ensures updated_at is stored as a str obj in ISO format
        """
        bmod = BaseModel()
        self.assertEqual(bmod.to_dict()["updated_at"], bmod.updated_at.isoformat())


    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
        """
        This function ensures 'to_dict()' returns the expected
        number of keys/values
        """
        b_mod = BaseModel()
        partial_expectation = {key: value for key, value in b_mod.__dict__.items()
                                if not key.startswith("_")}
        self.assertEqual(len(b_mod.to_dict()), len(partial_expectation) + 1)


    def test_when_kwargs_passed_is_empty(self):
        """
        This function automatically generate id, created_at and updated_at,
        if they're not in kwargs
        """
        my_dict = {}
        bmod = BaseModel(**my_dict)
        self.assertTrue(type(bmod.id) is str)
        self.assertTrue(type(bmod.created_at) is datetime)
        self.assertTrue(type(bmod.updated_at) is datetime)


    def test_when_kwargs_passed_is_not_empty(self):
        """
        This function ensures id, created_at and updated_at are created from kwargs
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        bmodel = BaseModel(**my_dict)
        self.assertEqual(bmodel.id, my_dict["id"])
        self.assertEqual(bmodel.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(bmodel.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_args_and_kwargs_are_passed(self):
        """
        This function makes BaseModel ignore args When args and kwargs are passed.
        """
        datey = datetime.now()
        datey_iso = datey.isoformat()
        bm = BaseModel("1234", id="234", created_at=datey_iso, name="Firdaus")
        self.assertEqual(bm.id, "234")
        self.assertEqual(bm.created_at, datey)
        self.assertEqual(bm.name, "Firdaus")


    def test_when_kwargs_passed_is_more_than_default(self):
        """
        This function checks that BaseModel does not break when kwargs
        contains more than the default attributes
        """
        dico = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        bmodel = BaseModel(**dico)
        self.assertTrue(hasattr(bmodel, "name"))


    def test_new_method_not_called_when_dict_obj_is_passed_to_BaseModel(self):
        """
        The function test ensures that storage.new() is not called
        when a BaseModel obj is created from a dictionary object
        """
        dico = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        bmod = BaseModel(**dico)
        self.assertTrue(bmod not in models.storage.all().values(),
                        "{}".format(models.storage.all().values()))
        del bmod

        bmod = BaseModel()
        self.assertTrue(bmod in models.storage.all().values())


    def test_that_save_method_updates_updated_at_attr(self):
        """
        This function ensures that save() method updates 'updated_at' attribute
        """
        bmod = BaseModel()
        sleep(0.02)
        temp_update = bmod.updated_at
        bmod.save()
        self.assertLess(temp_update, bmod.updated_at)

    def test_that_save_can_update_two_or_more_times(self):
        """
        This function tests that the save method updates 'updated_at' two times
        """
        bmod = BaseModel()
        sleep(0.02)
        temp_update = bmod.updated_at
        bmod.save()
        sleep(0.02)
        temp1_update = bmod.updated_at
        self.assertLess(temp_update, temp1_update)
        sleep(0.01)
        bmod.save()
        self.assertLess(temp1_update, bmod.updated_at)


    def test_save_update_file(self):
        """
        This function tests if file is updated when the 'save' is called
        """
        bmod = BaseModel()
        bmod.save()
        baseid = "BaseModel.{}".format(bmod.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(baseid, f.read())


    def test_that_to_dict_contains_correct_keys(self):
        """
        This functon checks whether to_dict() returns the expected key
        """
        dictionary = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for obj in attrs:
            self.assertIn(obj, dictionary)

    def test_to_dict_contains_added_attributes(self):
        """
        This function checks that new attributes are also returned by to_dict()
        """
        bmod = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        bmod.name = "Firdaus"
        bmod.email = "firduas@gmail.com"
        attrs.extend(["name", "email"])
        for obj in attrs:
            self.assertIn(obj, bmod.to_dict())

    def test_to_dict_output(self):
        """
        This function checks that output returned by to_dict()
        """
        bm = BaseModel()
        datey = datetime.now()
        bm.id = "12345"
        bm.created_at = bm.updated_at = datey
        test_dico = {
            'id': "12345",
            'created_at': datey.isoformat(),
            'updated_at': datey.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(test_dico, bm.to_dict())

    def test_to_dict_with_args(self):
        """
        This function checks that TypeError is returned when
        argument is passed to to_dict()
        """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_to_dict_not_dunder_dict(self):
        """
        This function checks that to_dict() is a dict object not equal to __dict__
        """
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)


if __name__ == "__main__":
    unittest.main()
