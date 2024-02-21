from products.product import Product


class Manual(Product):
    def __init__(self, product_id, product_name,retail_price , description, publisher):
        Product.__init__(self, product_id, product_name, retail_price, description)
        self.__publisher = publisher

    def get_publisher(self):
        return self.__publisher