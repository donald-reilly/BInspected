from figman import FigMan
from instrospection import BInspected
from serialize import To_File
from setting import Setting
import tkinter as tk
import figman


def serialize_text(data, file_path: str) -> None:
    from pprint import pformat
    with open(file_path, "w") as f:
        f.write(pformat(data))

def dump_info(object_to_dump, instance_of_object_to_dump = None):
    """
    Dumps the classification of the provided object to a file.

    params:
        object_to_dump: Object to be dumped.
        instance_of_object_to_dump: Instance of the object to be dumped.
    """

    serialize_text(dir(object_to_dump), f"BInspected/object_research/{object_to_dump}_dir.txt")
    serialize_text(object_to_dump.__dict__, f"BInspected/object_research/{object_to_dump}_dict.txt")
    if instance_of_object_to_dump is not None:
        serialize_text(dir(instance_of_object_to_dump), f"BInspected/object_research/{instance_of_object_to_dump}_instance_dir.txt")
        serialize_text(instance_of_object_to_dump.__dict__, f"BInspected/object_research/{instance_of_object_to_dump}_instance_dict.txt")

figman_instance = FigMan()
setting_instance = Setting("test_setting", 1)

dump_info(FigMan, figman_instance)
dump_info(Setting, setting_instance)


