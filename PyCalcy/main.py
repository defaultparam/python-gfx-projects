from tkinter import *
from tkinter import ttk


def calculate():
    try:
        value = eval(entry.get())
        label.configure(text=f"Result: {value}")
    except Exception as e:
        label.configure(text=f"Error: {str(e)}")


root = Tk()
root.title("PyCalcy - An offline calculator app")
root.geometry("400x500")

entry = Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=4)

button_labels = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    ".",
    "0",
    "=",
    "+",
]

for i in range(4):
    for j in range(4):
        button = Button(root, text=button_labels[i * 4 + j], width=10)
        button.grid(row=i + 1, column=j)
        if button_labels[i * 4 + j] == "=":
            button.configure(command=calculate)
        else:
            button.config(
                command=lambda text=button_labels[i * 4 + j]: entry.insert(END, text)
            )

label = Label(root, text="Result: ")
label.grid(row=5, column=0, columnspan=4)

root.mainloop()
