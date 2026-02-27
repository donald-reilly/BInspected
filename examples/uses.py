from pathlib import Path
import json

from binspected import BInspected
import binspected

class DescriptorExample:
    """Simple descriptor to test descriptor behavior."""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return f"Descriptor __get__ called on {instance} for {self.name}"

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class GoldenBase:
    """Base class to test inheritance."""
    base_class_variable = 42

    def base_method(self):
        return "Base method called"


class GoldenClass(GoldenBase):
    """A fully loaded class for introspection testing."""

    # Class variables
    class_variable = "I am a class variable"
    another_class_variable: int = 123

    # Descriptor
    descriptor_field = DescriptorExample("descriptor_field")

    # Nested class
    class Nested:
        """Nested class inside GoldenClass."""
        nested_var = "I am nested"

        def nested_method(self):
            return "Nested method called"

    def __init__(self, x: int = 5, y: str = "hello", *args, **kwargs):
        self.instance_var = "I am an instance variable"
        self._private_var = "I am private"
        self.x = x
        self.y = y
        self.args = args
        self.kwargs = kwargs

    # Regular method
    def method_one(self, param1, param2: int = 10) -> str:
        """This is method one"""
        local_variable = "I am a local variable in method one"
        return f"Method one called with {param1} and {param2}"

    # Method with *args, **kwargs, keyword-only args
    def method_two(self, a, b=3, *args, c, d=4, **kwargs):
        """Method with complex signature"""
        local_variable = "Local var in method two"
        return a, b, c, d, args, kwargs

    # Static method
    @staticmethod
    def static_method(alpha: float = 1.5):
        """Static method example"""
        return alpha * 2

    # Class method
    @classmethod
    def class_method(cls, name: str):
        """Class method example"""
        return f"Called on {cls.__name__} with {name}"

    # Property with getter, setter, deleter
    @property
    def my_property(self) -> str:
        """This is a property"""
        some_local_variable = "Local var in getter"
        return self._private_var

    @my_property.setter
    def my_property(self, value: str = "that", other_value: str = "this", *, x, y) -> None:
        """Setter for my_property"""
        some_local_variable = "Local var in setter"
        self._private_var = value

    @my_property.deleter
    def my_property(self) -> None:
        """Deleter for my_property"""
        del self._private_var

    # Method referencing nested class
    def create_nested(self):
        """Returns an instance of the nested class."""
        return self.Nested()

    # Method returning a lambda (tests function parsing)
    def lambda_factory(self):
        """Returns a lambda function."""
        return lambda z: z * 2


def save_inspection(data, filename="test_inspections/inspection_output.json"):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default= str)
    return path

inspector = BInspected()
test_class = GoldenClass()

save_inspection(inspector(binspected), "examples/GoldenClassInstanceMethodOne.json")
