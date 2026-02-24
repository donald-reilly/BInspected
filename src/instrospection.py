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