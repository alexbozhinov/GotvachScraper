## Code Academy Team 3
### A.Bozhinov, A.Aleksandrova, S.Arabadzhiev


## Project Summary

The main purpose of this project is to develop a web scraper for scraping recipes, store the data in JSON format, manipulate it(search, sort, etc.) and then save it in Google Sheets.

## Requirements for development

This script uses [virtualenv with python2.7]
To run the script successfully you must have first installed everything from requirement.txt file in the current project.

## Overall requirements

Tests, documentation, OOP design

## Technical Details

1. ArgParser implementation - get user input and parse it as an arguments
2. Scraping - get data from https://recepti.gotvach.bg/, the script uses request and Beautiful Soup
3. Data collector implementation - accepts and organize parsed data in JSON format
4. Data sender implementation - provide API to send the data to Google Sheets
5. Tests implementation

## Usage

The script is used to gather data from https://recepti.gotvach.bg/.
You can write the following command in your terminal:
  ```
  python main.py [-h] [-a <allergens>]
                 [-n <number of dishes>] [-l <last cooked>]
                 [-n <number of dishes>] [-p <products>]
                 [-n <number of dishes>] [-d <dish>]
                 [-n <number of dishes>] [-a <allergens> - in progress]
  ```
About the optional arguments:
  * -h,                    show this help message and exit
  * -n <number of dishes>  give number of dishes as an input
  * -a <allergens>         give list of allergens as an input
  * -l <last cooked>       give input search criteria option "last cooked"
  * -p <products>          give a list of products as a search criteria
  * -d <dish>              give a name of a dish as a search criteria  
  ...
  
## _Input example_
_Proper inputs should include:_
- n - number of recipes (required)
- product(s)
- dish name
- last cooked
- allergens 

Example:
```
    python main.py -n <number of dishes> -p <products>
    python main.py -n <number of dishes> -d <dish>
    python main.py -n <number of dishes> -l <last cooked>
    python main.py -a <allergens>
```

## __Project structure__
Project structure :
```
recipes-scraper/
    |--- modules/
        |--- __init__.py
        |--- agents.py
        |--- argparser.py
        |--- chef.py
        |--- product.py
        |--- recipe.py
        |--- recipe_data_storage.py
        |--- scraper.py
    |--- test/
    |--- __init__.py
    |--- .gitignore
    |--- main.py
    |--- README.md
    |--- requirements.txt
```