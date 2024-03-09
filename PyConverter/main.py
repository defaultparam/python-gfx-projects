from tkinter import *
from tkinter import ttk


# define a method to calculate feet to meter
def calculate():
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)

    except ValueError:
        meters.set("An error occurred!")
        pass


# create a root element and add title to the window
root = Tk()
root.title("Feet - Meter Converter")
root.geometry("1000x500")

# Create a frame widget, which will be the parent element on all the frames that we do
mainframe = ttk.Frame(root, padding="3 3 12 12", width=400, height=300)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(mainframe, width=70, textvariable=feet)
feet_entry.grid(
    column=2,
    row=1,
    sticky=(W, E),
)

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W))

ttk.Button(mainframe, command=calculate, text="Calculate").grid(
    column=3, row=3, sticky=E
)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.mainloop()
