#!/usr/bin/python3
"""Testing our Basemodel"""

import unittest
from datetime import datetime
from models.Basemodel import BaseModel


class test_Basemodel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    # ____________________________________________________________________________________

    """      _____________Testing attributes getters_____________        """
    # ID
    def test_getter_id(self):
        self.assertTrue(self.base.id)

    # created_at
    def test_getter_created_at(self):
        self.assertTrue(self.base.created_at)

    # updated_at
    def test_getter_updated_at(self):
        self.assertTrue(self.base.updated_at)

    # ____________________________________________________________________________________

    """      _____________Testing attributes setters_____________      """
    # id
    def test_setter_id(self):
        self.base.id = 10
        self.assertNotEqual(self.base.id, 10)

    # created_at
    def test_setter_created_at(self):
        created_at = self.base.created_at
        self.base.created_at = datetime.utcnow()

        self.assertEqual(self.base.created_at, created_at)

    # updated_at
    def test_setter_updated_at(self):
        updated_at = self.base.updated_at
        self.base.updated_at = datetime.utcnow()

        self.assertNotEqual(self.base.updated_at, updated_at)

    # ____________________________________________________________________________________

    def test_id_type(self):
        self.assertIs(type(self.base.id), str)

    # ____________________________________________________________________________________

    # Test updated_at setter
