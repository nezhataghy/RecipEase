#!/usr/bin/python3
"""Testing the Food Model"""

import unittest
from models.Food import Food
from models.Recipe import Recipe
from models.Basemodel import BaseModel


class Test_Recipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.food = Food()
        cls.food.name = "Couscous with chicken"
        cls.food.category = "Couscous"
        cls.food.save()
        cls.recipe = Recipe()
        cls.recipe.content = "1- wash\n2- your\n3- hands\n4- and\n5- cook\n6- the\n7- food\n8- eat"
        cls.recipe.food_id = cls.food.id
        cls.recipe.save()
        
    @classmethod
    def tearDownClass(cls):
        cls.food.delete()

    """      _____________Testing attributes getters_____________        """
    # ID
    def test_getter_id(self):
        self.assertTrue(self.recipe.id)

    # created_at
    def test_getter_created_at(self):
        self.assertTrue(self.recipe.created_at)

    # updated_at
    def test_getter_updated_at(self):
        self.assertTrue(self.recipe.updated_at)

    # ____________________________________________________________________________________

    def test_recipe_saving(self):
        from models import storage

        recipe = storage.get_obj_by_id(Recipe, self.recipe.id)
        self.assertEqual(recipe.id, self.recipe.id)

    # ____________________________________________________________________________________

    def test_instance(self):
        self.assertIsInstance(self.recipe, Recipe)
        self.assertTrue(issubclass(Recipe, BaseModel))


if __name__ == '__main__':
    unittest.main()
