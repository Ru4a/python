class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def set_price(self, price):
        self.price = price

    def set_stock(self, stock):
        self.stock = stock

    def display_info(self):
        print("Product name : ",self.name)
        print("Price : ", self.price)
        print("Stock : ",self.stock)

product1 = Product("Apple", 1000, 10)
product1.display_info()

product1.set_price(2000)
product1.set_stock(2)

product1.display_info()