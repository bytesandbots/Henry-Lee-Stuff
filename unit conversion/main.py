import tkinter as tk
from tkinter import *

unitOptions = ["Km", "M", "Lbs", "Kg", "Inches", "Ounces"]

def conversion():
    # Lengths
    # Kilometers
    if unit1.get() == "Km":
        if unit2.get() == "M":
            result['text'] = "{:.4f} miles".format(float(txtboxnum.get()) * 0.621371)
    # Miles
    elif unit1.get() == "M":
        if unit2.get() == "Km":
            result['text'] = "{:.4f} kilometers".format(float(txtboxnum.get()) * 1.60934)
    # Weights
    # Pounds
    elif unit1.get() == "Lbs":
        if unit2.get() == "Kg":
            result['text'] = "{:.4f} kilograms".format(float(txtboxnum.get()) * 0.45359237)
        elif unit2.get() == "Ounces":
            result['text'] = "{:.4f} ounces".format(float(txtboxnum.get()) * 16)
    # Kilograms
    elif unit1.get() == "Kg":
        if unit2.get() == "Lbs":
            result['text'] = "{:.4f} lbs".format(float(txtboxnum.get()) * 2.20462)
        elif unit2.get() == "Ounces":
            result['text'] = "{:.4f} ounces".format(float(txtboxnum.get()) * 35.274)
    # Ounces
    elif unit1.get() == "Ounces":
        if unit2.get() == "Lbs":
            result['text'] = "{:.4f} lbs".format(float(txtboxnum.get()) * 2.20462)
        elif unit2.get() == "Kg":
            result['text'] = "{:.4f} kg".format(float(txtboxnum.get()) / 35.274)
    # Invalid
    else:
        result['text'] = "Invalid"

app = Tk()
app.title("Unit Converter")
app.geometry("600x600")

number = DoubleVar()
unit1 = StringVar()
unit1.set("Select")
unit2 = StringVar()
unit2.set("Select")

numberText = Label(app, text="Number: ")
numberText.grid(row=0, column=0, sticky=W)
unitText = Label(app, text="Unit for number")
unitText.grid(row=1, column=0, sticky=W)
unitText2 = Label(app, text="Unit to be converted into:")
unitText2.grid(row=2, column=0, sticky=W)
txtboxnum = Entry(app, textvariable=number)
txtboxnum.grid(row=0, column=1)
txtboxunit = OptionMenu(app, unit1, *unitOptions)
txtboxunit.grid(row=1, column=1)
txtboxunit2 = OptionMenu(app, unit2, *unitOptions)
txtboxunit2.grid(row=2, column=1)
enterBtn = Button(app, text="Enter", command=conversion)
enterBtn.grid(row=3, column=0, sticky=W)
result = Label(app, text="")
result.grid(row=2, column=2, sticky=W)

app.mainloop()

