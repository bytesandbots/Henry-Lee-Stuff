import tkinter as tk
from tkinter import *
from tkinter import messagebox
unitOptions = ["Km", "M", "Lbs", "Kg"]
def conversion():
    if unit1.get() == "Km":
        if unit2.get() == "M":
            result['text'] = "{:.4} miles".format(float(txtboxnum.get())*0.621371)
    elif unit1.get() == "M":
        if unit2.get() == "Km":
            result['text'] = "{:.4} miles".format(float(txtboxnum.get())*1.6)
    elif unit1.get() == "Lbs":
        if unit2.get() == "Kg":
            result['text'] = "{:.4} miles".format(float(txtboxnum.get())*2.205)
app = Tk()
app.title("Unit Converter")
app.geometry("600x600")
number = DoubleVar()
unit1 = StringVar()
unit1.set("Select")
unit2 = StringVar()
unit2.set("Select")
numberText = tk.Label(app, text="Number: ")
numberText.grid(row = 0, column = 0, sticky = W)
unitText = tk.Label(app, text = "Unit for number")
unitText.grid(row = 1, column = 0, sticky = W)
unitText2 = tk.Label(app, text = "Unit to be converted into:")
unitText2.grid(row = 2, column = 0, sticky = W)
txtboxnum = Entry(app, textvariable = number)
txtboxnum.grid(row = 0, column = 1)
txtboxunit = OptionMenu(app, unit1, *unitOptions)
txtboxunit.grid(row = 1, column = 1)
txtboxunit2 = OptionMenu(app, unit2, *unitOptions)
txtboxunit2.grid(row = 2, column = 1)
enterBtn = tk.Button(app, text = "Enter", command = conversion)
enterBtn.grid(row = 3)
result = tk.Label(app, text = "")
result.grid(row = 4, column = 2)
app.mainloop()

