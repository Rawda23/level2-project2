from abc import ABC


class Product(ABC):
    def __init__(self, product_id, product_name, retail_price, description):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__retail_price = retail_price
        self.__description = description


    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_product_name(self):
        return self.__product_name

    def get_description(self):
        return self.__description

    def get_product_retail_price(self):
        return self.__retail_price