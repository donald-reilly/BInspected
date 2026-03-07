from types import BuiltinFunctionType, GeneratorType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType, FunctionType, MethodType, WrapperDescriptorType, CodeType, NoneType
from figman import FigMan, MasterGroup

class BInspected:
    """
    BInspected is a python object introspeciton engine.
    """
    def __init__(self, object_to_be_inspected):
        self.object_to_be_inspect = object_to_be_inspected
        self.figman = FigMan()
    def __call__(self, call):
        pass
    def _build_inspection(self)-> MasterGroup:
        pass
    def _inspecct(self)-> GeneratorType:
        pass
    def _calssifier(self)-> str:
        pass