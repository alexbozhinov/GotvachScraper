# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
from unittest import TestCase
from modules import chef
from modules import scraper


class TestChef(TestCase):
    """
    Test if the recipe chef data is correctly collected when scraping   
    """
    
    def setUp(self):
        self.url = "https://recepti.gotvach.bg/r-5458-Колачета"
        self.test_chef = chef.Chef(self.url, scraper.Scraper.header)

    def test_chef_name(self):
        self.assertEqual(u"Rosi Trifonova", self.test_chef.name)

    def test_chef_hats(self):
        self.assertEqual(6000.0, self.test_chef.hats)

    def test_chef_hearts(self):
        self.assertEqual(26000.0, self.test_chef.hearts)

    def test_chef_plates(self):
        self.assertEqual(1000.0, self.test_chef.plates)

    def test_chef_rating(self):
        self.assertEqual(11000.0, self.test_chef.get_ratings())


if __name__ == '__main__':
    unittest.main()
