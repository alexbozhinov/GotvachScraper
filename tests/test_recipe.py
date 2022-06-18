# -*- coding: utf-8 -*-
from __future__ import print_function
import unittest
from unittest import TestCase
from modules import recipe


class TestRecipe(TestCase):
    """
    Test if the recipe id, title, list of products and chef data are correctly stored  
    """
    def setUp(self):
        self.test_recipe = recipe.Recipe(1, [u"Мусака без домати (Бяла мусака)"],
                                [u"картофи 8 бр. едри", u"кайма 350 ,  400 г смес", u"лук 1 глава",
                                 u"олио 3, 4 суп.лъж.", u"чубрица", u"черен пипер", u"магданоз"],
                                [u"name: Илияна Димова",
                                 u"hats: 4000.0",
                                 u"hearts: 4000.0",
                                 u"plates: 1000.0",
                                 u"Rating: 3000.0"])

    def test_recipe_id(self):
        self.assertEqual(1, self.test_recipe.id)

    def test_recipe_title(self):
        self.assertEqual([u"Мусака без домати (Бяла мусака)"], self.test_recipe.title)

    def test_recipe_products(self):
        self.assertEqual([u"картофи 8 бр. едри", u"кайма 350 ,  400 г смес", u"лук 1 глава",
                          u"олио 3, 4 суп.лъж.", u"чубрица", u"черен пипер", u"магданоз"],
                         self.test_recipe.products)

    def test_recipe_chef(self):
        self.assertEqual([u"name: Илияна Димова",
                          u"hats: 4000.0",
                          u"hearts: 4000.0",
                          u"plates: 1000.0",
                          u"Rating: 3000.0"],
                         self.test_recipe.chef)

    def test_recipe_rating(self):
        pass

    def test_recipe_set_times_cooked(self):
        pass


if __name__ == '__main__':
    unittest.main()
