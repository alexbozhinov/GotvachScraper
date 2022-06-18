from modules.recipe_data_storage import RecipeDataStorage
from modules.scraper import Scraper
from modules.menu import menu

"""
Scraper, which scrapes the recipes from www.gotvach.bg
Storage, where the scraped recipes are stored
Check scraped recipes by print(storage)
"""


def main():
    scraper = Scraper()
    scraper.set_recipes()
    storage = RecipeDataStorage()
    scraper.export_to_storage(storage)
    menu(storage)


if __name__ == "__main__":
    main()
