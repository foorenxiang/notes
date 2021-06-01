## **Design Pattern Notes from [Linkedin Learning](https://www.linkedin.com/learning/python-design-patterns)**

# Creational Patterns

## Factory

### Problem:

1. Uncertainties in types of objects
2. Decisions on what classes to be used can only be made at runtime

```python
class Dog:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):

    """The factory method"""
    """Document the classes created that this factory method can use to instantiate new objects"""
    """To create a new object, just call this pattern and pass in the desired class as its input argument"""

    """this dict constructor is used to keep a manifest of classes and its desired constructors that can be accessed"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


""" Call the factory method to create new objects"""
d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())
```

# Abstract Factory

### Problem:

1. User expectation yields **multiple**, related objects

### Solution:

1. Abstract factory e.g. pet factory
2. Concrete factory e.g. dog factory and cat factory
3. Abstract product
4. Concrete product: dog and dog food; cat and cat food

```python
class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """PetStore houses our Abstract Factory"""
    """Used to invoke methods in the concrete factory that is passed into this abstract factory's constructor"""
    """Essentially acting as an interface"""

    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects retured by the DogFactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show the details of our pet
shop.show_pet()

```

## Singleton

### Problem:

1. Only one instance to be instantiated form a class
2. Create global variable in an objected-oriented way using a singleton

### Solution:

1. Module
   1. Shared by multiple objects
2. Borg design pattern

```python
class Borg:
    """The Borg pattern makes the class attributes global"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""

    # This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(
            kwargs
        )  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary for printing


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)

```

## Builder

### Problem:

1. Excessive number of constructors

### Solution:

1. Director
2. Abstract Builder: interfaces
3. Concrete Builder: implements the interfaces
4. Product: object being built

```python
class Director:
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)

```

##

### Problem:

1. Creating many identical objects individually becomes expensive
2. Cloning could be a good alternative to creating individual objects one at a time

### Solution:

1. Creating a prototypical **instance** first
2. Simply clone the prototypical instance whenever a replica is needed

```python
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register object to be cloned"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)

c1 = prototype.clone("skylark")

print(c1)

```

# Structural Patterns

## Decorator

### Problem:

1. Need to add new features to existing object

### Solution:

1. Functions, use built-in decorator feature

```python
from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply the decorator here!
@make_blink
def hello_world():
    """Original function!"""

    return "Hello, World!"


# Check the result of decorating
print(hello_world())

# Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)

```

## Proxy

### Problem:

1. Postpone object creation until absolutely necessary
2. Find a placeholder

### Solution:

1. Clients: interacting with a proxy
2. Proxy: responsible for creating the resource intensive objects

```python
import time


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """ "Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available ...")

        if self.occupied == "No":
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # Make the prodcuer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = "Yes"

# Make the Producer produce
p.produce()

```

## Adapter

### Problem:

1. Incompatible interfaces

### Solution:

1. Translation between interfaces

```python
class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:****
    """English speaker"""

    def __init__(self):
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        # For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))


for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))

```

## Composite

### Problem:

1. Recursive tree data structure
   1. e.g. Menu > Sub-menu > Sub-Sub-menu

### Solution:

1. Component
2. Child (inherits from component class)
3. Composite (inherits from component class)
   1. Maintains child component classes by adding them to a tree data structure

```python
class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):  # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here!
        print("{}".format(self.name))


class Composite(Component):  # Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the composite object
        self.name = args[0]

        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):

        # Print the name of the composite object
        print("{}".format(self.name))

        # Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()


# Build a composite submenu 1
sub1 = Composite("submenu1")

# Create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")
# Create a new Child sub_submenu 12
sub12 = Child("sub_submenu 12")

# Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
# Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite("top_menu")

# Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

# Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

# Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

# Let's test if our Composite pattern works!
top.component_function()

```

## Bridge

### Problem:

1. Two unrelated, parallel or orthogonal abstractions
2. One is implementation specific
3. The other is implementation-independent

### Solution:

1. Separate the abstractions into two different class hierarchies

```python
class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class Circle(object):
    """Implementation-independent abstraction: for example, there could be a rectangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent


# Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Draw a circle
circle1.draw()

# Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# Draw a circle
circle2.draw()

```

# Behavioral Patterns

## Observer

### Problem:

### Solution:

