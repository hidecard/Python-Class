from tkinter import *

def show_name():
    name = entry.get()
    label.config(text=f"Hello, {name}!")


root = Tk()
root.geometry("400x300")
root.title("Entry Example")

entry = Entry(root)
entry.pack(pady=10)

button = Button(root, text="Submit", command=show_name)
button.pack(pady=5)

label = Label(root, text="")
label.pack(pady=10)

root.mainloop()
