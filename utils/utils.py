import csv


class Item:
    discount = 1  # уровень цен на товары
    all = []

    def __init__(self, name: str, price: int, amount: int):
        self.__name = name
        self.__price = price
        self.__amount = amount
        Item.all.append(self)

    @property
    def name(self):
        """Возвращает название товра"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Контролирует длину названия товра"""
        if len(value) <= 10:
            self.__name = value
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @classmethod
    def instantiate_from_csv(cls, filename):
        """Создаёт новые экзэмпляры из csv файла"""
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        cls(row['name'], int(row['price']), int(row['quantity']))
                    else:
                        raise IndentationError
        except FileNotFoundError:
            print(f'отстутсвует файл items.csv')
        except IndentationError:
            print('Файл items.csv поврежден')

    @staticmethod
    def is_integer(num) -> bool:

        """Проверяет, является ли число целым"""

        if isinstance(num, int) or isinstance(num, float) and num % 1 == 0:
            return True
        else:
            return False

    def calculate_total_price(self):

        """Подсчитывает общую стоимость всех товаров"""

        self.total_price = self.price * self.amount * self.discount
        return self.total_price

    def apply_discount(self):

        """Подсчитывает стоимость одной еденицы товара с имеюшейся скидкой"""
        return self.price * self.discount

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}', {self.__amount}, {self.number_of_sim})"

    def __str__(self) -> str:
        return f'{self.__name}'


class MixinLog(Item):
    def __init__(self, name, price, amount):
        self.__language = 'EN'
        super().__init__(name, price, amount)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language in 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class KeyBoard(MixinLog, Item):

    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)
