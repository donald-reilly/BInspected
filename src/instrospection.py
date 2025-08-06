from collections.abc import Callable

class BInspected:
    def __init__(self, class_to_b_inspected):
        """
        Initializes a inspector with the class intended to be inspected.
        
        Params:
            class_to_b_inpsected: (object) The class that is going to be inspected.
        """
        
        self._class_to_b_inspected = class_to_b_inspected
    @property
    def all_methods(self)-> dict:
        """ 
        Provides access to all callable methods of the class to b inspected
        
        Returns:
            (dict) A dictionary containing all methods of a class
        """

        return self._pull_all_methods()
    @property
    def dunder_methods(self)-> dict:
        """ 
        Provides access to all dunder methods of the class to b inspected
        
        Returns:
            (dict) A dictionary containing all dunder methods of a class
        """

        return self._pull_dunder_methods()
    @property
    def methods(self)-> dict:
        """ 
        Provides access to all normal methods of the class to b inspected
        
        Returns:
            (dict) A dictionary containing all normal methods of a class
        """

        return self._pull_methods()
    @property
    def properties(self)-> dict:
        """ 
        Provides access to all properties defined by @property of the class to b inspected
        
        Returns:
            (dict) A dictionary containing all properties defined by @property of a class
        """

        return self._pull_properties()
    def _pull_all_methods(self)-> dict:
        """
        Creates a dictionary containing references to the callable methods of a class
        
        Returns:
            _methods: (dict) The dictionary containing refrences to the callable methods
        """
        # A dictionary comprehension that pulls all Callables out of a classes dict

        return self._pull_provided_type(Callable)
    def _pull_dunder_methods(self)-> dict:
        """
        Creates a dictionary containing references to the dunder methods of a class
        
        Returns:
            _dudner_methods: (dict) The dictionary containing refrences to the cdunder methods
        """
        # A dictionary comprehension that pulls all dudner methods out of the callables methods.
        _dunder_methods = {name : method
                           for name, method in self.all_methods.items()
                           if name.startswith("__") and name.endswith("__")}
        return _dunder_methods
    def _pull_methods(self)-> dict:
        """
        Creates a dictionary containing references to the normal methods of a class
        
        Returns:
            _dudner_methods: (dict) The dictionary containing refrences to the normal methods.
        """
        # A dictionary comprehension that pulls all normal methods out of the callables methods.
        _normal_methods = {name : method
                           for name, method in self.all_methods.items()
                           if not name.startswith("__") and  not name.endswith("__")}
        return _normal_methods
    def _pull_properties(self)-> dict:
        """ 
        Creates a dictionary containing references to the properties of a class
        
        Returns:
            (dict): A dictionary containing references to the properties of a class
        """

        return self._pull_provided_type(property)
    def _pull_provided_type(self, provided_type):
        """
        Creates a dictionary from the classes __dict__ method, the dicitonary contains only types that match the provided type
        
        Returns: 
            (dict): A dictionary containg only the attributes that are of the provided type
        """
        # A dictionary comprehension that seperates and returns the provided type
        _provided_type= {name: attributes
            for name, attributes in self._class_to_b_inspected.__dict__.items() 
            if isinstance(attributes, provided_type)}
        return _provided_type
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
            properties: (dict) A dictionary containing all the properties of the class.
            cls dict: (dict) A dictionary containing the entire class.
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