from abc import ABC


class Customer(ABC):
    # constructor
    def __init__(self, customer_id, customer_name, phone, customer_address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__phone = phone
        self.__customer_address = customer_address

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_customer_Adress(self):
        return self.__customer_address

    def set_customer_address(self, customer_address):
        self.__customer_address = customer_address

    def get_phone(self):
        return self.__phone
