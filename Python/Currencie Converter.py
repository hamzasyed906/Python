import tkinter as tk
from tkinter import ttk

usd_rates = {
    "USD": 1.0, "EUR": 0.85, "JPY": 156.86, "GBP": 0.74, "CHF": 0.79,
    "CAD": 1.37, "AUD": 1.49, "NZD": 1.73, "CNY": 6.99, "INR": 90.04,
    "KRW": 1442.52, "SGD": 1.29, "HKD": 7.79, "SEK": 9.22, "NOK": 11.0,
    "MXN": 17.91, "BRL": 5.43, "ZAR": 16.51, "TRY": 43.07, "THB": 31.59,
    "IDR": 16704.3, "PLN": 3.80, "DKK": 6.35, "CZK": 22.5, "AED": 3.67
}

def Convert():
    try:
        cur = float(entamount.get())
        fromcur = currency_box.get()
        rate = usd_rates[fromcur]

        usd_value = cur / rate

        result_label.config(text=f"{usd_value:.2f} USD")

    except ValueError:
        result_label.config(text="Enter a valid number")

# GUI setup
root = tk.Tk()
root.title('Currency Converter → USD')
root.geometry('250x250')
root.resizable(0, 0)
root['bg'] = 'light blue'

tk.Label(root, text="Currency to USD", bg='light blue').pack(pady=10)

entamount = tk.Entry(root)
entamount.pack()
entamount.insert(0, "1")

currency_box = ttk.Combobox(root, values=list(usd_rates.keys()))
currency_box.pack(pady=10)
currency_box.set("USD")

tk.Button(root, text="Convert", command=Convert).pack(pady=10)

result_label = tk.Label(root, text="", bg='light blue', font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
