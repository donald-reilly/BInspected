class Parser:
    def __init__(self):
        """
        Initializes the Parser class.
        """

        self.dispatcher = {
            "module": self.parse_module,
            "class": self.parse_class,
            "instance": self.parse_class_instance,
            "method": self.parse_method,
            "function": self.parse_function,
            "property": self.parse_property
        }
    def __call__(self, object_to_parse, type)-> dict:
        """
        Parse an object of a given type and return a dictionary representation of it.

        Params:
            object_to_parse: The object to be parsed.
            type: The type of the object to be parsed.
        Returns:
            A dictionary representation of the parsed object.
        """

        return self.dispatcher[type](object_to_parse)
    def parse_module(self, module_to_parse)-> dict:
        """
        Parse a module and return a dictionary representation of it.

        Params:
            module_to_parse: The module to be parsed.
        Returns:
            A dictionary representation of the parsed module.
        """
        return {"Module Name": "module"}
    def parse_class(self, class_to_parse)-> dict:
        """
        Parse a class and return a dictionary representation of it.

        Params:
            class_to_parse: The class to be parsed.
        Returns:
            A dictionary representation of the parsed class.
        """

        return {"Class Name": "class"}
    def parse_class_instance(self, instance_to_parse)-> dict:
        """
        Parse an instance of a class and return a dictionary representation of it.

        Params:
            instance_to_parse: The instance of a class to be parsed.
        Returns:
            A dictionary representation of the parsed instance of a class.
        """

        return {"Instance of Class Name": "instance of class"}
    def parse_method(self, method_to_parse)-> dict:
        """
        Parse a method and return a dictionary representation of it.
        Params:
            method_to_parse: The method to be parsed.
        Returns:
             A dictionary representation of the parsed method.
        """

        return {"Method Name": "method"}
    def parse_function(self, function_to_parse)-> dict:
        """
        Parse a function and return a dictionary representation of it.
        Params:
            function_to_parse: The function to be parsed.
        Returns:
             A dictionary representation of the parsed function.
        """
        parsed_function = {
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
        return parsed_function
    def parse_property(self, property_to_parse)-> dict:
        """
        Parse a property and return a dictionary representation of it.
        Params:
            property_to_parse: The property to be parsed.
        Returns:
             A dictionary representation of the parsed property.
        """

        parsed_property = {
            "name": property_to_parse.__name__,
            "doc": property_to_parse.__doc__ if property_to_parse.__doc__ else None,
            "getter": self.parse_property_function(property_to_parse.fget) if  property_to_parse.fget else None,
            "setter": self.parse_property_function(property_to_parse.fset) if property_to_parse.fset else None,
            "deleter": self.parse_property_function(property_to_parse.fdel) if property_to_parse.fdel else None
        }
        return parsed_property
    def parse_property_function(self, property_function_to_parse)-> dict:
        """
        Parse a property function and return a dictionary representation of it.
        Params:
            property_function_to_parse: The property function to be parsed.
        Returns:
             A dictionary representation of the parsed property function.
        """
        parsed_property_function = {
            "local variable names": property_function_to_parse.__code__.co_varnames,
            "number of positional arguments": property_function_to_parse.__code__.co_argcount,
            "default values for trailing positional arguments": property_function_to_parse.__defaults__,
            "default values for keyword-only arguments": property_function_to_parse.__kwdefaults__,
            "type hints for paramenters and return value": {key: f"{value}" for key, value in property_function_to_parse.__annotations__.items()}
            }   
        return parsed_property_function