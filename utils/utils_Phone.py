from utils.utils import *


class Phone(Item):

    def __init__(self, name, price, amount, number_of_sim):
        super().__init__(name, price, amount)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.amount + other.amount
        else:
            raise ValueError('Только объекты класса Phone')
