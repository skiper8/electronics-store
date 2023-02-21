from utils.utils import *

item = Store('Телефон', 10000, 5)
item.name = 'Смартфон'
print(item.name)

item.name = 'СуперСмартфон'

Store.instantiate_from_csv('items.csv')  # создание объектов из данных файла
print(len(Store.all))  # в файле 5 записей с данными по товарам
item1 = Store.all[0]
print(item1.name)

print(Store.is_integer(5))
print(Store.is_integer(5.0))
print(Store.is_integer(5.5))
