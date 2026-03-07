from typing import Generator, Any
from figman import FigMan, MasterGroup

class BInspected:
    """
    BInspected is a python object introspeciton engine.
    """
    def __init__(self, object_to_be_inspected: Any) -> None:
        self.object_to_be_inspect = object_to_be_inspected
        self.figman = FigMan()

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
    def _calssifier(self)-> str:
        pass