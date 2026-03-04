def extract_meta_data(object_to_parse) -> dict:
    """
    Parse an object, extract meta-data and format it into a dictionary.
    Params:
        object_to_parse: The object to be parsed.
        object_type: The Name of the object to be parsed.
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
        "instance Variables": lambda: object_to_parse.__dict__, # Any namespace variables
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
    return inspection