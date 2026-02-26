from pathlib import Path
import json

import instrospection
import golden_class



def save_inspection(data, filename="test_inspections/inspection_output.json"):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default= str)
    return path

inspector = instrospection.BInspected()
save_inspection(inspector(instrospection.BInspected), "FigMan_inspection.json")
