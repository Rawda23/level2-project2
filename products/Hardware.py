from Taxable.taxable import Taxable
from products.product import Product


class Hardware(Product, Taxable):

    def __init__(self,  product_id, product_name,retail_price, description, warranty_period):
        super().__init__(product_id, product_name, retail_price, description)
        self.__warranty_period = warranty_period

    def get_warranty_period(self):
        return self.__warranty_period

    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period



    def get_tax(self, amount):
        return amount * Taxable.VAT_PERCENTAGE / 100