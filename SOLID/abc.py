# abc module
import abc

# Make the class abstract
class MyABC(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition"""

    # Abstract method
    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    # Abstract property
    @abc.abstractproperty
    def some_property(self):
        """Required property"""

# Inherit from MyABC
class MyClass(MyABC):
    """Implementation of MyABC"""

    # Standard constructor
    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value

    # Note the property decorator
    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop

a = MyClass(value=42)
print (a.some_property)
a.do_something(value=41)
print(a.some_property)

# Missing implementations
class BadClass(MyABC):
    pass

#
# assert BadClass()
