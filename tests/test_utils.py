from utils.utils import *
import pytest


def test_class_Store():
    n = Store('Телефон', 6000, 1)
    assert n.calculate_total_price() == 6000
    assert n.apply_discount() == 6000
    Store.discount = 0.5
    assert n.apply_discount() == 3000.0
