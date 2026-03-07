from typing import Generator, Any
from figman import FigMan, MasterGroup
from binspected.bclassified import BClassified

class BInspected:
    """
    BInspected is a python object introspeciton engine.
    """
    def __init__(self, object_to_be_inspected: Any) -> None:
        """
        Initialize the BInspected class and it's components.
        
        Params:
            object_to_be_inspected
        Returns:
            None
        """

        self.object_to_be_inspect = object_to_be_inspected# Assigns the object to be inspected to a instance attribute.
        self.figman = FigMan()# Initialize the dictionary manager.
        self.classifier = BClassified()# Initialize the classifier.
    def __call__(self):
        pass
    def _build_inspection(self)-> MasterGroup:
        pass
    def _inspect(self, object_to_inspect: Any)-> Generator[tuple[str, str], Any]:
        """
        Create a generator function that yeilds the namespace attributes of an object.
        
        Params:
            object_to_inspect
        Returns:
            Generator function yeilding key value pairs of the objects namespace
        """

        for name in dir(object_to_inspect):
            try:
                meta_data = getattr(object_to_inspect, name)
            except:
                continue
            yield name, meta_data
    def _classifier(self)-> str:
        pass
