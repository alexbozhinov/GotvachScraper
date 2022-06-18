class Product:
    """
    A class which stores the information of a product - it's name, and it's quantity as separated strings
    """

    def __init__(self, product_full):
        self.product_sublist = product_full.split(" - ")
        self.title = "".join(self.product_sublist[0])
        self.quantity = ", ".join(self.product_sublist[1:])

    def quantity_to_number(self):
        pass

    def __str__(self):
        return "title: {}, quantity: {}".format(self.title.encode("utf-8"),
                                                self.quantity.encode("utf-8"))
