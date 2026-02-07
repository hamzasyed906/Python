import tkinter as tk
from tkinter import ttk

togram = {
    "Gram": 1,
    "KG": 1000, 
    "Ounce": 28.34952, 
    "Pound": 453.59237
}

def Convert():
    try:
        weight = float(entamount.get())
        from_unit = weight_box.get()
        
        rate = togram[from_unit]

        grvalue = weight * rate

        result_label.config(text=f"{grvalue:.2f} Grams", fg="black")

    except ValueError:
        result_label.config(text="Enter a valid number", fg="red")
    except KeyError:
        result_label.config(text="Select a unit", fg="red")

root = tk.Tk()
root.title('Weight Converter')
root.geometry('300x300')
root.resizable(0, 0)
root['bg'] = 'light blue'

tk.Label(root, text="Weight Converter to Grams", bg="light blue", font=("Arial", 10, "bold")).pack(pady=10)

entamount = tk.Entry(root)
entamount.pack()
entamount.insert(0, "1")

weight_box = ttk.Combobox(root, values=list(togram.keys()))
weight_box.pack(pady=10)
weight_box.set("KG")

tk.Button(root, text="Convert", command=Convert, width=15).pack(pady=10)

result_label = tk.Label(root, text="", bg='light blue', font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()