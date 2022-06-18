# -*- coding: utf-8 -*-
from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from sys import argv


class ArgParser:
    """
    The parser of the user input
    """

    def __init__(self):
        self.parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
        self.add_arguments()
        self.args = self.parser.parse_args()
        self.n_dishes = 0
        self.products = None
        self.last_cooked = None
        self.dish_name = None
        self.agents = None
        self._set_dishes_number()
        self._set_products()
        self._set_last_cooked()
        self._set_dish_name()
        self._set_agents()

    def add_arguments(self):
        """
        A method where the possible user arguments are added.
        :return:
        """

        self.parser.add_argument("-n", "--number", type=int, help="store number of recipes", required=True)
        self.parser.add_argument("-l", "--last_cooked", action="store_true", help="choose from last cooked recipes")
        self.parser.add_argument("-p", "--products", type=str, nargs="+", help="choose particular product")
        self.parser.add_argument("-d", "--dish_name", type=str, help="store the name of the dish")
        self.parser.add_argument("-a", "--agents", type=str, nargs="+", help="store the name of the agents")

    def _set_dishes_number(self):
        self.n_dishes = abs(self.args.number)

    def _set_products(self):
        self.products = self.args.products

    def _set_last_cooked(self):
        self.last_cooked = self.args.last_cooked

    def _set_dish_name(self):
        self.dish_name = self.args.dish_name

    def _set_agents(self):
        self.agents = self.args.agents

