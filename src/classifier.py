from types import ModuleType, MethodType, FunctionType
class Classifier:
    #TODO: Ok got a good start for the day. Tomorrow finish this out and just move on to the parser.
    #TODO: change returns to strs of the type. Super simple. 

    def __init__(self):
        pass
    def classify_initial_object(self, object_to_classify: ModuleType | type | MethodType | FunctionType | property) -> dict:
        """
        Classifies objects and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            object_to_classify: Object to be classified.
        return:
            dictionary representation of the classification of the provided object and all of it's attributes.
        """

        if isinstance(object_to_classify, ModuleType):
            return self.classify_module(object_to_classify)
        if isinstance(object_to_classify, type):
            return self.classify_class(object_to_classify)
        if isinstance(object_to_classify, MethodType):
            return self.classify_method(object_to_classify)
        if isinstance(object_to_classify, FunctionType):
            return self.classify_function(object_to_classify)
        if isinstance(object_to_classify, property):
            return self.classify_property(object_to_classify)
        return self.classify_instance_of_user_defined_class(object_to_classify)
    def classify_module(self, module_to_classify: ModuleType)-> dict:
        """
        Classifies modules and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            module_to_classify: Module to be classified.
        return:
            dictionary representation of the classification of the provided module and all of it's attributes.
        """

        return {"Name": module_to_classify.__name__, "Type": "Module"}
    
    def classify_instance_of_user_defined_class(self, instance_to_classify: object)-> dict:
        """
        Classifies instances of user-defined classes and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            instance_to_classify: Instance of a user-defined class to be classified.
        return:
            dictionary representation of the classification of the provided instance of a user-defined class and all of it's attributes.
        """
        
        return {"Name": instance_to_classify.__class__.__name__, "Type": "Instance of User Defined Class"}
    def classify_class(self, class_to_classify: type)-> dict:
        """
        Classifies classes and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            class_to_classify: Class to be classified.
        return:
            dictionary representation of the classification of the provided class and all of it's attributes.
        """

        return {"Name": class_to_classify.__name__, "Type": "Class"}
    def classify_method(self, method_to_classify: MethodType)-> dict:
        """
        Classifies methods and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            method_to_classify: Method to be classified.
        return:
            dictionary representation of the classification of the provided method and all of it's attributes.
        """

        return {"Name": method_to_classify.__name__, "Type": "Method"}
    def classify_function(self, function_to_classify: FunctionType)-> dict:
        """
        Classifies functions and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            function_to_classify: Function to be classified.
        return:
            dictionary representation of the classification of the provided function and all of it's attributes.
        """
        
        return {"Name": function_to_classify.__name__, "Type": "Function"}
    def classify_property(self, property_to_classify: property)-> dict:
        """
        Classifies properties and all of it's attributes and returns a dictionary representation of the classification.

        params:
            property_to_classify: Property to be classified.
        return:
            dictionary representation of the classification of the provided property and all of it's attributes.
        """
        
        return {"Name": property_to_classify.__name__, "Type": "Property"}
    