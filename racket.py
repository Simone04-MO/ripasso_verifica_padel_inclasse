class Racket(object):
    def __init__(self,brand,model,size,weight,quantity,price):
        if not isinstance(brand, str):
            raise TypeError('brand is not a string')
        if not isinstance(model, str):
            raise TypeError('model is not a string')
        if not isinstance(size, str):
            raise TypeError('size is not a string')
        if not isinstance(weight, int):
            raise TypeError('weight is not a int')
        if weight <=0:
            raise ValueError("weight must be positive")
        if not isinstance(quantity, int):
            raise TypeError('quantity is not a int')
        if quantity <0:
            raise ValueError("quantity must be positive or zero")
        if not isinstance(price, float):
            raise TypeError('price is not a float')
        if price <0:
            raise ValueError("price must be positive or zero")
        self._brand = brand
        self._model = model
        self._size = size
        self._weight = weight
        self._quantity = quantity
        self._price = price

    #getters
    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def size(self):
        return self._size

    @property
    def weight(self):
        return self._weight

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price

    #setters
    @quantity.setter
    def quantity(self,new_quantity):
        if not isinstance(new_quantity, int):
            raise TypeError('quantity is not a int')
        if new_quantity < 0:
            raise ValueError("quantity must be positive or zero")
        self._quantity= new_quantity

    @price.setter
    def price(self,new_price):
        if not isinstance(new_price, float):
            raise TypeError('price is not a float')
        if new_price < 0:
            raise ValueError("price must be positive or zero")
        self._price = new_price

    def __str__(self):
        string_to_return=f"brand: {self._brand}\nmodel: {self._model}\nsize: {self._size}\nprice: {self._price}"
        return string_to_return





        

