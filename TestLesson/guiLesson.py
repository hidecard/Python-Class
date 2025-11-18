import tkinter

# print(tkinter.TkVersion)

from tkinter import*

# def greet():
#     Label.config(text="Welcome Back")

# root = Tk()
# root.title("Test GUI")
# root.geometry("800x400")
# Label = Label(root,text="Welcome")
# Button = Button(root,text="Click Me",command=greet)
# Label.pack()
# Button.pack()
# root.mainloop()

# def show():
#     data = input.get()
#     label.config(text=f"Hello {data}")

# root = Tk()
# root.title("Lesson Input")
# root.geometry("300x400")

# input = Entry(root)
# btn = Button(root,text="Click Me",command=show)
# label = Label(root,text="")

# input.pack()
# btn.pack()
# label.pack()

# root.mainloop()

def show():
    data = text.get("1.0",END)
    print(data)

root = Tk()

root.geometry("300x400")
root.title("Lesson 2")

text = Text(root,width=30,height=5)
btn = Button(root,text="Read Text",command=show)
btn.pack()
text.pack(pady=10)

root.mainloop()