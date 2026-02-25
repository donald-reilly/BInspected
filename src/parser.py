from classifier import Classifier
class Parser:
    def __init__(self):
        """
        Initializes the Parser class.
        """

        self.dispatcher = {
            "module": self.parse_module,
            "class": self.parse_class,
            "method": self.parse_method,
            "instance": self.parse_class_instance,
            "function": self.parse_function,
            "property": self.parse_property,
            "built-in": self.parse_built_in
        }
        self.classifier = Classifier()
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

        parsed_module = {
                "name": module_to_parse.__name__,
                "type": "Module",
                "children": {}
            }
        return parsed_module
    def parse_class(self, class_to_parse)-> dict:
        """
        Parse a class and return a dictionary representation of it.

        Params:
            class_to_parse: The class to be parsed.
        Returns:
            A dictionary representation of the parsed class.
        """
        #TODO: This is the issue. I need to find a better way to sort dict and pull out the callables.
        #TODO: Once I fix this issue. Then I can hanlde whatever else is in __dict__. It's classifying so many things as instance
        #classify_callables = {}
        #for object_to_classify in class_to_parse.__dict__.values():
        #    object_type = self.classifier(object_to_classify)
        #    if object_type in self.dispatcher and object_type != "built-in":
        #        classify_callables = classify_callables | self.dispatcher[object_type](object_to_classify)
        
        class_dict = {
            "Qualified Name" : class_to_parse.__qualname__,
            "Module Name" : class_to_parse.__module__,
            "Bases" : class_to_parse.__bases__,
            "DocString" : class_to_parse.__doc__,
            "Type Hints" : class_to_parse.__annotations__,
        }
        return class_dict
    def parse_class_instance(self, instance_to_parse)-> dict:
        """
        Parse an instance of a class and return a dictionary representation of it.

        Params:
            instance_to_parse: The instance of a class to be parsed.
        Returns:
            A dictionary representation of the parsed instance of a class.
        """

        instance_dict = {
                "Instance Variables": instance_to_parse
            }
        return instance_dict
    def parse_built_in(self, built_in_to_parse)-> dict:
        print(type(built_in_to_parse))
        return {"some_builtin": "some_builtin"}
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
                "fully qualified name": function_to_parse.__qualname__,
                "module name": function_to_parse.__module__,
                "function docstring": function_to_parse.__doc__
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
                "doc": property_to_parse.__doc__ if property_to_parse.__doc__ else "No Document",

            }
        return parsed_property

    def parse_variables(self, function_to_parse):
        """
        Parse the variables of a function.
        
        Params:
            function_to_parse: The functions whose variables need parsing.
        Returns:
            A dictionary representation of the parsed variables.
        """

        all_variables = function_to_parse.__code__.co_varnames # Assign all variables
        arguement_count = function_to_parse.__code__.co_argcount # Assign the count of arguements
        arguement_types = function_to_parse.__annotations__ or {} # Assign the defulat types or an empty dict
        arguement_default_values = function_to_parse.__defaults__ or () # Assign the default values or an empty list

        local_variables = all_variables[arguement_count:] # Pull local variables and kwvars from all vars
        arguements = all_variables[:arguement_count] # pull arguements from all vars

        arguements = self.parse_arguements(arguements, arguement_types, arguement_default_values) # Parse the arguements
        parsed_variables = {
            "Arguements": arguements,
            "Local Variables": local_variables,
            "return type": arguement_types["return"] if "return" in arguement_types else "None"
        }
        return parsed_variables
    def parse_arguements(self, arguements, types, default_values)-> dict:
        """
        Parse the arguements of a function and return a dictionary representation of them.

        Params:
            function_to_parse: The function whose arguements are to be parsed.
        Returns:
             A dictionary representation of the parsed arguements of the function.
        """

        num_defaults = len(default_values) # Get the number of vars with default values.
        args_with_defaults = arguements[-num_defaults:] # Get the arguements that have default values
        default_map = dict(zip(args_with_defaults, default_values)) # Assign the defualt values to the correct arguements
        arguement_map = {}
        # create the dictionary representation of the parsed arguements.
        for arg in arguements:
            arguement_map[arg] = {
                "type":  {types[arg]} if arg in types else "None",
                "default value": default_map[arg] if arg in default_map else "None"
            }

        return arguement_map
