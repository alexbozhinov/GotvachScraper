# -*- coding: utf-8 -*-
from __future__ import print_function

import time

import requests
from bs4 import *
from argparser import *
from chef import Chef
from product import Product
from recipe import *
from agents import *
from recipe_data_storage import RecipeDataStorage


class Scraper:
    """
    A class where recipes are scraped
    """
    GOTVACH_MAIN_PAGE = "https://recepti.gotvach.bg/"
    SEARCH_BOX = "?kw="
    L_COOKED_TAG = "-cook"

    header = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Safari/537.36'
    }

    def __init__(self, args=None):
        self.args = ArgParser() if args is None else args
        self.dishes_count = self.args.n_dishes
        self.searched_by_products_urls = None
        self.searched_by_last_cooked_urls = None
        self.searched_by_recipe_name_urls = None
        self.recipes = []
        self._set_searched_by_products_recipe_urls()
        self._set_searched_by_last_cooked_recipe_urls()
        self._set_searched_by_recipe_name_urls()

    def _set_searched_by_products_recipe_urls(self):
        """
        A method which sets the urls of recipes when searched by product
        :return:
        """
        urls = []
        page_url = self.GOTVACH_MAIN_PAGE
        if self.args.products:
            product_url = "%20".join(self.args.products)
            for x in range(0, self.dishes_count):
                time.sleep(1)
                page = requests.get(page_url + str(x) + self.SEARCH_BOX + product_url, headers=self.header, timeout=3)
                soup = BeautifulSoup(page.content, "lxml")
                results = soup.find(id="searchRecipes")
                recipes_titles = results.find_all("a", class_="title")
                for title in recipes_titles:
                    link_url = title["href"]
                    urls.append(link_url)
                    if len(urls) == self.dishes_count:
                        break
        self.searched_by_products_urls = urls

    def set_recipes_by_product(self):
        """
        A method which sets the recipes with their id, name, products list and chef information when searched
        by recipe products
        :return:
        """
        i = 0
        try:
            while len(self.recipes) < self.dishes_count:
                url = self.searched_by_products_urls[i]
                products_list = []
                time.sleep(1)
                page = requests.get(url, headers=self.header)
                soup = BeautifulSoup(page.content, "lxml")
                result = soup.find(id="content")

                for j in range(len(result.find("ul"))):
                    new_product = Product(result.find("ul").find_all("li")[j].text)
                    products_list.append(new_product)

                if self.args.agents:
                    self.validate_agents()
                    if self.product_list_contains_agent(products_list):
                        i += 1
                        continue

                recipe_title = result.find_all("h1")[0].text
                new_chef = Chef(url=url, header=self.header)
                recipe = Recipe(recipe_id=i, title=recipe_title, products=products_list, chef=new_chef,
                                recipe_soup=soup)
                self.recipes.append(recipe)
                i += 1
        except IndexError:
            print("No more recipes with these parameters!")

    def _set_searched_by_last_cooked_recipe_urls(self):
        """
        A method which sets the urls of recipes when searched by last cooked
        :return:
        """
        urls = []
        url_last_cooked = self.GOTVACH_MAIN_PAGE
        for x in range(0, self.dishes_count):
            time.sleep(1)
            page = requests.get(url_last_cooked + str(x) + self.L_COOKED_TAG, headers=self.header)
            soup = BeautifulSoup(page.content, "lxml")
            results = soup.find(id="lastCook")
            recipes_titles = results.find_all("a", class_="title")
            for title in recipes_titles:
                link_url = title["href"]
                urls.append(link_url)
        self.searched_by_last_cooked_urls = urls

    def set_recipes_by_last_cooked(self):
        """
        A method which sets the recipes with their id, name, products list and chef information when searched
        by last cooked
        :return:
        """
        i = 0
        try:
            while len(self.recipes) < self.dishes_count:
                url = self.searched_by_last_cooked_urls[i]
                products_list = []
                time.sleep(1)
                page = requests.get(url, headers=self.header)
                soup = BeautifulSoup(page.content, "lxml")
                result = soup.find(id="content")

                for j in range(len(result.find("ul"))):
                    new_product = Product(result.find("ul").find_all("li")[j].text)
                    products_list.append(new_product)

                if self.args.agents:
                    self.validate_agents()
                    if self.product_list_contains_agent(products_list):
                        i += 1
                        continue

                recipe_title = result.find_all("h1")[0].text
                new_chef = Chef(url=url, header=self.header)
                recipe = Recipe(recipe_id=i, title=recipe_title, products=products_list, chef=new_chef,
                                recipe_soup=soup)
                self.recipes.append(recipe)
                i += 1
        except IndexError:
            print("No more recipes with these parameters!")

    def _set_searched_by_recipe_name_urls(self):
        """
        A method which sets the urls of recipes when searched by recipe name
        :return:
        """
        urls = []
        page_url = self.GOTVACH_MAIN_PAGE + self.SEARCH_BOX
        if self.args.dish_name:
            page_url += self.args.dish_name
        for x in range(0, self.dishes_count):
            time.sleep(1)
            page = requests.get(page_url, headers=self.header, timeout=3)
            soup = BeautifulSoup(page.content, "lxml")
            results = soup.find(id="searchRecipes")
            recipes_titles = results.find_all("a", class_="title")
            for title in recipes_titles:
                link_url = title["href"]
                urls.append(link_url)
                if len(urls) == self.dishes_count:
                    break
        self.searched_by_recipe_name_urls = urls

    def set_recipes_by_recipe_name(self):
        """
        A method which sets the recipes with their id, name, products list and chef information when searched
        by recipe name
        :return:
        """
        i = 0
        try:
            while len(self.recipes) < self.dishes_count:
                url = self.searched_by_recipe_name_urls[i]
                products_list = []
                time.sleep(1)
                page = requests.get(url, headers=self.header)
                soup = BeautifulSoup(page.content, "lxml")
                result = soup.find(id="content")
                # print("result1", result)

                for j in range(len(result.find("ul"))):
                    new_product = Product(result.find("ul").find_all("li")[j].text)
                    products_list.append(new_product)

                if self.args.agents:
                    self.validate_agents()
                    if self.product_list_contains_agent(products_list):
                        i += 1
                        continue

                recipe_title = result.find_all("h1")[0].text
                new_chef = Chef(url=url, header=self.header)
                recipe = Recipe(recipe_id=i, title=recipe_title, products=products_list, chef=new_chef,
                                recipe_soup=soup)
                self.recipes.append(recipe)
                i += 1

        except IndexError:
            print("No more recipes with these parameters!")

    def product_list_contains_agent(self, products_list):
        for agent in self.args.agents:
            for product in products_list:
                product = product.title.encode("utf-8")
                if product == agent:
                    return True
        return False

    def validate_agents(self):
        valid_agents = to_string_list(agents_data_list)

        for agent in self.args.agents:
            if agent not in valid_agents:
                self.args.agents.remove(agent)

    def export_to_storage(self, storage):
        for recipe in self.recipes:
            storage.add_recipe(recipe)

    def set_recipes(self):
        if self.args.products:
            self.set_recipes_by_product()
        if self.args.last_cooked:
            self.set_recipes_by_last_cooked()
        if self.args.dish_name:
            self.set_recipes_by_recipe_name()
