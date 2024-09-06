class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Value will be the placeholder of all names to be filled
        
        # Checks if name is not none
        if hasattr(self, '_name') and self._name is not None:
            raise Exception('Name cannot be changed once set')
        
        # Checks if name is a string
        if not isinstance(value, str):
            raise Exception('Name must be a string')
        
        # Checks if length of the coffee name is 3 or more 
        if len(value) < 3:
            raise Exception('Name must be at least 3 characters long')
        self._name = value
    
    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception('Name must be a string')
        if not (1<= len(value) <= 15):
            raise Exception('Name must be between 1 to 15 characters long')
        self._name = value
 
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = None
        self.price = price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, amount):
        if hasattr(self, '_price') and self._price is not None:
            raise Exception('Amount cannot be changed once set')
        if not isinstance(amount, float):
            raise Exception('Price must be into float format')
        if not (1.0<= amount <=10.0):
            raise Exception('Number must be between 1.0 and 10.0')
        self._price = amount