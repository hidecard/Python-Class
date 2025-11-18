import tkinter as tk

class DashboardFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="POS System Dashboard").pack(pady=10)
        tk.Button(self, text="Category CRUD", command=lambda: self.controller.show_frame("CategoryCRUD")).pack(pady=5)
        tk.Button(self, text="Item CRUD", command=lambda: self.controller.show_frame("ItemCRUD")).pack(pady=5)
        tk.Button(self, text="Staff CRUD", command=lambda: self.controller.show_frame("StaffCRUD")).pack(pady=5)
        tk.Button(self, text="Safe Page", command=lambda: self.controller.show_frame("SafePage")).pack(pady=5)
        tk.Button(self, text="Safe List", command=lambda: self.controller.show_frame("SafeList")).pack(pady=5)
        tk.Button(self, text="Logout", command=lambda: self.controller.show_frame("Login")).pack(pady=5)
