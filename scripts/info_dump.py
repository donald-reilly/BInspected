from pathlib import Path
import json

from instrospection import BInspected
import golden_class



def save_inspection(data, filename="inspection_output.json"):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default= str)
    return path

inspector = BInspected()
save_inspection(inspector(golden_class), "FigMan_inspection.json")