```python
class Subject(object):  # Represents what is being 'observed'
    def __init__(self):
        self._observers = (
            []
        )  # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if (
            observer not in self._observers
        ):  # If the observer is not already in the observers list
            self._observers.append(observer)  # append the observer to the list

    def detach(self, observer):  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all the observers in the list
            if (
                modifier != observer
            ):  # Don't notify the observer who is actually updating the temperature
                observer.update(self)  # Alert the observers!


class Core(Subject):  # Inherits from the Subject class
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # Set the name of the core
        self._temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()  # Notify the observers whenever somebody changes the core temperature


class TempViewer:
    def update(
        self, subject
    ):  # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print(
            "Temperature Viewer: {} has Temperature {}".format(
                subject._name, subject._temp
            )
        )


# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90

```

## Visitor

### Problem:

### Solution:

```python
class House(object):  # The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        visitor.visit(self)  # Triggers the visiting operation!

    def work_on_hvac(self, hvac_specialist):
        print(
            self, "worked on by", hvac_specialist
        )  # Note that we now have a reference to the HVAC specialist object in the house object!

    def work_on_electricity(self, electrician):
        print(
            self, "worked on by", electrician
        )  # Note that we now have a reference to the electrician object in the house object!

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""

    def __str__(self):
        """Simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        house.work_on_hvac(
            self
        )  # Note that the visitor now has a reference to the house object


class Electrician(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: electrician"""

    def visit(self, house):
        house.work_on_electricity(
            self
        )  # Note that the visitor now has a reference to the house object


# Create an HVAC specialist
hv = HvacSpecialist()
# Create an electrician
e = Electrician()

# Create a house
home = House()

# Let the house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)

# Let the house accept the electrician and work on the house by invoking the visit() method
home.accept(e)

```

## Iterator

### Problem:

### Solution:

```python
def count_to(count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:

        # Returns a 'generator' containing numbers in German
        yield number


# Let's test the generator returned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))

```

## Strategy

### Problem:

### Solution:

```python
import types  # Import the types module


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(
        self,
    ):  # This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()

```

## Chain of responsibility

### Problem:

### Solution:

```python
class Handler:  # Abstract handler
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")


class ConcreteHandler1(Handler):  # Inherits from the abstract handler
    """Concrete handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:  # Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True  # Indicates that the request has been handled


class DefaultHandler(Handler):  # Inherits from the abstract handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""
        # No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True  # Indicates that the request has been handled


class Client:  # Using handlers
    def __init__(self):
        self.handler = ConcreteHandler1(
            DefaultHandler(None)
        )  # Create handlers and use them in a sequence you want
        # Note that the default handler has no successor

    def delegate(
        self, requests
    ):  # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)

```

# Design Best Practices

# Consistency

# Other qualities

## **Advanced Design Pattern Notes from [Linkedin Learning](https://www.linkedin.com/learning/python-advanced-design-patterns)**

## Facade

### Problem:

### Solution:

```python
class SubsystemA:

	def method1(self):
		print('SubsystemA method1 ...')

	def method2(self):
		print('SubsystemA method2 ...')

class SubsystemB:

	def method1(self):
		print('SubsystemB method1 ...')

	def method2(self):
		print('SubsystemB method2 ...')

class Facade:

	def __init__(self):
		self._subsystem_A = SubsystemA()
		self._subsystem_B = SubsystemB()

	def method(self):
		self._subsystem_A.method1()
		self._subsystem_A.method2()

		self._subsystem_B.method1()
		self._subsystem_B.method2()

def main():
	facade = Facade()
	facade.method()

if __name__ == "__main__":
	main()

```

## Command

### Problem:

### Solution:

```python
class Command:
	def execute(self):
		pass

class Copy(Command):
	def execute(self):
		print("Copying ...")

class Paste(Command):
	def execute(self):
		print("Pasting ...")

class Save(Command):
	def execute(self):
		print("Saving ...")

class Macro:
	def __init__(self):
		self.commands = []

	def add(self, command):
		self.commands.append(command)

	def run(self):
		for o in self.commands:
			o.execute()

def main():
	macro = Macro()
	macro.add(Copy())
	macro.add(Paste())
	macro.add(Save())
	macro.run()

if __name__ == "__main__":
	main()

```

## Interpreter

### Problem:

### Solution:

```python
from abc import ABC, abstractmethod

class AbstractExpression():

	@abstractmethod
	def interpret(self):
		pass

class NonterminalExpression(AbstractExpression):

	def __init__(self, expression):
		self._expression = expression

	def interpret(self):
		print("Non-terminal expression being interpreted ...")
		self._expression.interpret()

class TerminalExpression(AbstractExpression):

	def interpret(self):
		print("Terminal expression being interpreted ...")

def main():

	ast = NonterminalExpression(NonterminalExpression(TerminalExpression()))
	ast.interpret()

if __name__ == "__main__":
	main()

```

