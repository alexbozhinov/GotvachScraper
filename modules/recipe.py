# coding=utf-8
from chef import Chef


class Recipe:
    """
    A class which stores the data of each recipe - id, title, list of products and chef
    """
    LAST_LIST_ELEMENT_IDX = -1
    TIMES_COOKED_SPAN_IDX = -2

    def __init__(self, recipe_id, title="", products=None, chef=None, recipe_soup=None):
        self.id = recipe_id
        self.title = title
        self.products = products
        self.chef = chef
        self._data = recipe_soup
        self.rating = None
        self.cooked_times = 0
        self.set_recipe_rating()
        self.set_times_cooked()

    def get_data(self):
        return self._data

    def set_recipe_rating(self):
        try:
            self.rating = self._data.find(
                "div", {"class": "lsi"}
            ).find("div").text
        except AttributeError:
            self.rating = "0"

    def set_times_cooked(self):
        try:
            find_stats = self._data.find(
                "div", {"class": "stats soc"}
            ).find("ul").findAll("li", href=False)[self.LAST_LIST_ELEMENT_IDX]
            find_cooked_span = find_stats.findAll("span")[self.TIMES_COOKED_SPAN_IDX].get_text()
            is_cooked = find_cooked_span == "Сготвена"
            self.cooked_times = find_stats.findAll("span")[
                self.LAST_LIST_ELEMENT_IDX].get_text() if is_cooked else self.cooked_times
        except AttributeError:
            self.cooked_times = 0

    def __str__(self):
        return "Recipe {}\ntitle: {}\nproducts: {}\nchef: {}\nrating: {}\tcooked: {}\n".format(self.id,
                                                                                               self.title.encode(
                                                                                                   "utf-8"),
                                                                                               "\n\t".join(
                                                                                                   [product.__str__()
                                                                                                    for product in
                                                                                                    self.products]),
                                                                                               self.chef,
                                                                                               self.rating,
                                                                                               self.cooked_times)
