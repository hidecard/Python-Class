# Tkinter GUI Application
# Includes essentials: text, canvas, button, form, etc.

import tkinter as tk
from tkinter import messagebox, simpledialog

class TkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter GUI Demo")
        self.root.geometry("600x400")

        # Text Widget
        self.text_label = tk.Label(root, text="Text Widget:")
        self.text_label.pack(pady=5)
        self.text_area = tk.Text(root, height=5, width=50)
        self.text_area.pack(pady=5)
        self.text_area.insert(tk.END, "This is a text area. You can type here...")

        # Canvas Widget
        self.canvas_label = tk.Label(root, text="Canvas Widget:")
        self.canvas_label.pack(pady=5)
        self.canvas = tk.Canvas(root, width=200, height=100, bg="lightblue")
        self.canvas.pack(pady=5)
        # Draw a rectangle and oval on canvas
        self.canvas.create_rectangle(50, 25, 150, 75, fill="red")
        self.canvas.create_oval(75, 40, 125, 60, fill="yellow")

        # Button Widget
        self.button = tk.Button(root, text="Click Me!", command=self.button_click)
        self.button.pack(pady=10)

        # Form Elements (Entry and Label)
        self.form_label = tk.Label(root, text="Simple Form:")
        self.form_label.pack(pady=5)
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=5)

        # Additional GUI Elements
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(root, text="Check me", variable=self.checkbox_var)
        self.checkbox.pack(pady=5)

        self.radio_var = tk.StringVar(value="Option1")
        self.radio1 = tk.Radiobutton(root, text="Option 1", variable=self.radio_var, value="Option1")
        self.radio1.pack()
        self.radio2 = tk.Radiobutton(root, text="Option 2", variable=self.radio_var, value="Option2")
        self.radio2.pack()

        # Menu Bar
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

    def button_click(self):
        messagebox.showinfo("Button Clicked", "Hello! Button was clicked.")

    def submit_form(self):
        name = self.name_entry.get()
        if name:
            messagebox.showinfo("Form Submitted", f"Hello, {name}!")
        else:
            messagebox.showwarning("Form Error", "Please enter a name.")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        # Simple open simulation
        content = simpledialog.askstring("Open File", "Enter file content:")
        if content:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()
