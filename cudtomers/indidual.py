from cudtomers.customer import Customer


class Individual(Customer):
    def __init__(self, cust_Id, name, address, phone, lic_number):
        Customer.__init__(self, cust_Id, name, address, phone)
        self.__lic_number = lic_number

    def get_lic_number(self):
        return self.__lic_number

    def set_discount(self, lic_number):
        self.__lic_number = lic_number