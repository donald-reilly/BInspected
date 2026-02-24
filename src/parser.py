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
        return {}
    def parse_class(self, class_to_parse)-> dict:
        """
        Parse a class and return a dictionary representation of it.

        Params:
            class_to_parse: The class to be parsed.
        Returns:
            A dictionary representation of the parsed class.
        """

        return {}
    def parse_class_instance(self, instance_to_parse)-> dict:
        """
        Parse an instance of a class and return a dictionary representation of it.

        Params:
            instance_to_parse: The instance of a class to be parsed.
        Returns:
            A dictionary representation of the parsed instance of a class.
        """

        return {}
    def parse_method(self, method_to_parse)-> dict:
        """
        Parse a method and return a dictionary representation of it.
        Params:
            method_to_parse: The method to be parsed.
        Returns:
             A dictionary representation of the parsed method.
        """

        return {}
    def parse_function(self, function_to_parse)-> dict:
        """
        Parse a function and return a dictionary representation of it.
        Params:
            function_to_parse: The function to be parsed.
        Returns:
             A dictionary representation of the parsed function.
        """
        return {"name": function_to_parse.__name__}
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
            "getter": property_to_parse.fget if  property_to_parse.fget else None,
            "setter": property_to_parse.fset if property_to_parse.fset else None,
            "deleter": property_to_parse.fdel if property_to_parse.fdel else None,
        }
        return parsed_property