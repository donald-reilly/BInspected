class Parser:
    """
    Parser: Extracts meta data from python objects.
    
    This class parses python objects to provide clean and readable meta data.
    """

    def __init__(self):
        """
        Initializes the Parser class.
        """

        # The method dispatcher, currently not in use, would like to add for easy extension.
        self.dispatcher = {
            #"module": self.parse_module,
            #"class": self.parse_class,
            #"method": self.parse_method,
            "instance": self._parse_class_instance
            #"function": self.parse_function,
            #"property": self.parse_property
        }

    def __call__(self, object_to_parse, object_type = None)-> dict:
        """
        Parse an object of a given type and return a dictionary representation.

        Params:
            object_to_parse: The object to be parsed.
            object_type: The type of the object to be parsed.
        Returns:
            A dictionary representation of the parsed object.
        """
        
        return self._parse_object(object_to_parse, object_type)
    
    def _parse_object(self, object_to_parse, object_type = None)-> dict:
        """Parse an object of a given type and return a dictionary representation
        
        Params:
            object_to_parse: The object to be parsed.
            object_type: The type of the object to be parsed.
        Returns:
            A dicitonary representation of the parsed object.
            
        """
        meta_data_dict = self._extract_meta_data(object_to_parse)
        #TODO: So far this is the only type that has different parsing. Need to move all the parsing code into the parser and out of the python API.
        if object_type in self.dispatcher:
            meta_data_dict |= self.dispatcher[object_type](object_type)
        return meta_data_dict
    def _extract_meta_data(self, object_to_parse)-> dict:
        """
        Parse an object, extract meta-data and format it into a dictionary.
        
        Params:
            object_to_parse: The object to be parsed.
            object_type: The Name of the object to be parsed.
        Returns:
            A dictionary representation of the meta data.
        """

        # Calls to meta data to be extracted.
        meta_data_map = {
            "name" : lambda: object_to_parse.__name__, # Object name
            "qualified name" : lambda: object_to_parse.__qualname__, # Qualified object name
            "module name" : lambda: object_to_parse.__module__, # Objects module name
            "bases" : lambda: object_to_parse.__bases__, # Base class names
            "doc string" : lambda: object_to_parse.__doc__, # Doc String
            "type hints" : lambda: object_to_parse.__annotations__ # Any type hinting of variables
        }
        meta_data_dict = {} # Initializng the meta data dictionary.
        for meta_data in meta_data_map: # For loop that cycles the meta data map and updates the meta_data dict if an expection isn't encountred.
            try:
                meta_data_dict[meta_data] = meta_data_map[meta_data]()
            except:
                continue
        return meta_data_dict
    
    def _parse_class_instance(self, instance_to_parse)-> dict:
        """
        Parse an instance of a class and return a dictionary representation of it.

        Params:
            instance_to_parse: The instance of a class to be parsed.
        Returns:
            A dictionary representation of the parsed instance of a class.
        """

        # Pulls the instance variables.
        instance_dict = {
                "Instance Variables": instance_to_parse.__dict__
            }
        return instance_dict
    
    def _parse_variables(self, function_to_parse):
        """
        Parse the variables of a function.
        
        Params:
            function_to_parse: The functions whose variables need parsing.
        Returns:
            A dictionary representation of the parsed variables.
        """

        all_variables = function_to_parse.__code__.co_varnames # Assign all variables
        argument_count = function_to_parse.__code__.co_argcount # Assign the count of arguments
        argument_types = function_to_parse.__annotations__ or {} # Assign the defulat types or an empty dict
        argument_default_values = function_to_parse.__defaults__ or () # Assign the default values or an empty list

        local_variables = all_variables[argument_count:] # Pull local variables and kwvars from all vars
        arguments = all_variables[:argument_count] # pull arguments from all vars

        arguments = self._parse_arguments(arguments, argument_types, argument_default_values) # Parse the arguments
        parsed_variables = {
            "arguments": arguments,
            "Local Variables": local_variables,
            "return type": argument_types["return"] if "return" in argument_types else "None"
        }
        return parsed_variables
    
    def _parse_arguments(self, arguments, types, default_values)-> dict:
        """
        Parse the arguments of a function and return a dictionary representation of them.

        Params:
            arguments: The arguments to be parsed.
            types: the argument type hints.
            default_values: Any default values for the arguements.
        Returns:
             A dictionary representation of the parsed arguments of the function.
        """

        num_defaults = len(default_values) # Get the number of vars with default values.
        args_with_defaults = arguments[-num_defaults:] # Get the arguments that have default values
        default_map = dict(zip(args_with_defaults, default_values)) # Assign the defualt values to the correct arguments
        argument_map = {}
        # create the dictionary representation of the parsed arguments.
        for arg in arguments:
            argument_map[arg] = {
                "type":  {types[arg]} if arg in types else "None",
                "default value": default_map[arg] if arg in default_map else "None"
            }

        return argument_map
    