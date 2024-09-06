
# Coffee Shop System

This repository contains a basic structure  of a coffee shop system using Python classes. My main goal was to use many to many relationships as well as ORM. It includes three main classes:


1. **Coffee**: Represents a type of coffee.
2. **Customer**: Represents a customer who can place orders.
3. **Order**: Represents an order placed by a customer for a specific       coffee.

## Fork and clone

To deploy this project on your local machine

```bash
  fork and clone the repository
  ```
  The overview of the project is laid down below.

## Classes

### Coffee

Represents a coffee with the following attributes and methods:


- **Attributes:**
  - `name`: The name of the coffee (string, 3 or more characters, immutable).
  - `._orders`: List of orders that include this coffee.

- **Methods:**
  - `orders()`: Returns a list of all orders for this coffee.
  - `add_order(order)`: Adds an `Order` instance to the list of orders for this coffee.
  - `customers()`: Returns a unique list of all customers who have ordered this coffee.
  - `num_orders()`: Returns the total number of times this coffee has been ordered.
  - `average_price()`: Returns the average price of orders for this coffee. Returns 0 if no orders exist.


### Customer

Represents a customer with the following attributes and methods:

- **Attributes:**
  - `name`: The name of the customer (string, 1 to 15 characters).
  - `orders`: List of orders placed by the customer.

- **Methods:**
  - `orders()`: Returns a list of all orders placed by this customer.
  - `add_order(order)`: Adds an `Order` instance to the list of orders for this customer.
  - `coffees()`: Returns a unique list of all coffee types ordered by this customer.
  - `create_order(coffee, price)`: Creates and returns an `Order` instance for the specified coffee and price.

### Order

Represents an order with the following attributes and methods:

- **Attributes:**
  - `customer`: The customer who placed the order (must be an instance of `Customer`).
  - `coffee`: The coffee that was ordered (must be an instance of `Coffee`).
  - `price`: The price of the order (float, between 1.0 and 10.0, immutable).

- **Methods:**
  - `price`: Property to get and set the price of the order. Ensures price is between 1.0 and 10.0 and cannot be changed once set.
  - `customer`: Property to get and set the customer who placed the order.
  - `coffee`: Property to get and set the coffee that was ordered.

## Usage

From your VsCode terminal make sure to install:

```sh
pipenv install

pipenv shell

pip install ipdb
```

Here is a brief example of how to use these classes:
```python
import ipdb
from your_module import Coffee, Customer, Order

# Create some coffee types
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create orders
order1 = alice.create_order(latte, 5.0)
order2 = bob.create_order(latte, 7.0)
order3 = alice.create_order(espresso, 4.0)

# Start debugging
ipdb.set_trace()

# Retrieve information
print(latte.orders())  # List of orders for Latte
print(latte.customers())  # List of customers who ordered Latte
print(latte.num_orders())  # Total number of Latte orders
print(latte.average_price())  # Average price of Latte orders

print(Customer.most_aficionado(latte))
```


## Running Tests

To run tests, run the following command

