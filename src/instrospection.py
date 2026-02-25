
from classifier import Classifier
from parser import Parser
class BInspected:
    #TODO: This is a major refactor of the entire module.
    #TODO: Plans to seperate concerns. Parser has become too crowded and must be changed to fit new scope of BInspected.
    #TODO: This class will consistently makes calls to itself using self() to traverse an object and it's childern for the creation of an introspection dict.
    #TODO: If all goes well this should majorly simplify the creation and recursion of these dictionaries.
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

        self.dispatcher = {
            "module": self.inspect_module,
            "class": self.inspect_class,
            "method": self.inspect_method,
            #"instance": self.inspect_class_instance,
            "property": self.inspect_property,
            #"built-in": self.inspect_built_in,
            "function": self.inspect_function,
            "System Level Module": self.inspect_sys,
        }
        return self._build_inspection(object_to_inspect)
    def _build_inspection(self, object_to_inspect)-> dict:
        """
        Complete object inspection and formation of the objects underlying stucture
        
        Params:
            object_to_inspect: Object to inspect
        Returns:
            An introspection dictionary
        """

        object_type = self.classifier(object_to_inspect)
        parsed_object = self.dispatcher[object_type](object_to_inspect)

        return parsed_object
    def _group_children(self, dict_to_group):
        skip_children = [
            "__loader__",
            "__spec__",
            "__package__",
            "__builtins__",
            "__cached__",
            "__file__",
        ]
        grouped_dict ={
            "modules": {},
            "class": {},
            "method": {},
            "function": {},
            "property": {},
            "property": {},
            "instance": {}
        }
        for key, value in dict_to_group.items():
            if key in skip_children:
                continue
            object_type = self.classifier(value)
            if object_type in grouped_dict:
                grouped_dict[object_type][key] = value
        return grouped_dict
        
    def inspect_sys(self, sys_to_inspect):
        return{"Sytem Level Module": "To Be Added Later"}
    def inspect_module(self, module_to_inspect)-> dict:
        """
        Inspect a modules underlying data structure and provide an introspection dictionary.
        
        Params:
            module_to_inspect: Module to inspect
        Returns:
            An introspection dictionary
        """

        module_dict = self.parser.parse_module(module_to_inspect)
        module_dict["children"] = self._group_children(module_to_inspect.__dict__)

        for object_type in module_dict["children"].values():
            for child_name, child in object_type.items():
                object_type[child_name] = self._group_children(child.__dict__)
        return module_dict
    def inspect_class(self, class_to_inspect)-> dict:
        """
        Inspect a class' underlying data structure and provide an introspection dictionary.
        
        Params:
            class_to_inspect: Class to inspect
        Returns:
            An introspection dictionary
        """
        class_dict = self.parser.parse_class(class_to_inspect)
        children_dict = {}
        return class_dict
    def inspect_method(self, method_to_inspect)-> dict:
        """
        Inspect a methods underlying data structure and provide an introspection dictionary.
        
        Params:
            method_to_inspect: Method to inspect
        Returns:
            An introspection dictionary
        """
        return {"type method": "method type"}
    def inspect_function(self, function_to_inspect)-> dict:
        """
        Inspect a functions underlying data structure and provide an introspection dictionary.
        
        Params:
            function_to_inspect: Function to inspect
        Returns:
            An introspection dictionary
        """
        return {"type funciton": "function type"}
    def inspect_property(self, property_to_inspect)-> dict:
        """
        Inspect a property's underlying data structure and provide an introspection dictionary.
        
        Params:
            property_to_inspect: Property to inspect
        Returns:
            An introspection dictionary
        """
        return {"type property": "property type"}       
    def inspect_varibales(self, variables_to_inspect)-> dict:
        """
        Inspect a varibales underlying data structure and provide an introspection dictionary.
        
        Params:
            variable_to_inspect: Variable to inspect
        Returns:
            An introspection dictionary
        """
        return {"type variable": "variable type"}
    def inspect_arguements(self, arguements_to_inspect)-> dict:
        """
        Inspect an arguements underlying data structure and provide an introspection dictionary.
        
        Params:
            arguement_to_inspect: Arguement to inspect
        Returns:
            An introspection dictionary
        """
        return {"type arguement": "arguement type"}