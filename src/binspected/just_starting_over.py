def extract_meta_data(object_to_parse) -> dict:
    """
    Parse an object, extract meta-data and format it into a dictionary.

    Params:
        object_to_parse: The object to be parsed.
  
    Returns:
        A dictionary representation of the meta data.
    """
    
    # Calls to meta data to be extracted.
    meta_data_map = {
        "name": lambda: object_to_parse.__name__,# Object name
        "qualified name": lambda: object_to_parse.__qualname__,# Qualified object name
        "module name": lambda: object_to_parse.__module__,# Objects module name
        "bases": lambda: object_to_parse.__bases__,# Base class names
        "doc string": lambda: object_to_parse.__doc__,# Doc String
        "type hints": lambda: object_to_parse.__annotations__,# Any type hinting of variables
        "namespace attributes": lambda: object_to_parse.__dict__, # Any namespace variables
        "function variables": lambda: object_to_parse.__code__.co_varnames,
        "argument count": lambda: object_to_parse.__code__.co_argcount,
        "default values": lambda: object_to_parse.__defaults__
    }
    inspection = {}
    for meta_data, values in meta_data_map.items():
        try:
            inspection[meta_data] = values()
        except:
            continue
    if "function variables" in inspection and "argument count" in inspection:
        all_variables= inspection.pop('function variables')
        argument_count = inspection.pop("argument count")
        if "default values" in inspection:
            default_values = inspection.pop("default values")
        if "type hints" in inspection:
            type_hints = inspection.pop("type hints")
            
            inspection |= parse_function_variables(all_variables, argument_count, default_values, type_hints)
    return inspection

def parse_function_variables(all_variables, argument_count, default_values, type_hints):    
    """
    Parse the variables of a function.
    Params:
        function_to_parse: The functions whose variables need parsing.
    Returns:
        A dictionary representation of the parsed variables.
    """

    arguments = all_variables[:argument_count]
    local_vars = all_variables[argument_count:]
    arguments_and_defaults = {}
    if default_values:
        number_of_defaults =  len(default_values)
        arguments_with_defaults = arguments[-number_of_defaults:]
        arguments_and_defaults = dict(zip(arguments_with_defaults, default_values))
    arg_dict = {}
    for var in arguments:
        arg_dict[var] = {
            "default value": arguments_and_defaults[var] if var in arguments_and_defaults else None,
            "default type": type_hints[var]  if var in type_hints else None
        }
    complete_parse = {
        "local variables": local_vars,
        "arguments": arg_dict,
        "return type": type_hints["return"]  if "return" in type_hints else None
    }
    return complete_parse