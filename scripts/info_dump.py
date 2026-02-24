from figman import FigMan
from instrospection import BInspected
from serialize import To_File
from setting import Setting
import tkinter as tk
import figman
import json
from pathlib import Path
from golden_class import GoldenClass
from setting import Setting


def serialize_text(data, file_path: str) -> None:
    from pprint import pformat
    with open(file_path, "w") as f:
        f.write(pformat(data))

def save_inspection(data, filename="inspection_output.json"):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default= str)
    return path


def dump_info(object_to_dump, instance_of_object_to_dump = None):
    """
    Dumps the classification of the provided object to a file.

    params:
        object_to_dump: Object to be dumped.
        instance_of_object_to_dump: Instance of the object to be dumped.
    """

    serialize_text(dir(object_to_dump), f"BInspected/object_research/{object_to_dump}_dir.txt")
    if hasattr(object_to_dump, "__dict__"):
        serialize_text(object_to_dump.__dict__, f"BInspected/object_research/{object_to_dump}_dict.txt")
    if instance_of_object_to_dump is not None:
        serialize_text(dir(instance_of_object_to_dump), f"BInspected/object_research/{instance_of_object_to_dump}_instance_dir.txt")
        serialize_text(instance_of_object_to_dump.__dict__, f"BInspected/object_research/{instance_of_object_to_dump}_instance_dict.txt")

inspector = BInspected()
save_inspection(inspector(GoldenClass), "FigMan_inspection.json")



