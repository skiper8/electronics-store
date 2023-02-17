from utils.utils import *

item1 = Store("Смартфон", 10_000, 20)  # экземпляр класса
item2 = Store("Ноутбук", 20_000, 5)  # экземпляр класса

print(item1.calculate_total_price())  # подсчет полной стоимости товара первого экземпляра
print(item2.calculate_total_price())  # подсчет полной стоимости товара второго экземпляра

Store.discount = 0.8  # изменение размера скидки
print(item1.apply_discount()) # подсчет стоимости одного товара в зависимости от скидки
print(item2.apply_discount())  # подсчет стоимости одного товара в зависимости от скидки

print(Store.all)
