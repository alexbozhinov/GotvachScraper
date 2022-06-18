# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
from unittest import TestCase
from modules import scraper
from modules import recipe


class MockArgParser:
    def __init__(self, n_dishes, products, last_cooked, dish_name, agents):
        self.n_dishes = n_dishes
        self.products = products
        self.last_cooked = last_cooked
        self.dish_name = dish_name
        self.agents = agents


class TestScraper(TestCase):
    """
    mock arguments
    """
    
    def setUp(self):
        self.a = MockArgParser(2, [u"ягоди"], True, u"мусака", [u"риба"])

    def test_main_page_url(self):
        main_url = scraper.Scraper(args=self.a).GOTVACH_MAIN_PAGE
        self.assertEqual("https://recepti.gotvach.bg/", main_url)

    def test_last_cooked_tag(self):
        main_url = scraper.Scraper(args=self.a).L_COOKED_TAG
        self.assertEqual("-cook", main_url)

    def test_search_box(self):
        main_url = scraper.Scraper(args=self.a).SEARCH_BOX
        self.assertEqual("?kw=", main_url)

    def test_scraper_dishes_count(self):
        d_count = scraper.Scraper(args=self.a).dishes_count
        self.assertEqual(2, d_count)

    def test_set_recipes_by_product(self):
        """
        Test if the urls count of recipes when searched by product are correct
        """
        s = scraper.Scraper(args=self.a)
        s.set_recipes_by_product()
        self.assertEqual(2, len(s.recipes))

    def test_set_recipes_by_last_cooked(self):
        """
        Test if the urls count of recipes when searched by last cooked are correct
        """
        s = scraper.Scraper(args=self.a)
        s.set_recipes_by_last_cooked()
        self.assertEqual(2, len(s.recipes))    

    def test_set_recipes_by_dish_name(self):
        """
        Test if the urls count of recipes when searched by recipe name are correct
        """
        s = scraper.Scraper(args=self.a)
        s.set_recipes_by_recipe_name()
        self.assertEqual(2, len(s.recipes))

    def test_product_list_not_contains_agent(self):
        """
        Test if the list contains agents
        """
        s = scraper.Scraper(args=self.a)
        product_list = s.recipes
        test_contains_agents = s.product_list_contains_agent(product_list)
        self.assertEqual(False, test_contains_agents)


if __name__ == '__main__':
    unittest.main()
