#!/usr/bin/python3
"""Testing the Food Model"""

import unittest
from models.Food import Food
from models.Basemodel import BaseModel
from models import storage


class Test_Food(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.food = Food()
        cls.food.name = "Couscous with chicken"
        cls.food.category = "Couscous"
        cls.food.save()

    @classmethod
    def tearDownClass(cls):
        cls.food.delete()
        storage.close()

    """      _____________Testing attributes getters_____________        """
    # ID
    def test_getter_id(self):
        self.assertTrue(self.food.id)

    # created_at
    def test_getter_created_at(self):
        self.assertTrue(self.food.created_at)

    # updated_at
    def test_getter_updated_at(self):
        self.assertTrue(self.food.updated_at)

    # ____________________________________________________________________________________

    def test_food_saving(self):
        from models import storage

        food = storage.get_obj_by_id(Food, self.food.id)
        self.assertEqual(food.id, self.food.id)
    
    # ____________________________________________________________________________________

    def test_instance(self):
        self.assertIsInstance(self.food, Food)
        self.assertTrue(issubclass(Food, BaseModel))


if __name__ == '__main__':
    unittest.main()
