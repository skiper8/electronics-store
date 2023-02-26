from utils.utils import *


def test_Store():
    item = Store('Телефон', 100, 1)
    assert item.calculate_total_price() == 100
    assert item.apply_discount() == 100
    assert item.name != 'СуперТелефон'
    item.price = 1000
    assert item.price == 1000
    item.amount = 10
    assert item.amount == 10
    Store.instantiate_from_csv('test_items.csv')
    assert len(Store.all) == 6
    assert item.is_integer(1.6) == False
    assert item.is_integer(10) == True