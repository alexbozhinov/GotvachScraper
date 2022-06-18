from recipe_data_storage import RecipeDataStorage
from import_google_sheets import *


def menu(storage):
    print("Sort Options:\n")

    sort_type = -1

    while sort_type != 0:
        sort_type = int(input("Recipe rating ascending - 1\nProduct count ascending - 2\nProduct count descending - 3\n"
                              "Chef rating ascending - 4\n"
                              "Most cooked ascending - 5\nTitle ascending - 6\nExport to google sheets - 7\n"
                              "Exit - 0\n"))
        if sort_type == 1:
            storage.sort_by_recipe_rating_ascending()
            print(storage)

        elif sort_type == 2:
            storage.sort_by_recipe_product_count_ascending()
            print(storage)

        elif sort_type == 3:
            storage.sort_by_recipe_product_count_descending()
            print(storage)

        elif sort_type == 4:
            storage.sort_by_chef_rating_ascending()
            print(storage)

        elif sort_type == 5:
            storage.sort_by_most_cooked_ascending()
            print(storage)

        elif sort_type == 6:
            storage.sort_by_title_ascending()
            print(storage)

        elif sort_type == 7:
            storage.export_to_google_sheets()

        elif sort_type == 0:
            break

        else:
            print("Incorrect option!")
