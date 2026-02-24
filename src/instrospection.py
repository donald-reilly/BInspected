from collections.abc import Callable
import types
from classifier import Classifier
from parser import Parser
class BInspected:
    #TODO: Create a parser class. 
    #TODO: Alllrighty then. Going to get back to having some fun with these. Brighten the mood a little bit with this work shit.
    #TODO: Never actually went about using the singleton type deal yet. Make that shit happen brotha. Lets do it. 
    #TODO: Also another thing, I noticed some issues with my logic and some improvements that I can make after everything else. I iterate through .__dict__ pretty often. Could be a one and done. Then pass those all around. Not a major deal. Just no reason to keep doing it.
    def __init__(self):
        """
        Initializes the BInspected class.
        """

        self.classifier = Classifier()
        self.parser = Parser()
    def __call__(self, object_to_inspect):
        """
        Classify an object and return it's introspection dictionary.
        
        Params:
            object_to_inspect: Object to be inspected.
        Returns:
            An introspection dictionary.
        """
        

        object_type = self.classifier(object_to_inspect)
        parsed_object = self.parser(object_to_inspect, object_type)
        return parsed_object
    def _parse_instance(self, instance_to_parse)-> dict[str, str]:
        """
        Creates structure for unique instances of a provided class and returns the introspection dictionary.
        
        Param:
            instance_to_parse: Instance of a class to be parsed.
        Return: 
            Dictionary representation of the the parsed instance of a class.
        """
        
        # Creates and structures the introspection dictionary for instances of a class
        instance_dict = {
            "Name" : f"Instance of {instance_to_parse.__class__.__name__}",# Provides unique name for the instance.
            "Instance Variables" : instance_to_parse.__dict__# Pulls instance specific variables.
        }
        class_dict = self._parse_class(instance_to_parse.__class__)# Parses the underlying class.
        instance_dict = class_dict | instance_dict# Merges the two dictionaries.

        return instance_dict
    def _parse_class(self, class_to_parse: type)-> dict:
        """
        Parses class object and returns an introspection dictionary.

        Param:
            class_to_parse: Class to be parsed.
        Return: 
            Dictionary representaion of parsed class.
        """
        
        # Creates the introspection of the class object.
        class_dict = {
            "Name" : class_to_parse.__name__,
            "Qualified Name" : class_to_parse.__qualname__,
            "Module Name" : class_to_parse.__module__,
            "Bases" : class_to_parse.__bases__,
            "DocString" : class_to_parse.__doc__,
            "Type Hints" : class_to_parse.__annotations__,
            "Callables" : self._parse_callables(class_to_parse),# Parses callables in the class.
            "Property" : self._parse_properties(class_to_parse)# Parses properties in the class.
        }

        return class_dict
    def _parse_callables(self, class_to_parse: type)-> dict:
        """
        Parses all callables of a given class.
        
        Param: 
            class_to_parse: Class to be parsed.
        Return:
            Dictionary representation of the callables of a class.
        """
        
        callables = self._pull_attribute(class_to_parse, Callable) # Pulls the callables from the class.
        # Parses the callables in a class.
        for key, func in callables.items():
            if isinstance(func, types.MethodType):
                callables[key] = self._parse_method(func)
            elif isinstance(func, types.FunctionType):
                callables[key] = self._parse_function(func)

        return callables
    def _parse_method(self, method_to_parse: types.MethodType )-> dict:
        """
        Parses provided bound method.
        
        Param:
            method_to_parse: Method to be parsed.
        Return:
            Introspection dictionary of the bound method.
        """

        # Creates the introspection of the method object.
        _parsed_method = {
            "function name": method_to_parse.__name__,
            "Qualified Name": method_to_parse.__qualname__,
            "Callable type": type(method_to_parse),
            "module name": method_to_parse.__module__,
            "function docstring": method_to_parse.__doc__,
            "local variable names": method_to_parse.__code__.co_varnames,
            "number of positional arguments": method_to_parse.__code__.co_argcount,
            "default values for trailing positional arguments": method_to_parse.__func__.__defaults__,
            "default values for keyword-only arguments": method_to_parse.__func__.__kwdefaults__,
            "type hints for paramenters and return value": method_to_parse.__annotations__
        }

        return _parsed_method
    def _parse_function(self, function_to_parse: types.FunctionType)-> dict:
        """
        Parses provided function.

        Param:
            function_to_parse: Function to be parsed.
        Return:
            Introspection dictionary of the function.
        """

        # Creates the introspection of the function object.
        _parsed_method = {
            "function name": function_to_parse.__name__,
            "fully qualified name": function_to_parse.__qualname__,
            "Callable type": type(function_to_parse),
            "module name": function_to_parse.__module__,
            "function docstring": function_to_parse.__doc__,
            "local variable names": function_to_parse.__code__.co_varnames,
            "number of positional arguments": function_to_parse.__code__.co_argcount,
            "default values for trailing positional arguments": function_to_parse.__defaults__,
            "default values for keyword-only arguments": function_to_parse.__kwdefaults__,
            "type hints for paramenters and return value": function_to_parse.__annotations__
        }

        return _parsed_method
    def _parse_properties(self, class_to_parse: type)-> dict:
        """
        Parse all properties of a given class.
        
        Param:
            class_to_parse: Class to be parsed.
        Return:
           Properties of a given class.
        """
        
        #TODO: This needs to actually parse the property, for now it only provides the property.
        return self._pull_properties(class_to_parse)
    def _pull_attribute(self, class_to_parse,  provided_type):
        """
        Creates a dictionary from the classes __dict__ method, the dicitonary contains only types that match the provided type
        
        Returns: 
            (dict): A dictionary containg only the attributes that are of the provided type
        """
        
        # A dictionary comprehension that seperates and returns the provided type
        _provided_type= {name: attributes
            for name, attributes in class_to_parse.__dict__.items() 
            if isinstance(attributes, provided_type)}
        return _provided_type
    def _pull_dunder_methods(self):
        """
        Creates a dictionary containing references to the dunder methods of a class
        
        Returns:
            _dudner_methods: (dict) The dictionary containing refrences to the cdunder methods
        """

        #TODO: Need to fix this. Class is going to be a singleton. WOn't hold references to methods anymore.
        ## A dictionary comprehension that pulls all dudner methods out of the callables methods.
        #_dunder_methods = {name : method
        #                   for name, method in self.all_methods.items()
        #                   if name.startswith("__") and name.endswith("__")}
        #return _dunder_methods
        pass
    def _pull_methods(self):
        """
        Creates a dictionary containing references to the normal methods of a class
        
        Returns:
            _dudner_methods: (dict) The dictionary containing refrences to the normal methods.
        """

        #TODO: Need to fix this. Class in now a singleton. Doesn't hold references to methods anymore.
        ## A dictionary comprehension that pulls all normal methods out of the callables methods.
        #_normal_methods = {name : method
        #                   for name, method in self.all_methods.items()
        #                   if not name.startswith("__") and  not name.endswith("__")}
        #return _normal_methods
        pass
    def _pull_properties(self, class_to_parse)-> dict:
        """ 
        Creates a dictionary containing references to the properties of a class
        
        Returns:
            (dict): A dictionary containing references to the properties of a class
        """

        return self._pull_attribute(class_to_parse, property)
    def _pull_method_args(self, method_to_map: Callable)-> dict:
        """
        Sort this methods arguements. Provide a dictionary of each arguement and the required types.
        
        Params:
            method_to_map: (Callable) The method who's arguements need to be introspected.
        Returns:
            mapped_args: (dict) A dictionary that becomes kwargs for class instantiation
        """
        
        mapped_args = {
            "all_vars": method_to_map.__code__.co_varnames, 
            "default_vals": method_to_map.__defaults__, 
            "default_kw": method_to_map.__kwdefaults__, 
            "annotations": method_to_map.__annotations__
        }

        return mapped_args
    def _parse_method_args_for_instantiation(self, method_to_map)-> dict:
        """
        Parse the args required for creating an instance of the class.
        
        Params:
            mapped_args:(dict) A dictionary containing all arguements of the class.
        Returns:
            method_args:(dict) A dictionary containing kwargs necassary for creating an instance of the class
        """
        
        mapped_args = self._pull_method_args(method_to_map)
        method_kwargs = {}
        for arg in mapped_args["all_vars"]:
            if arg in mapped_args['annotations']:
                method_kwargs[arg] = mapped_args['annotations'][arg]
            elif arg == "self": # Not sure if I should keep this, makes my intent obvious.
                continue
            else:
                method_kwargs[arg] = None

        return method_kwargs