```python
  pytest
  #  or
  pytest -x
```


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- [@NathanMwai](https://github.com/Nathan-Mwai)


## 🛠 Skills
Javascript, HTML, CSS, REACT, PYTHON
# Just another work
# Coffee Shop System

## Class: `Coffee`

| Property / Method     | Type                  | Description |
|-----------------------|-----------------------|-------------|
| `name`                | `str`                  | Coffee name. Read-only once set. Must be at least 3 characters long. |
| `orders()`            | `List[Order]`          | Returns the list of all orders for this coffee. |
| `add_order(order)`    | `Order`                | Adds an order to the coffee's order list. |
| `customers()`         | `List[Customer]`       | Returns a list of unique customers who have ordered this coffee. |
| `num_orders()`        | `int`                  | Returns the total number of orders for this coffee. |
| `average_price()`     | `float`                | Returns the average price of all orders for this coffee. Returns 0 if no orders. |

## Class: `Customer`

| Property / Method              | Type                  | Description |
|--------------------------------|-----------------------|-------------|
| `name`                         | `str`                  | Customer name. Must be between 1 and 15 characters long. |
| `orders()`                     | `List[Order]`          | Returns the list of all orders made by this customer. |
| `add_order(order)`             | `Order`                | Adds an order to the customer's order list. |
| `coffees()`                    | `List[Coffee]`         | Returns a list of unique coffees ordered by the customer. |
| `create_order(coffee, price)`  | `Order`                | Creates a new order for the given coffee and price. |

## Class: `Order`

| Property / Method                         | Type                  | Description |
|-------------------------------------------|-----------------------|-------------|
| `price`                                   | `float`                | The price of the order. Must be between 1.0 and 10.0. |
| `customer`                                | `Customer`             | The customer who made the order. |
| `coffee`                                  | `Coffee`               | The coffee that was ordered. |
| `__init__(customer, coffee, price)`       | `None`                 | Initializes a new order with the given customer, coffee, and price. |
| `all`                                     | `List[Order]`          | Class attribute storing all orders. |

## Method: `Customer.most_aficionado(coffee)`

| Property / Method                         | Type                  | Description |
|-------------------------------------------|-----------------------|-------------|
| `most_aficionado(coffee)`                 | `Customer`            | Returns the customer who has spent the most money on the specified coffee. Returns `None` if no customers have ordered that coffee. |


                            E         N          D          
# Mock Code Challenge - Coffee Shop (Object Relationships)

For this assignment, we'll be working with a Coffee shop-style domain.

We have three models: `Coffee`, `Customer`, and `Order`.

For our purposes, a `Coffee` has many `Order`s, a `Customer` has many `Order`s,
and a `Order` belongs to a `Customer` and to a `Coffee`.

`Coffee` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You can
run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Customer

- `Customer __init__(self, name)`
  - Customer is initialized with a name
- `Customer property name`
  - Returns customer's name
  - Names must be of type `str`
  - Names must be between 1 and 15 characters, inclusive
  - Should **be able** to change after the customer is instantiated

#### Coffee

- `Coffee __init__(self, name)`
  - Coffee is initialized with a name
- `Coffee property name`
  - Returns the coffee's name
  - Names must be of type `str`
  - Names length must be greater or equal to 3 characters
  - Should **not be able** to change after the coffee is instantiated
  - _hint: `hasattr()`_

#### Order

- `Order __init__(self, customer, coffee, price)`
  - Order is initialized with a `Customer` instance, a `Coffee` instance, and a
    price
- `Order property price`
  - Returns the price for the order
  - Prices must be of type `float`
  - Price must be a number between 1.0 and 10.0, inclusive
  - Should **not be able** to change after the order is instantiated
  - _hint: `hasattr()`_

### Object Relationship Methods and Properties

#### Order

- `Order property customer`
  - Returns the customer object for that order
  - Must be of type `Customer`
- `Order property coffee`
  - Returns the coffee object for that order
  - Must be of type `Coffee`

#### Coffee

- `Coffee orders()`
  - Returns a list of all orders for that coffee
  - Orders must be of type `Order`
- `Coffee customers()`
  - Returns a **unique** list of all customers who have ordered a particular
    coffee.
  - Customers must be of type `Customer`

#### Customer

- `Customer orders()`
  - Returns a list of all orders for that customer
  - Orders must be of type `Order`
- `Customer coffees()`
  - Returns a **unique** list of all coffees a customer has ordered
  - Coffees must be of type `Coffee`

### Aggregate and Association Methods

#### Customer

- `Customer create_order(coffee, price)`
  - Receives a **coffee object** and a **price number** as arguments
  - Creates and returns a new Order instance and associates it with that
    customer and the coffee object provided.

#### Coffee

- `Coffee num_orders()`
  - Returns the total number of times a coffee has been ordered
  - Returns `0` if the coffee has never been ordered
- `Coffee average_price()`
  - Returns the average price for a coffee based on its orders
  - Returns `0` if the coffee has never been ordered
  - Reminder: you can calculate the average by adding up all the orders prices
    and dividing by the number of orders

### Bonus: Aggregate and Association Method

- `Customer classmethod most_aficionado(coffee)`
  - Receives a **coffee object** argument
  - Returns the `Customer` instance that has spent the most money on the coffee
    instance provided as argument.
  - Returns `None` if there are no customers for the coffee instance provided.
  - _hint: will need a way to remember all `Customer` objects_
  - Uncomment lines 137-147 in the customer_test file

### Bonus: For any invalid inputs raise an `Exception`.

- First, **comment out** the following lines
  - **customer_test.py**
    - lines 25-26, 40-41, and 44-45
  - **coffee_test.py**
    - lines 34-35
  - **order_test.py**
    - lines 46-47
- Then, **uncomment** the following lines in the test files

  - **customer_test.py**
    - lines 31-32, 48-49, and 52-53
  - **coffee_test.py**
    - lines 22-23, 26-27, and 38-39
  - **order_test.py**
    - lines 32-33, 36-37, and 50-51
