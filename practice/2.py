class Menu:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, sale):
        self.price = (self.price/100) * (100 - sale)

    def decrease_stock(self, stock):
        self.stock = stock

apple = Menu('apple', 1000, 10)
banana = Menu('banana', 2000, 15)

apple.apply_discount(80)
banana.decrease_stock(5)

print(apple.name, apple.price, apple.stock)
print(banana.name, banana.price, banana.stock)