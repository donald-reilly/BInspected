from collections.abc import Callable
import types
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
        
        object_type = self.classifier(object_to_inspect)
        parsed_object = self.parser(object_to_inspect, object_type)
        return parsed_object
