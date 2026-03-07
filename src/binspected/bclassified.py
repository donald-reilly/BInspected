from typing import Generator
from types import BuiltinFunctionType, GeneratorType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType, FunctionType, MethodType, WrapperDescriptorType, CodeType, NoneType

class BClassified:
    """
    BClassified provides an single point of classification and grouping of python objects.
    """
    def __init__(self) -> None:
        self.branch = {
            "Method Descriptor": MethodDescriptorType,
            "Builtin Function": BuiltinFunctionType,
            "Builtin Method": BuiltinMethodType,
            "Method Wrapper": MethodWrapperType,
            "Wrapper Descriptor": WrapperDescriptorType,
            "Function": FunctionType,
            "Method": MethodType,
            "Generator": Generator
        }
        self.leaf = (
            int,
            float,
            str,
            bytearray,
            NoneType,
            bool,
            list,
            tuple,
            dict,
            set,
            frozenset
        )
    def __call__(self, object_to_classify):
        pass
    def _classify(self, object_to_classify):
