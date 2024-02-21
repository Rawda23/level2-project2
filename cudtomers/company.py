from cudtomers.customer import Customer


class Company(Customer):
    def __init__(self, cust_Id, name, address, phone, contact, discount):
        Customer.__init__(self, cust_Id, name, address, phone)
        self.__contact = contact
        self.__discount = discount

    def get_contact(self):
        return self.__contact

    def get_discount(self):
        return self.__discount

    def set_contact(self, contact):
        self.__contact = contact

    def set_discount(self, discount):
        self.__discount = discount
