class GoldenClass:
    def __init__(self):
        self.class_variable = "I am a class variable"
        self._my_property = "I am a property value"
    
    def method_one(self, param1, param2):
        """This is method one"""
        local_variable = "I am a local variable in method one"
        return f"Method one called with {param1} and {param2}"
    
    def method_two(self, param1):
        """This is method two"""
        local_variable = "I am a local variable in method two"
        return f"Method two called with {param1}"
    
    @property
    def my_property(self)-> str:
        """This is a property"""
        return self._my_property
    @my_property.setter
    def my_property(self, value: str)-> None:
        """Setter for my_property"""
        self._my_property = value
    @my_property.deleter
    def my_property(self)-> None:
        """Deleter for my_property"""
        del self._my_property