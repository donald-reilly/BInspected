from figman import FigMan
from types import BuiltinFunctionType, BuiltinMethodType, MethodDescriptorType, MethodWrapperType, FunctionType, MethodType, WrapperDescriptorType, CodeType
def extract_meta_data(object_to_parse):
    """
    Parse an object, extract meta-data and format it into a dictionary.

    Params:
        object_to_parse: The object to be parsed.
  
    Returns:
        A dictionary representation of the meta data.
    """
    

    for name in dir(object_to_parse):
        try:
            meta_data = getattr(object_to_parse, name)
        except:
            continue
        yield name, meta_data
"""    #TODO this is not stout.

    if "function variables" in inspection and "argument count" in inspection:
        all_variables= inspection.pop('function variables')
        argument_count = inspection.pop("argument count")
        if "default values" in inspection:
            default_values = inspection.pop("default values")
        if "type hints" in inspection:
            type_hints = inspection.pop("type hints")
            inspection |= parse_function_variables(all_variables, argument_count, default_values, type_hints)
    return inspection
"""
def parse_function_variables(all_variables, argument_count, default_values, type_hints):# -> dict[str, Any]:    
    """
    Parse the variables of a function.

    Params:
        function_to_parse: The functions whose variables need parsing.
    Returns:
        A dictionary representation of the parsed variables.
    """
    #TODO: There are two options in this. Make it stout here. Or make it stout on input.... hmmmm. If I know it will work for the inputs I want, make what i'm inspecting very clear. Then I can reject them before they ever get here.
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

def build_introspect(object_to_inspect, current_level, search, inspect_methods, inspect_arguments):
    """
    Test function to see how I want to use generators
    """

    attributes_to_skip =[
        "__class__",
        "__builtins__"
    ]

    types_to_skip = (
        MethodDescriptorType,
        BuiltinFunctionType,
        BuiltinMethodType,
        MethodWrapperType,
        WrapperDescriptorType
    )
    if type(object_to_inspect) is not dict:
        object_to_recurse = extract_meta_data(object_to_inspect)
    else:
        object_to_recurse = object_to_inspect
    for name, value in object_to_recurse:
        if isinstance(value, types_to_skip) or name in attributes_to_skip:
            continue
        if isinstance(value, MethodType) and inspect_methods:
            new_group = current_level("methods")
            if name.startswith("__") and name.endswith("__"):
                new_group1 = new_group("special methods")
                new_group1(name, value)
        if search == name:
            for key, item in value.items():
                new_group = current_level(key)
                build_introspect(item, new_group, search, inspect_methods, inspect_arguments)
        else:
            current_level(name, value)

def master_config(object_to_inspect, search = "", inspect_methods = False, inspect_arguments = False):

        mata_data_manager = FigMan()
        new_meta_data = mata_data_manager.configuration(str(object_to_inspect))
        build_introspect(object_to_inspect, new_meta_data, search, inspect_methods, inspect_arguments)

        return(new_meta_data)
