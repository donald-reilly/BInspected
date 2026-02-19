from collections.abc import Callable
import types

class BInspected:

    def __call__(self, object_to_inspect)-> dict[str]:
        """
        Classify an object and return it's introspection dictionary.
        
        Params:
            object_to_inspect(object): Object to be inspected.
        Returns:
            (dict): An introspectin dictionary.
        """
        
        return self._classify_object(object_to_inspect)
    def _classify_object(self, object_to_classify)-> dict[str]:
        """
        Classifies object and returns it's introspeciton dictionary.
        
        Params:
            object_to_inspect(object): Object to be inspected
        Returns: 
            An introspection dictionary.
        """
        
        # Logic gate to classify provided object for parsing.
        if isinstance(object_to_classify, type):# Classifies classes.
            return self._parse_class(object_to_classify)
        if isinstance(object_to_classify, (types.FunctionType, types.MethodType)):# Classifies methods and functions.
            return self._parse_method(object_to_classify)
        if object_to_classify.__class__.__module__ == "builtins":# Classifies builtin objects.
            return "builtin_instance"
        return self._parse_instance(object_to_classify)# classifies instances of user-defined classes.
    def _parse_instance(self, instance_to_parse)-> dict[str]:
        """
        Creates structure for unique instances of a provided class and returns the introspection dictionary.
        
        Param:
            param instance_to_parse: Instance of a class to be parsed.
        Return: 
            Dictionary representation of the the parsed instance of a class.
        """
        
        # Creates and structures the introspection dictionary for instances of a class
        instance_dict["Name"] = f"Instance of {instance_to_parse.__class__["Name"]}" # Provides unique name for the instance.
        instance_dict["Instance Variables"] = instance_to_parse.__dict__ # Pulls instance specific variables.
        class_dict = self._parse_class(instance_to_parse.__class__) # Parses the underlying class.
        instance_dict = instance_dict | class_dict # Merges the two dictionaries.
        return instance_dict
    def _parse_class(self, class_to_parse: type)-> dict[str]:
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
            "Callables" : self._parse_callables(class_to_parse), # Parses callables in the class.
            "Property" : self._parse_properties(class_to_parse) # Parses properties in the class.
        }
        return class_dict
    def _parse_callables(self, class_to_parse: type)-> dict[str]:
        """
        Parses all callables of a given class.
        
        Param: 
            class_to_parse: Class to be parsed.
        Return:
            Dictionary representation of the callables of a class.
        """
        
        callables = self._pull_attribute(class_to_parse, Callable) # Pulls the callables from the class.
        # Parses the callables in a class.
        for func in callables.keys():
            callables[func] = self._parse_method(callables[func])
        return callables
    def _parse_properties(self, class_to_parse: type)-> dict:
        """
        Parse all properties of a given class
        
        Param:
            class_to_parse: Class to be parsed
        Return
           Properties of a given class
        """
        
        #TODO: This needs to actually parse the property, for now it only provides the property.
        return self._pull_properties(class_to_parse)
    def _parse_method(self, method_to_parse: types.MethodType | types.FunctionType)-> dict:
        """
        Docstring for _parse_method
        
        :return: Description
        :rtype: dict[Any, Any]
        """

        mtp = method_to_parse
        if isinstance(mtp, types.MethodType):
            _parsed_method = {
                "local variable names": mtp.__code__.co_varnames,
                "number of positional arguments": mtp.__code__.co_argcount,
                "default values for trailing positional arguments": mtp.__func__.__defaults__,
                "default values for keyword-only arguments": mtp.__func__.__kwdefaults__,
                "type hints for paramenters and return value": mtp.__annotations__,
                "function docstring": mtp.__doc__,
                "function name": mtp.__name__,
                "module name": mtp.__module__,
                "fully qualified name": mtp.__qualname__,
            }

        elif isinstance(mtp, types.FunctionType):
            _parsed_method = {
                "local variable names": mtp.__code__.co_varnames,
                "number of positional arguments": mtp.__code__.co_argcount,
                "type hints for paramenters and return value": mtp.__annotations__,
                "function docstring": mtp.__doc__,
                "function name": mtp.__name__,
                "module name": mtp.__module__,
                "fully qualified name": mtp.__qualname__,
            }
            
        else:
            _parsed_method = {"error" : f"{mtp} is of type {type(mtp)} not Function or Method"}
        return _parsed_method
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
    def _pull_dunder_methods(self)-> dict:
        """
        Creates a dictionary containing references to the dunder methods of a class
        
        Returns:
            _dudner_methods: (dict) The dictionary containing refrences to the cdunder methods
        """
        
        # A dictionary comprehension that pulls all dudner methods out of the callables methods.
        _dunder_methods = {name : method
                           for name, method in self.all_methods.items()
                           if name.startswith("__") and name.endswith("__")}
        return _dunder_methods
    def _pull_methods(self)-> dict:
        """
        Creates a dictionary containing references to the normal methods of a class
        
        Returns:
            _dudner_methods: (dict) The dictionary containing refrences to the normal methods.
        """
        
        # A dictionary comprehension that pulls all normal methods out of the callables methods.
        _normal_methods = {name : method
                           for name, method in self.all_methods.items()
                           if not name.startswith("__") and  not name.endswith("__")}
        return _normal_methods
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