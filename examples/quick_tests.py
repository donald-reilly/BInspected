from binspected import introspection
import tkinter as tk
from binspected import just_starting_over

inspector = introspection.BInspected()

new_window = tk.Tk()

second_inspection = just_starting_over.extract_meta_data(new_window)
print(second_inspection)