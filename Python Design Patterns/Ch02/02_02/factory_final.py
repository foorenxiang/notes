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