## Mediator

### Problem:

### Solution:

```python
import sys

class Colleague(object):
	def __init__(self, mediator, id):
		self._mediator = mediator
		self._id = id

	def getID(self):
		return self._id

	def send(self, msg):
		pass

	def receive(self, msg):
		pass

class ConcreteColleague(Colleague):
	def __init__(self, mediator, id):
		super().__init__(mediator, id)

	def send(self, msg):
		print("Message '" + msg + "' sent by Colleague " + str(self._id))
		self._mediator.distribute(self, msg)

	def receive(self, msg):
		print("Message '" + msg + "' received by Colleague " + str(self._id))


class Mediator:
	def add(self, colleague):
		pass

	def distribute(self, sender, msg):
		pass

class ConcreteMediator(Mediator):
	def __init__(self):
		Mediator.__init__(self)
		self._colleague = []

	def add(self, colleague):
		self._colleague.append(colleague)

	def distribute(self, sender, msg):
		for colleague in self._colleague:
			if colleague.getID() != sender.getID():
				colleague.receive(msg)


def main():
	mediator = ConcreteMediator()

	c1 = ConcreteColleague(mediator, 1)
	c2 = ConcreteColleague(mediator, 2)
	c3 = ConcreteColleague(mediator, 3)

	mediator.add(c1)
	mediator.add(c2)
	mediator.add(c3)

	c1.send("Good Morning!")

if __name__ == "__main__":
	main()

```

## Memento

### Problem:

### Solution:

```python
import pickle

class Originator:

	def __init__(self):
		self._state = None

	def create_memento(self):
		return pickle.dumps(vars(self))

	def set_memento(self, memento):
		previous_state = pickle.loads(memento)
		vars(self).clear
		vars(self).update(previous_state)

def main():
	originator = Originator()

	print(vars(originator))

	memento = originator.create_memento()

	originator._state = True

	print(vars(originator))

	originator.set_memento(memento)

	print(vars(originator))

if __name__ == "__main__":
	main()

```

## State

### Problem:

### Solution:

```python
class AtmState():

	name = "state"
	allowed = []

	def goNext(self, state):
		if state.name in self.allowed:
			print("Current State: ", self, " switched to: ", state.name)
			self.__class__ = state

		else:
			print("Current State: ", self, " switching to: ", state.name, " not possible!")

	def __str__(self):
		return self.name

class Off(AtmState):

	name = "off"
	allowed = ['on']

class On(AtmState):

	name = "on"
	allowed = ['off']

class ATM():

	def __init__(self):
		self.current = Off()

	def setState(self, state):
		self.current.goNext(state)

def main():
	atm = ATM()

	atm.setState(On)
	atm.setState(Off)
	atm.setState(Off)

if __name__ == "__main__":
	main()


```

## Template

### Problem:

### Solution:

```python
import sys

from abc import ABC, abstractmethod

class AbstractClass(ABC):
#This class inherit from Abstract Base Class to allow the use of the @abstractmethod decorator

	def template_method(self):
		"""Ths is the template method that contains a collection of
		methods to stay the same, to be overriden, and to be overriden optionally.
		"""

		self.__always_do_this()
		self.do_step_1()
		self.do_step_2()
		self.do_this_or()

	def __always_do_this(self):
		#This is a protected method that should not be overriden.

		name = sys._getframe().f_code.co_name
		print('{}.{}'.format(self.__class__.__name__, name))

	@abstractmethod
	def do_step_1(self):
		#This method should be overriden
		pass

	@abstractmethod
	def do_step_2(self):
		#This method should be overriden
		pass

	def do_this_or(self):
		print('You can overide me but you do not have to')

class ConcreteClassA(AbstractClass):
#This class inherits from the Abstract class featuring the template method.

	def do_step_1(self):
		print('Doing step 1 for ConcreteClassA ...')

	def do_step_2(self):
		print('Doing step 2 for ConcreteClassA ...')

class ConcreteClassB(AbstractClass):
#This class inherits from the Abstract class featuring the template method.

	def do_step_1(self):
		print('Doing step 1 for ConcreteClassB ...')

	def do_step_2(self):
		print('Doing step 2 for ConcreteClassB ...')

	def do_this_or(self):
		print('Doing my own business ...')

def main():
	print('==ConcreteClassA==')
	a = ConcreteClassA()
	a.template_method()

	print('==ConcreteClassB==')
	b = ConcreteClassB()
	b.template_method()

if __name__ == '__main__':
	main()

```
