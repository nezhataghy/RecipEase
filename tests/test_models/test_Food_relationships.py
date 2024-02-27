#!/usr/bin/python3
"""Testing the Food Model"""

import unittest
from datetime import datetime
from models.Food import Food
from models.Recipe import Recipe
from models.Ingredient import Ingredient


class Test_Food_Relation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        cls.food = Food()
        # cls.recipe = Recipe()
        cls.ingredient1 = Ingredient()
        cls.ingredient2 = Ingredient()
        cls.food.name = "Rice with speices"
        cls.food.category = "Rice"
        cls.ingredient1.name = "Carrot"
        cls.ingredient2.name = "Tomato"
        cls.food.save()
        cls.ingredient1.save()
        cls.ingredient2.save()
    
    @classmethod
    def tearDownClass(cls):
        from models import storage
        cls.food.delete()
        cls.ingredient1.delete()
        cls.ingredient2.delete()
        storage.close()

    # ____________________________________________________________________________________

    def test_add_ingredient(self):
        from models import storage

        storage.append_ingredient_to_food(self.food.id, self.ingredient1.id, '3 pcs')
        storage.append_ingredient_to_food(self.food.id, self.ingredient2.id, '5 pcs')

    # ____________________________________________________________________________________
        
    def test_get_ingrds_from_food(self):
        self.assertEqual(len(self.food.ingredients), 2)
    

if __name__ == '__main__':
    unittest.main()
