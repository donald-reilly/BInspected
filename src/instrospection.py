from collections.abc import Callable

class BInspected:
    def bview_functions(self, function_to_inspect: Callable):
        """ 
        The purpose of this method is to provide a complete mapping of the provided method or function
        
        Params:
            function_to_inspect: (Callable) The method or function to B inspected
        """
        
        print(f"{function_to_inspect.__code__.co_varnames} = func.__code__.co_varnames")
        print(f"{function_to_inspect.__code__.co_argcount} = func.__code__.co_argcount")
        print(f"{function_to_inspect.__defaults__} = init.__defaults__")
        print(f"{function_to_inspect.__kwdefaults__} = func.__kwdefaults__")
        print(f"{function_to_inspect.__annotations__} = func.__annotations__")
        print(f"{function_to_inspect.__doc__} = func.__doc__")
        print(f"{function_to_inspect.__name__} = func.__name__")
        print(f"{function_to_inspect.__module__} = func.__module__")
        print(f"{function_to_inspect.__qualname__} = func.__qualname__")
    def bview_class(self, class_to_inspect):
        """
        The purpose of this function is to seperate out the functions from the __dict__ so they can be tested.
        
        Params:
            class_to_inspect: (object) The class whose dictionary needs to be sorted and pulled out.
        Returns:
            functions: (dict) A dictionary containing all the callable functions of the class.
        """
        
        cls_dict = class_to_inspect.__dict__.copy()
        functions = {} # A dictionary to contain all the functions
        properties = {}
        # Loops through __dict__ and seperates all the callables
        for key, value in class_to_inspect.__dict__.items():
            if isinstance(value, Callable):
                functions[key] = value
                del cls_dict[key]
            elif isinstance(value, property):
                properties[key] = value
                del cls_dict[key]
        return functions, properties, cls_dict
    def pull_dunder_methods(self, class_to_inspect):
        pass
    def loop_dict(self, class_to_inspect):
        pass