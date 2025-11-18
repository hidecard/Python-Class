import tkinter as tk
from tkinter import ttk, messagebox

class StaffCRUDFrame(tk.Frame):
    def __init__(self, parent, controller, db):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = db

        tk.Label(self, text="Staff Management").pack(pady=10)
        tk.Label(self, text="Name:").pack(pady=5)
        self.staff_name_entry = tk.Entry(self)
        self.staff_name_entry.pack(pady=5)
        tk.Label(self, text="Role:").pack(pady=5)
        self.staff_role_entry = tk.Entry(self)
        self.staff_role_entry.pack(pady=5)
        tk.Button(self, text="Create", command=self.create_staff).pack(pady=5)
        tk.Button(self, text="Update", command=self.update_staff).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_staff).pack(pady=5)
        self.staff_tree = ttk.Treeview(self, columns=("ID", "Name", "Role"), show="headings")
        self.staff_tree.heading("ID", text="ID")
        self.staff_tree.heading("Name", text="Name")
        self.staff_tree.heading("Role", text="Role")
        self.staff_tree.pack(pady=10)
        tk.Button(self, text="Refresh", command=self.load_staff).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Dashboard")).pack(pady=5)

    def create_staff(self):
        name = self.staff_name_entry.get()
        role = self.staff_role_entry.get()
        if name and role:
            try:
                self.db.execute_query("INSERT INTO staff (name, role) VALUES (%s, %s)", (name, role))
                messagebox.showinfo("Success", "Staff created successfully")
                self.staff_name_entry.delete(0, tk.END)
                self.staff_role_entry.delete(0, tk.END)
                self.load_staff()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter name and role")

    def update_staff(self):
        selected = self.staff_tree.selection()
        if selected:
            item = self.staff_tree.item(selected[0])
            staff_id = item['values'][0]
            name = self.staff_name_entry.get()
            role = self.staff_role_entry.get()
            if name and role:
                try:
                    self.db.execute_query("UPDATE staff SET name = %s, role = %s WHERE id = %s", (name, role, staff_id))
                    messagebox.showinfo("Success", "Staff updated successfully")
                    self.staff_name_entry.delete(0, tk.END)
                    self.staff_role_entry.delete(0, tk.END)
                    self.load_staff()
                except Exception as e:
                    messagebox.showerror("Database Error", str(e))
            else:
                messagebox.showwarning("Input Error", "Please enter name and role")
        else:
            messagebox.showwarning("Selection Error", "Please select staff to update")

    def delete_staff(self):
        selected = self.staff_tree.selection()
        if selected:
            item = self.staff_tree.item(selected[0])
            staff_id = item['values'][0]
            try:
                self.db.execute_query("DELETE FROM staff WHERE id = %s", (staff_id,))
                messagebox.showinfo("Success", "Staff deleted successfully")
                self.load_staff()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Selection Error", "Please select staff to delete")

    def load_staff(self):
        for item in self.staff_tree.get_children():
            self.staff_tree.delete(item)
        try:
            staff = self.db.fetch_all("SELECT id, name, role FROM staff")
            for s in staff:
                self.staff_tree.insert("", tk.END, values=s)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
