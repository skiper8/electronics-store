import csv


class Store:
    discount = 1  # уровень цен на товары
    all = []

    def __init__(self, name: str, price: int, amount: int):
        self.__name = name
        self.price = price
        self.amount = amount
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
            print('Exception: Длина наименования товара превышает 10 символов.')

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

