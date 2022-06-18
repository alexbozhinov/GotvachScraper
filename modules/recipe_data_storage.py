from import_google_sheets import *


class RecipeDataStorage:
    """
    A class in where to store all scraped recipes in order to do more actions with them (ex. export to google sheets)
    """

    def __init__(self):
        self.recipe_storage = []

    def add_recipe(self, recipe):
        """
        A method which adds the given recipe into the storage
        :param recipe:
        :return:
        """
        self.recipe_storage.append(recipe)

    def sort_by_recipe_product_count_ascending(self):
        """
        Sorts the recipes by product count - ascending order
        """
        self.recipe_storage = sorted(self.recipe_storage,
                                     key=lambda r: len(r.products),
                                     reverse=False)

    def sort_by_recipe_product_count_descending(self):
        """
        Sorts the recipes by product count - descending order
        """
        self.recipe_storage = sorted(self.recipe_storage,
                                     key=lambda r: len(r.products),
                                     reverse=True)

    def sort_by_most_cooked_ascending(self):
        """
        Sorts the recipes by how many time is cooked - ascending order
        """
        self.recipe_storage = sorted(self.recipe_storage,
                                     key=lambda r: r.set_times_cooked())

    def sort_by_recipe_rating_ascending(self):
        """
        Sorts the recipes by how many time is cooked - ascending order
        """
        self.recipe_storage = sorted(self.recipe_storage,
                                     key=lambda r: r.rating,
                                     reverse=False)

    def sort_by_chef_rating_ascending(self):
        """
        Sorts the recipes by chef rating - ascending order
        """
        self.recipe_storage = sorted(self.recipe_storage,
                                     key=lambda r: r.chef.get_ratings(),
                                     reverse=False)

    def sort_by_title_ascending(self):
        """
        Sorts the recipes by title name - ascending order
        """
        self.recipe_storage = sorted(self.recipe_storage,
                                     key=lambda r: r.title.encode("utf-8"))

    def export_to_google_sheets(self):
        """
        Export all data to Google sheets
        """
        credentials = authorize_to_api(AUTH_SCOPES)
        sheet_id = handle_spreadsheet(credentials)
        for recipe in self.recipe_storage:
            values = handle_values(recipe)
            upload_to_sheets(credentials, sheet_id, values)

    def __str__(self):
        return "Recipes:\n\n{}".format("\n".join([recipe.__str__() for recipe in self.recipe_storage]))
