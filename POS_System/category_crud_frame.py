import tkinter as tk
from tkinter import ttk, messagebox

class CategoryCRUDFrame(tk.Frame):
    def __init__(self, parent, controller, db):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = db

        tk.Label(self, text="Category Management").pack(pady=10)
        tk.Label(self, text="Name:").pack(pady=5)
        self.category_name_entry = tk.Entry(self)
        self.category_name_entry.pack(pady=5)
        tk.Button(self, text="Create", command=self.create_category).pack(pady=5)
        tk.Button(self, text="Update", command=self.update_category).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_category).pack(pady=5)
        self.category_tree = ttk.Treeview(self, columns=("ID", "Name"), show="headings")
        self.category_tree.heading("ID", text="ID")
        self.category_tree.heading("Name", text="Name")
        self.category_tree.pack(pady=10)
        tk.Button(self, text="Refresh", command=self.load_categories).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Dashboard")).pack(pady=5)

    def create_category(self):
        name = self.category_name_entry.get()
        if name:
            try:
                self.db.execute_query("INSERT INTO categories (name) VALUES (%s)", (name,))
                messagebox.showinfo("Success", "Category created successfully")
                self.category_name_entry.delete(0, tk.END)
                self.load_categories()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter category name")

    def update_category(self):
        selected = self.category_tree.selection()
        if selected:
            item = self.category_tree.item(selected[0])
            category_id = item['values'][0]
            name = self.category_name_entry.get()
            if name:
                try:
                    self.db.execute_query("UPDATE categories SET name = %s WHERE id = %s", (name, category_id))
                    messagebox.showinfo("Success", "Category updated successfully")
                    self.category_name_entry.delete(0, tk.END)
                    self.load_categories()
                except Exception as e:
                    messagebox.showerror("Database Error", str(e))
            else:
                messagebox.showwarning("Input Error", "Please enter category name")
        else:
            messagebox.showwarning("Selection Error", "Please select a category to update")

    def delete_category(self):
        selected = self.category_tree.selection()
        if selected:
            item = self.category_tree.item(selected[0])
            category_id = item['values'][0]
            try:
                self.db.execute_query("DELETE FROM categories WHERE id = %s", (category_id,))
                messagebox.showinfo("Success", "Category deleted successfully")
                self.load_categories()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Selection Error", "Please select a category to delete")

    def load_categories(self):
        for item in self.category_tree.get_children():
            self.category_tree.delete(item)
        try:
            categories = self.db.fetch_all("SELECT id, name FROM categories")
            for category in categories:
                self.category_tree.insert("", tk.END, values=category)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
