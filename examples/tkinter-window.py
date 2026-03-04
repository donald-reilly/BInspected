import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json

from binspected import introspection

inspector = introspection.BInspected()

def save_inspection(data, filename="test_inspections/inspection_output.json"):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default= str)
    return path

def on_submit():
    print("Submitted:", entry.get())

root = tk.Tk()
root.title("Nested Tkinter GUI")
root.geometry("400x300")

# --- Top-level frame ---
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

# --- Left nested frame ---
left_frame = ttk.LabelFrame(main_frame, text="User Input", padding=10)
left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

label = ttk.Label(left_frame, text="Enter something:")
label.pack(anchor="w")

entry = ttk.Entry(left_frame)
entry.pack(fill="x", pady=5)

submit_btn = ttk.Button(left_frame, text="Submit", command=on_submit)
submit_btn.pack(pady=5)

# --- Right nested frame ---
right_frame = ttk.LabelFrame(main_frame, text="Options", padding=10)
right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

list_label = ttk.Label(right_frame, text="Pick an option:")
list_label.pack(anchor="w")

listbox = tk.Listbox(right_frame, height=5)
for item in ["Alpha", "Beta", "Gamma", "Delta"]:
    listbox.insert("end", item)
listbox.pack(fill="both", expand=True, pady=5)

select_btn = ttk.Button(right_frame, text="Select", command=lambda: print("Selected:", listbox.get("active")))
select_btn.pack(pady=5)


first_inspection = inspector(root)
save_inspection(first_inspection, filename ="examples/tkrootinspection.json")

root.mainloop()
