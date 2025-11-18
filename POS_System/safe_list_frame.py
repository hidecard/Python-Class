import tkinter as tk
from tkinter import ttk, messagebox

class SafeListFrame(tk.Frame):
    def __init__(self, parent, controller, db):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = db

        tk.Label(self, text="Safe Transactions Report").pack(pady=10)
        self.safe_tree = ttk.Treeview(self, columns=("ID", "Amount", "Type", "Date"), show="headings")
        self.safe_tree.heading("ID", text="ID")
        self.safe_tree.heading("Amount", text="Amount")
        self.safe_tree.heading("Type", text="Type")
        self.safe_tree.heading("Date", text="Date")
        self.safe_tree.pack(pady=10)
        tk.Button(self, text="Refresh", command=self.load_safe_transactions).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Dashboard")).pack(pady=5)

    def load_safe_transactions(self):
        for item in self.safe_tree.get_children():
            self.safe_tree.delete(item)
        try:
            transactions = self.db.fetch_all("SELECT id, amount, type, date FROM safe_transactions")
            for trans in transactions:
                self.safe_tree.insert("", tk.END, values=trans)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
