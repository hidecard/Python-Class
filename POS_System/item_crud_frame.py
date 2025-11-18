import tkinter as tk
from tkinter import ttk, messagebox

class ItemCRUDFrame(tk.Frame):
    def __init__(self, parent, controller, db):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = db

        tk.Label(self, text="Item Management").pack(pady=10)
        tk.Label(self, text="Name:").pack(pady=5)
        self.item_name_entry = tk.Entry(self)
        self.item_name_entry.pack(pady=5)
        tk.Label(self, text="Price:").pack(pady=5)
        self.item_price_entry = tk.Entry(self)
        self.item_price_entry.pack(pady=5)
        tk.Label(self, text="Barcode:").pack(pady=5)
        self.item_barcode_entry = tk.Entry(self)
        self.item_barcode_entry.pack(pady=5)
        tk.Label(self, text="Category:").pack(pady=5)
        self.item_category_var = tk.StringVar()
        self.item_category_menu = ttk.Combobox(self, textvariable=self.item_category_var)
        self.item_category_menu.pack(pady=5)
        tk.Button(self, text="Create", command=self.create_item).pack(pady=5)
        tk.Button(self, text="Update", command=self.update_item).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_item).pack(pady=5)
        self.item_tree = ttk.Treeview(self, columns=("ID", "Name", "Price", "Barcode", "Category"), show="headings")
        self.item_tree.heading("ID", text="ID")
        self.item_tree.heading("Name", text="Name")
        self.item_tree.heading("Price", text="Price")
        self.item_tree.heading("Barcode", text="Barcode")
        self.item_tree.heading("Category", text="Category")
        self.item_tree.pack(pady=10)
        tk.Button(self, text="Refresh", command=self.load_items).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Dashboard")).pack(pady=5)

    def load_categories_for_item(self):
        try:
            categories = self.db.fetch_all("SELECT id, name FROM categories")
            self.item_category_menu['values'] = [f"{cat[0]} - {cat[1]}" for cat in categories]
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def create_item(self):
        name = self.item_name_entry.get()
        price = self.item_price_entry.get()
        barcode = self.item_barcode_entry.get()
        category = self.item_category_var.get().split(' - ')[0] if self.item_category_var.get() else None
        if name and price and barcode and category:
            try:
                self.db.execute_query("INSERT INTO items (name, price, barcode, category_id) VALUES (%s, %s, %s, %s)", (name, float(price), barcode, int(category)))
                messagebox.showinfo("Success", "Item created successfully")
                self.item_name_entry.delete(0, tk.END)
                self.item_price_entry.delete(0, tk.END)
                self.item_barcode_entry.delete(0, tk.END)
                self.item_category_var.set("")
                self.load_items()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter all fields")

    def update_item(self):
        selected = self.item_tree.selection()
        if selected:
            item = self.item_tree.item(selected[0])
            item_id = item['values'][0]
            name = self.item_name_entry.get()
            price = self.item_price_entry.get()
            barcode = self.item_barcode_entry.get()
            category = self.item_category_var.get().split(' - ')[0] if self.item_category_var.get() else None
            if name and price and barcode and category:
                try:
                    self.db.execute_query("UPDATE items SET name = %s, price = %s, barcode = %s, category_id = %s WHERE id = %s", (name, float(price), barcode, int(category), item_id))
                    messagebox.showinfo("Success", "Item updated successfully")
                    self.item_name_entry.delete(0, tk.END)
                    self.item_price_entry.delete(0, tk.END)
                    self.item_barcode_entry.delete(0, tk.END)
                    self.item_category_var.set("")
                    self.load_items()
                except Exception as e:
                    messagebox.showerror("Database Error", str(e))
            else:
                messagebox.showwarning("Input Error", "Please enter all fields")
        else:
            messagebox.showwarning("Selection Error", "Please select an item to update")

    def delete_item(self):
        selected = self.item_tree.selection()
        if selected:
            item = self.item_tree.item(selected[0])
            item_id = item['values'][0]
            try:
                self.db.execute_query("DELETE FROM items WHERE id = %s", (item_id,))
                messagebox.showinfo("Success", "Item deleted successfully")
                self.load_items()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Selection Error", "Please select an item to delete")

    def load_items(self):
        for item in self.item_tree.get_children():
            self.item_tree.delete(item)
        try:
            items = self.db.fetch_all("SELECT i.id, i.name, i.price, i.barcode, c.name FROM items i JOIN categories c ON i.category_id = c.id")
            for item in items:
                self.item_tree.insert("", tk.END, values=item)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
