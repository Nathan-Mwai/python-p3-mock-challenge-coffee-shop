class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []
    # This are the initial properties
    
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
        return self._orders
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError('Order must be an instance of Order')
        self._orders.append(order)
    
    def customers(self):
        customers_orders = set()
        # customers_orders = {order.customer for order in self._orders if isinstance(order.customer, Customer)}
        for order in self._orders:
            if isinstance(order.customer, Customer):
                customers_orders.add(order.customer)
        return list(customers_orders)
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        number_of_orders = len(self._orders)
        
        return total_price / number_of_orders

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        
    # This are the initial properties
    @property
    def name(self):
        return self._name
    
    @name.setter
            # Value will be the placeholder of all names to be filled

    def name(self, value):
        if not isinstance(value, str):
            raise Exception('Name must be a string')
        if not (1<= len(value) <= 15):
            raise Exception('Name must be between 1 to 15 characters long')
        self._name = value
 
    def orders(self):
        return self._orders
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError('Order must be an instance of Order')
        self._orders.append(order)
    
    def coffees(self):
        coffee_orders = {order.coffee for order in self._orders if isinstance(order.coffee, Coffee)}
        return list(coffee_orders)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    
    
class Order:
    
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = None
        self.price = price
        # Calling the function here adds order to the list
        coffee.add_order(self)
        customer.add_order(self)
        Order.all.append(self)
        # This are the initial properties
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
    # This where orm is initialized
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, related_to_customer):
        if not isinstance(related_to_customer, Customer):
            raise Exception('Customer must be a customer')
        self._customer = related_to_customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, related_to_coffee):
        if not isinstance(related_to_coffee, Coffee):
            raise Exception('Must be of instance Coffee')
        self._coffee = related_to_coffee