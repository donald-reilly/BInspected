from types import ModuleType, MethodType, FunctionType
class Classifier:
    def __init__(self):
        pass
    def classify_initial_object(self, object_to_classify: ModuleType | type | MethodType | FunctionType | property) -> str:
        """
        Classifies objects and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            object_to_classify: Object to be classified.
        return:
            dictionary representation of the classification of the provided object and all of it's attributes.
        """

        if isinstance(object_to_classify, ModuleType):
            return "object is a module"
        if isinstance(object_to_classify, type):
            return "object is a class"
        if isinstance(object_to_classify, MethodType):
            return "object is a method"
        if isinstance(object_to_classify, FunctionType):
            return "object is a function"
        if isinstance(object_to_classify, property):
            return "object is a property"
        return "object is an instance of a user-defined class"
    def classify_module(self, module_to_classify: ModuleType)-> dict:
        """
        Classifies modules and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            module_to_classify: Module to be classified.
        return:
            dictionary representation of the classification of the provided module and all of it's attributes.
        """

        return {}
    def classify_class(self, class_to_classify: type)-> dict:
        """
        Classifies classes and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            class_to_classify: Class to be classified.
        return:
            dictionary representation of the classification of the provided class and all of it's attributes.
        """

        return {}
    def classify_method(self, method_to_classify: MethodType)-> dict:
        """
        Classifies methods and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            method_to_classify: Method to be classified.
        return:
            dictionary representation of the classification of the provided method and all of it's attributes.
        """

        return {}
    def classify_function(self, function_to_classify: FunctionType)-> dict:
        """
        Classifies functions and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            function_to_classify: Function to be classified.
        return:
            dictionary representation of the classification of the provided function and all of it's attributes.
        """
        
        return {}
    def classify_property(self, property_to_classify: property)-> dict:
        """
        Classifies properties and all of it's attributes and returns a dictionary representation of the classification.

        params:
            property_to_classify: Property to be classified.
        return:
            dictionary representation of the classification of the provided property and all of it's attributes.
        """
        
        return {}
    