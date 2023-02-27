import csv


class Store:
    discount = 1  # уровень цен на товары
    all = []

    def __init__(self, name: str, price: int, amount: int):
        self.__name = name
        self.__price = price
        self.__amount = amount
        Store.all.append(self)

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
    def instantiate_from_csv(cls, path: str) -> None:
        """Создаёт новые экзэмпляры из csv файла"""

        with open(path, encoding='UTF-8') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                cls(
                    name=row['name'],
                    price=row['price'],
                    amount=row['quantity']
                )

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
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}', {self.__amount})"

    def __str__(self) -> str:
        return f'{self.__name}'
