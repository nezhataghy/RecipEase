#!/usr/bin/python3
"""Testing the Food Model"""

import unittest
from models.Ingredient import Ingredient
from models.Basemodel import BaseModel
from models import storage

class Test_Ingredient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ingredient = Ingredient()
        cls.ingredient.name = 'Carrot'
    
    @classmethod
    def tearDownClass(cls):
        cls.ingredient.delete()
        storage.close()

    """      _____________Testing attributes getters_____________        """
    # ID
    def test_getter_id(self):
        self.assertTrue(self.ingredient.id)

    # created_at
    def test_getter_created_at(self):
        self.assertTrue(self.ingredient.created_at)

    # updated_at
    def test_getter_updated_at(self):
        self.assertTrue(self.ingredient.updated_at)

    # ____________________________________________________________________________________

    def test_ingredient_saving(self):
        from models import storage

        self.ingredient.name = "Couscous with chicken"
        self.ingredient.category = "Couscous"
        self.ingredient.save()
        ingredient = storage.get_obj_by_id(Ingredient, self.ingredient.id)
        self.assertEqual(ingredient.id, self.ingredient.id)
    
    # ____________________________________________________________________________________

    def test_instance(self):
        self.assertIsInstance(self.ingredient, Ingredient)
        self.assertTrue(issubclass(Ingredient, BaseModel))


if __name__ == '__main__':
    unittest.main()
