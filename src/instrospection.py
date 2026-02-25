
from classifier import Classifier
from parser import Parser
class BInspected:
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
        parsed_object = self.parser(object_to_inspect, object_type)
        
        return {}
    def inspect_module(self, module_to_inspect)-> dict:
        """
        Inspect a modules underlying data structure and provide an introspection dictionary.
        
        Params:
            module_to_inspect: Module to inspect
        Returns:
            An introspection dictionary
        """
        return {}
    def inspect_class(self, class_to_inspect)-> dict:
        """
        Inspect a class' underlying data structure and provide an introspection dictionary.
        
        Params:
            class_to_inspect: Class to inspect
        Returns:
            An introspection dictionary
        """
        return {}
    def inspect_method(self, method_to_inspect)-> dict:
        """
        Inspect a methods underlying data structure and provide an introspection dictionary.
        
        Params:
            method_to_inspect: Method to inspect
        Returns:
            An introspection dictionary
        """
        return {}
    def inspect_function(self, function_to_inspect)-> dict:
        """
        Inspect a functions underlying data structure and provide an introspection dictionary.
        
        Params:
            function_to_inspect: Function to inspect
        Returns:
            An introspection dictionary
        """
        return {}
    def inspect_varibales(self, variables_to_inspect)-> dict:
        """
        Inspect a varibales underlying data structure and provide an introspection dictionary.
        
        Params:
            variable_to_inspect: Variable to inspect
        Returns:
            An introspection dictionary
        """
        return {}
    def inspect_arguements(self, arguements_to_inspect)-> dict:
        """
        Inspect an arguements underlying data structure and provide an introspection dictionary.
        
        Params:
            arguement_to_inspect: Arguement to inspect
        Returns:
            An introspection dictionary
        """
        return {}