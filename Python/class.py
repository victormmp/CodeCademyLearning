"""
LEARNNG CLASSES

As mentioned, you can think of __init__() as the method that "boots up" a class'
instance object: the init bit is short for "initialize."

The first argument __init__() gets is used to refer to the instance object, and
by convention, that argument is called self. If you add additional arguments—for
instance, a name and age for your animal—setting each of those equal to self.name
and self.age in the body of __init__() will make it so that when you create an
instance object of your Animal class, you need to give each instance
a name and an age, and those will be associated with the particular instance
you create.

SCOPE
Another important aspect of Python classes is scope. The scope of a variable is
the context in which it's visible to the program.

It may surprise you to learn that not all variables are accessible to all parts
of a Python program at all times. When dealing with classes, you can have
variables that are available everywhere (global variables), variables that are
only available to members of a certain class (member variables), and variables
that are only available to particular instances of a class (instance variables).

The same goes for functions: some are available everywhere, some are only
available to members of a certain class, and still others are only available to
particular instance objects.
"""

# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    is_alive = True
    def __init__(self, name, age, hungry):
        self.name = name
        self.age = age
        self.is_hungry = hungry

    def description(self):
        """description of the animal"""
        print self.name
        print self.age

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
hippo = Animal("Joe", 12, False)

print zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_hungry, giraffe.is_alive
print panda.name, panda.age, panda.is_hungry, panda.is_alive

hippo.description()

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
my_cart = ShoppingCart("Joe")
my_cart.add_item("Viagra", 10)

"""
INHERITANCE

Inheritance is the process by which one class takes on the attributes and
methods of another, and it's used to express an is-a relationship. For example,
a Panda is a bear, so a Panda class could inherit from a Bear class. However, a
Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if
 they have a lot of attributes and methods in common). Instead, both Toyota and
 Tractor could ultimately inherit from the same Vehicle class.
"""
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#Another example of inherited class
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

"""
OVERRIDE

Sometimes you'll want one class that inherits from another to not only take on
the methods and attributes of its parent, but to override one or more of them.
"""

"""
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name

class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
"""

"""
Rather than have a separate greet_underling method for our CEO, we override (or
re-create) the greet method on top of the base Employee.greet method. This way,
we don't need to know what type of Employee we have before we greet another
Employee.

On the flip side, sometimes you'll be working with a derived class (or subclass)
and realize that you've overwritten a method or attribute defined in that class'
base class (also called a parent or superclass) that you actually need. Have no
fear! You can directly access the attributes or methods of a superclass with
Python's built-in super call.
"""
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours*12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")

print milton.full_time_wage(10)

"""
REPRESENTATIONS

One useful class method to override is the built-in __repr__() method, which is
short for representation; by providing a return value in this method, we can
tell Python how to represent an object of our class (for instance, when using a
print statement).
"""
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)

print my_point
