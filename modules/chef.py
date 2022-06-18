# coding=utf-8
import requests
from bs4 import BeautifulSoup


class Chef:
    """
    A class which stores the data of scraped recipe's chef
    """

    def __init__(self, url, header):
        self.url = url
        self.header = header
        self.name = ""
        self.hats = 0
        self.hearts = 0
        self.plates = 0
        self._set_name()
        self._set_hats()
        self._set_hearts()
        self._set_plates()

    def _set_name(self):
        """
        A method which returns the name of the chef from the recipe of the given url
        :return: name
        """
        page = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(page.content, "lxml")
        name = soup.find("div", {"class": "aub"}).select_one("a", href=False).text
        self.name = name

    def _set_hats(self):
        """
        A method which returns the hats (as text) of the chef from the recipe of the given url
        :return: hats
        """
        page = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(page.content, "lxml")
        hats = soup.find("div", {"class": "aub"}).select_one('span.icb-hat').text
        self.hats = self._to_number(hats)

    def _set_hearts(self):
        """
        A method which returns the hearts (as text) of the chef from the recipe of the given url
        :return: hats
        """
        page = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(page.content, "lxml")
        hearts = soup.find("div", {"class": "aub"}).select_one('span.icb-hrt').text
        self.hearts = self._to_number(hearts)

    def _set_plates(self):
        """
        A method which returns the plates (as text) of the chef from the recipe of the given url
        :return: hats
        """
        page = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(page.content, "lxml")
        plates = soup.find("div", {"class": "aub"}).select_one('span.icb-plt').text
        self.plates = self._to_number(plates)

    @staticmethod
    def _to_number(str_value):
        """
        A static method which transforms the given text variable into float number
        :param str_value:
        :return: in_number
        """
        in_number = float("".join(number for number in str_value if number.isdigit()))
        if u"k" in str_value:
            in_number *= 1000
        return in_number

    def get_ratings(self):
        """
        A method which calculates the rating of the chef, based on the values of it's hats, hearts and plates
        :return:
        """
        return (self.hats + self.hearts + self.plates) // 3

    def __eq__(self, other):
        return self.get_ratings() == other.get_ratings()

    def __lt__(self, other):
        return self.get_ratings() < other.get_ratings()

    def __gt__(self, other):
        return self.get_ratings() > other.get_ratings()

    def __str__(self):
        return "name: {}\nhats: {}\thearts: {}\tplates: {}\nRating: {}".format(self.name.encode("utf-8"),
                                                                               self.hats, self.hearts, self.plates,
                                                                               self.get_ratings())
