from binspected.classifier import Classifier
from binspected.parser import Parser
class BInspected:
    """
    BInspected: A recursive Python object introspection engine.

    This module provides the BInspected class, which classifies Python
    objects, extracts metadata, groups children, and recursively builds
    a structured introspection dictionary.
    """
    
    def __init__(self):
        """
        Initializes the BInspected class.
        """

        self.dispatcher = {
            "module": self._inspect_module,
            "class": self._inspect_class,
            "method": self._inspect_method,
            "instance": self._inspect_class_instance,
            "property": self._inspect_property,
            "built-in": self._inspect_built_in,
            "function": self._inspect_function
        }
        self.classifier = Classifier()
        self.parser = Parser()

    def __call__(self, object_to_inspect)-> dict:
        """
        Classify an object and return it's introspection dictionary.
        
        Params:
            object_to_inspect: Object to be inspected.
        Returns:
            An introspection dictionary.
        """

        return self._build_inspection(object_to_inspect)
    
    def _build_inspection(self, object_to_inspect)-> dict:
        """
        Complete object inspection and formation of the objects underlying structure
        
        Params:
            object_to_inspect: Object to inspect
        Returns:
            An introspection dictionary
        """

        object_type = self.classifier(object_to_inspect)
        parsed_object = self.dispatcher[object_type](object_to_inspect)

        return parsed_object
    
    def _group_children(self, dict_to_group)-> dict:
        """
        Sort an objects __dict__
        
        Params:
            dict_to_group: __dict__ of the object that needs sorting
        Returns:
            A dictionary of the sorted objects. Example structure: 
            grouped_dict ={
                "module": {},
                "class": {},
                "method": {},
                "function": {},
                "property": {},
                "instance": {}
            }
        """

        # System specific children who don't need to be inspected... yet..
        skip_children = [
            "__loader__",
            "__spec__",
            "__package__",
            "__builtins__",
            "__cached__",
            "__file__",
        ]
        # The layout of the returned dictionary needs to be removed eventually and be formed at creation
        grouped_dict ={
            "module": {},
            "class": {},
            "method": {},
            "function": {},
            "property": {},
            "instance": {}
        }
        # Loop for sorting the __dict__
        for key, value in dict_to_group.items():
            if key in skip_children: # Skips the system entries.
                continue
            object_type = self.classifier(value) # Classifies each child object
            if object_type in grouped_dict:
                grouped_dict[object_type][key] = value # Sorts each object in correct dictionary entry.
        return grouped_dict
    
    def _get_children(self, object_to_get_children)-> dict:
        """
        Gets the children objects and recursively sorts and produces dictionaries.

        Params:
            object_to_get_children: The object whose children need sorting and parsing.
        Returns:
            The parsed dictionary of each child object.
        """

        #TODO: This needs a little rework. It's ok for now, but it's unclear exactly what it's doing and that could be fixed.
        #TODO: Maybe just a renaming so it's function is clear. This is the problem with recursion, it confuses shit.
        children_dict = self._group_children(object_to_get_children.__dict__)# Get the sorted dictionary of the children objects
        # Loop through the sorted dictionary and recursively sort and inspect the children.
        for children_objects in children_dict.values():
            for object_name, object_ref in children_objects.items():
                children_objects[object_name] = self(object_ref)# call back to inspected to start the loop over again.
        return children_dict
    
    def _inspect_module(self, module_to_inspect)-> dict:
        """
        Inspect a modules underlying data structure and provide an introspection dictionary.
        
        Params:
            module_to_inspect: Module to inspect
        Returns:
            An introspection dictionary
        """

        module_dict = self.parser.parse_module(module_to_inspect) # Gets meta data and build dictionary.
        module_dict["children"] = self._get_children(module_to_inspect)# Starts recursion.
        return module_dict
    
    def _inspect_class(self, class_to_inspect)-> dict:
        """
        Inspect a class' underlying data structure and provide an introspection dictionary.
        
        Params:
            class_to_inspect: Class to inspect
        Returns:
            An introspection dictionary
        """

        class_dict = self.parser.parse_class(class_to_inspect)
        class_dict["children"] = self._get_children(class_to_inspect)
        return class_dict
    
    def _inspect_method(self, method_to_inspect)-> dict:
        """
        Inspect a methods underlying data structure and provide an introspection dictionary.
        
        Params:
            method_to_inspect: Method to inspect
        Returns:
            An introspection dictionary
        """
        method_dict = self.parser.parse_method(method_to_inspect)
        function_dict = self(method_to_inspect.__func__)
        method_dict |= function_dict
        return method_dict
    
    def _inspect_function(self, function_to_inspect)-> dict:
        """
        Inspect a functions underlying data structure and provide an introspection dictionary.
        
        Params:
            function_to_inspect: Function to inspect
        Returns:
            An introspection dictionary
        """

        function_dict = self.parser.parse_function(function_to_inspect)
        function_dict["variables"] = self.parser.parse_variables(function_to_inspect)
        return function_dict
    
    def _inspect_property(self, property_to_inspect)-> dict:
        """
        Inspect a property's underlying data structure and provide an introspection dictionary.
        
        Params:
            property_to_inspect: Property to inspect
        Returns:
            An introspection dictionary
        """

        property_dict = self.parser.parse_property(property_to_inspect)
        property_dict["getter"] = self(property_to_inspect.fget) if  property_to_inspect.fget else None
        property_dict["setter"] = self(property_to_inspect.fset) if property_to_inspect.fset else None
        property_dict["deleter"] = self(property_to_inspect.fdel) if property_to_inspect.fdel else None
        return property_dict    
      
    def _inspect_variables(self, variables_to_inspect)-> dict:
        """
        Inspect a variables underlying data structure and provide an introspection dictionary.
        
        Params:
            variable_to_inspect: Variable to inspect
        Returns:
            An introspection dictionary
        """

        return {"type variable": "variable type"}
    
    def _inspect_arguments(self, arguments_to_inspect)-> dict:
        """
        Inspect an arguments underlying data structure and provide an introspection dictionary.
        
        Params:
            argument_to_inspect: Argument to inspect
        Returns:
            An introspection dictionary
        """

        return {"type argument": "argument type"}
    
    def _inspect_class_instance(self, instance_to_inspect)-> dict:
        """
        Inspect an instances underlying data structure and provide an introspection dictionary.
        
        Params:
            instance_to_inspect: instance to inspect
        Returns:
            An introspection dictionary
        """

        instance_dict = self.parser.parse_class_instance(instance_to_inspect)
        class_dict = self(instance_to_inspect.__class__)
        instance_dict = instance_dict | class_dict
        return instance_dict
    def _inspect_built_in(self, instance_to_inspect)-> dict:
        """
        Inspect the built_in underlying data structure and provide an introspection dictionary.
        
        Params:
            built_in_to_inspect: built_in to inspect
        Returns:
            An introspection dictionary
        """

        return {"Not Implemented": "_inspect_built_in"}
    
    def _quick_helper_function(self, thing_to_inspect):
        if type(thing_to_inspect) == dict:
            for key, value in thing_to_inspect.items():
                print(f"{key}, {value}")   
            return  
        print(dir(thing_to_inspect))
        if thing_to_inspect.__dict__:
            for key, value in thing_to_inspect.__dict__.items():
                print(f"{key}, {value}")
    