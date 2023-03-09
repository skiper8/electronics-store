from utils.utils import *
from utils.utils_Phone import *

# item = Item('Телефон', 10000, 5)
# item.name = 'Смартфон'
# print(item.name)

# item.name = 'СуперСмартфон'

Item.instantiate_from_csv('items.csv')  # создание объектов из данных файла
print(len(Item.all))  # в файле 5 записей с данными по товарам
item1 = Item.all[0]
print(item1.name)

print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))

phone1 = Phone("iPhone 14", 120_000, 5, 2)
print(phone1)
print(repr(phone1))
phone1.number_of_sim = 0

