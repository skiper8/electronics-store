from utils.utils import *


class Test_Item():

    def test_calculate_total_price(self):
        item = Item('Телефон', 100, 1)
        assert item.calculate_total_price() == 100

    def test_apply_discount(self):
        item = Item('Телефон', 1000, 1)
        item.discount = 0.5
        assert item.apply_discount() == 500.0

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv('items.csv')
        assert len(Item.all) == 2

    def test_prop(self):
        item = Item('Телефон', 100, 1)
        assert len(item.name) < 10
        assert item.name != 'СуперТелефон'
        item.price = 1000
        assert item.price == 1000
        item.amount = 10
        assert item.amount == 10

    def test_is_integer(self):
        item = Item('Телефон', 100, 1)
        assert item.is_integer(1.6) is False
        assert item.is_integer(10) is True


