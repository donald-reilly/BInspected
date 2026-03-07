from typing import Generator, Any
from types import BuiltinFunctionType, GeneratorType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType, FunctionType, MethodType, WrapperDescriptorType, CodeType, NoneType

class BClassified:
    """
    BClassified provides an single point of classification and grouping of python objects.
    """
    def __init__(self) -> None:
        """
        Initialize the BClassified class and it's components.
        
        Params:
            None
        Returns:
            None
        """

        # A collection of known types that could be recursed into.
        self.branch: dict[Any, str] = {
            MethodDescriptorType: "Method Descriptor",
            BuiltinFunctionType: "Builtin Function",
            BuiltinMethodType: "Builtin Method",
            MethodWrapperType: "Method Wrapper",
            WrapperDescriptorType: "Wrapper Descriptor",
            FunctionType: "Function",
            MethodType: "Method",
            Generator: "Generator"
        }
        # A collection of known nodes in the mapping.
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
    def __call__(self, name: str, object_to_classiy: Any)-> tuple[str, str]:
        return self._classify(object_to_classify)
    def _classify(self, name: str, object_to_classify: Any)->tuple[str, str]:
        object_type: Any = type(object_to_classify)
        if object_type in self.branch:
            object_classification = self.branch[object_type]
        elif object_type in self.leaf:
            object_classification = "Attribute"
        else:
            object_classification = "Unknown"
        if name.startswith("__") and name.endswith("__"):
            subclass = "Special"
        elif name.startswith("_"):
            subclass = "Private"
        else:
            subclass = "Public"
        return object_classification, subclass

