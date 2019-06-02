
class Good:
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, count):
        self.__count = count

    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count
    
    def __str__(self):
        return f'商品: {self.name}'
