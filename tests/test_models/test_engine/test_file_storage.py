#!/usr/bin/python3

import os
import unittest
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.test_save = BaseModel()

    def test_save(self):
        self.test_save.save()
        storage.reload()
        self.assertTrue(hasattr(self.test_save, 'save'))