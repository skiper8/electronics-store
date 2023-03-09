from utils.utils import *


def test_calculate_total_price():
    item = Item('Телефон', 100, 1)
    assert item.calculate_total_price() == 100


def test_apply_discount():
    item = Item('Телефон', 1000, 1)
    item.discount = 0.5
    assert item.apply_discount() == 500.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv('test_items.csv')
    assert len(Item.all) == 5


def test_prop():
    item = Item('Телефон', 100, 1)
    assert len(item.name) < 10
    assert item.name != 'СуперТелефон'
    item.price = 1000
    assert item.price == 1000
    item.amount = 10
    assert item.amount == 10


def test_is_integer():
    item = Item('Телефон', 100, 1)
    assert item.is_integer(1.6) is False
    assert item.is_integer(10) is True

