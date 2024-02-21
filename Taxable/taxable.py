from abc import ABC, abstractmethod


class Taxable(ABC):

    VAT_PERCENTAGE = 14


    @abstractmethod
    def get_tax(self, amount):
        pass