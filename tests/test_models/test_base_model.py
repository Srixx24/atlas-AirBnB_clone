#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_creation_of_base_instance(self):
        my_instance = BaseModel()
        self.assertIsInstance(my_instance, BaseModel)

    