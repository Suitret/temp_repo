#!/usr/bin/python3
"""
This is the test file that test for the
correctness of the BaseModel.
File: ../models/base_model.py
Class: BaseModel
Function: No function particularly, but all
inside Base Model
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """A class that tests the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        cls.fir_base = BaseModel()
        cls.sec_base = BaseModel()
        cls.thi_base = BaseModel()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_for_correct_type_for_instances(self):
        self.assertTrue(type(self.fir_base.id), str)
        self.assertTrue(type(self.sec_base.id), str)
        self.assertIsInstance(self.fir_base.created_at, datetime.datetime)
        self.assertIsInstance(self.sec_base.updated_at, datetime.datetime)

    def test_for_non_quality_between_updated_at_and_created_(self):
        self.assertNotEqual(self.fir_base.created_at, self.fir_base.updated_at)
        self.assertNotEqual(self.sec_base.created_at, self.sec_base.updated_at)

    def test_the_save_method_inside_the_class(self):
        self.fir_base.save()
        self.assertNotEqual(self.fir_base.created_at, self.fir_base.updated_at)
        self.sec_base.save()
        self.assertNotEqual(self.sec_base.created_at, self.sec_base.updated_at)

    def test_for_methods_returns_type(self):
        self.assertEquals(type(self.fir_base.to_dict()), dict)

    def test_for_correctness_when_kwargs_is_specified(self):
        self.thi_base = BaseModel(**self.sec_base.to_dict())

        self.assertEqual(self.thi_base.id, self.sec_base.id)
        self.assertEqual(
            self.thi_base.created_at.isoformat(),
            self.sec_base.created_at
        )
        self.assertEqual(
            self.thi_base.updated_at.isoformat(),
            self.sec_base.updated_at
        )

    def test_the_instance_created_with_kwargs_is_different_from_old(self):
        self.assertIsNot(self.sec_base, self.thi_base)


if __name__ == "__main__":
    unittest.main()
