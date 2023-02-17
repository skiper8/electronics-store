class Store:
    discount = 1  # уровень цен на товары
    all = []

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.all += (self, name, price, amount)

    def calculate_total_price(self):
        self.total_price = self.price * self.amount * self.discount
        return self.total_price

    def apply_discount(self):
        return self.price * self.discount
