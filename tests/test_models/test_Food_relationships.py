#!/usr/bin/python3
"""Testing the Food Model"""

import unittest
from models.Food import Food
from models.Recipe import Recipe
from models.Ingredient import Ingredient


class Test_Food_Relation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        cls.food = Food()
        cls.ingredient1 = Ingredient()
        cls.ingredient2 = Ingredient()
        cls.recipe = Recipe()
        cls.recipe.content = '1- add salt\n2- add pepper\n3- add water'
        cls.recipe.food_id = cls.food.id
        cls.food.name = "Rice with speices"
        cls.food.category = "Rice"
        cls.ingredient1.name = "Carrot"
        cls.ingredient2.name = "Tomato"
        cls.food.save()
        cls.recipe.save()
        cls.ingredient1.save()
        cls.ingredient2.save()
    
    @classmethod
    def tearDownClass(cls):
        from models import storage
        cls.food.delete()
        storage.close()

    # ____________________________________________________________________________________

    def test_add_ingredient(self):
        from models import storage

        storage.append_ingredient_to_food(self.food.id, self.ingredient1.id, '3 pcs')
        storage.append_ingredient_to_food(self.food.id, self.ingredient2.id, '5 pcs')

    # ____________________________________________________________________________________
        
    def test_get_ingrds_from_food(self):
        self.assertEqual(len(self.food.ingredients), 2)
    
    # ____________________________________________________________________________________
    
    def test_get_recipe_from_food(self):
        self.assertEqual(len(self.food.recipe), 1)
        self.assertEqual(len(self.recipe.content), len(self.food.recipe[0].content))
    

if __name__ == '__main__':
    unittest.main()
