from types import ModuleType, MethodType, FunctionType, BuiltinFunctionType, BuiltinMethodType
class Classifier:
    #TODO: For now i'm going to keep this too expanded class. Just incase I want to expand on this later. Gonna seem like a waste for now.
    #TODO: Need to figure out the whole instance thing and how to actaully handle the __dict__ of some objects. it's a problem that i just passed over for now.
    def __init__(self):
        pass
    def __call__(self, object_to_classify)-> str:
        """
        Calls the classifier on an object and returns a string representation of the classification.

        params:
            object_to_classify: Object to be classified.
        return:
            string representation of the classification of the provided object.
        """
        return self.classify_initial_object(object_to_classify)
    def classify_initial_object(self, object_to_classify: ModuleType | type | MethodType | FunctionType | property)-> str:
        """
        Classifies objects and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            object_to_classify: Object to be classified.
        return:
            dictionary representation of the classification of the provided object and all of it's attributes.
        """


        if isinstance(object_to_classify, ModuleType):
            return "module"
        if isinstance(object_to_classify, type):
            return "class"
        if isinstance(object_to_classify, MethodType):
            return "method"
        if isinstance(object_to_classify, FunctionType):
            return "function"
        if isinstance(object_to_classify, property):
            return "property"
        if object_to_classify.__class__.__module__ == "builtins":
            return "built-in"
        return "instance"
    def classify_module(self, module_to_classify: ModuleType)-> str:
        """
        Classifies modules and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            module_to_classify: Module to be classified.
        return:
            dictionary representation of the classification of the provided module and all of it's attributes.
        """

        return "module"
    
    def classify_instance_of_user_defined_class(self, instance_to_classify: object)-> str:
        """
        Classifies instances of user-defined classes and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            instance_to_classify: Instance of a user-defined class to be classified.
        return:
            dictionary representation of the classification of the provided instance of a user-defined class and all of it's attributes.
        """
        
        return "instance of user-defined class"
    def classify_class(self, class_to_classify: type)-> str:
        """
        Classifies classes and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            class_to_classify: Class to be classified.
        return:
            dictionary representation of the classification of the provided class and all of it's attributes.
        """

        return "class"
    def classify_method(self, method_to_classify: MethodType)-> str:
        """
        Classifies methods and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            method_to_classify: Method to be classified.
        return:
            dictionary representation of the classification of the provided method and all of it's attributes.
        """

        return "method"
    def classify_function(self, function_to_classify: FunctionType)-> str:
        """
        Classifies functions and all of it's attributes and returns a dictionary representation of the classification.
        
        params:
            function_to_classify: Function to be classified.
        return:
            dictionary representation of the classification of the provided function and all of it's attributes.
        """
        
        return "function"
    def classify_property(self, property_to_classify: property)-> str:
        """
        Classifies properties and all of it's attributes and returns a dictionary representation of the classification.

        params:
            property_to_classify: Property to be classified.
        return:
            dictionary representation of the classification of the provided property and all of it's attributes.
        """
        
        return "property"
    