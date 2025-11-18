import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

class SafePageFrame(tk.Frame):
    def __init__(self, parent, controller, db):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = db

        tk.Label(self, text="Safe Transaction").pack(pady=10)
        tk.Label(self, text="Amount:").pack(pady=5)
        self.safe_amount_entry = tk.Entry(self)
        self.safe_amount_entry.pack(pady=5)
        tk.Label(self, text="Type:").pack(pady=5)
        self.safe_type_var = tk.StringVar(value="Deposit")
        tk.Radiobutton(self, text="Deposit", variable=self.safe_type_var, value="Deposit").pack(pady=5)
        tk.Radiobutton(self, text="Withdrawal", variable=self.safe_type_var, value="Withdrawal").pack(pady=5)
        tk.Button(self, text="Submit", command=self.submit_safe_transaction).pack(pady=10)
        tk.Button(self, text="Print Receipt", command=self.print_receipt).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Dashboard")).pack(pady=5)

    def submit_safe_transaction(self):
        amount = self.safe_amount_entry.get()
        trans_type = self.safe_type_var.get()
        if amount:
            try:
                self.db.execute_query("INSERT INTO safe_transactions (amount, type, date) VALUES (%s, %s, %s)", (float(amount), trans_type, datetime.now()))
                messagebox.showinfo("Success", "Transaction submitted successfully")
                self.safe_amount_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter amount")

    def print_receipt(self):
        # Simple print to file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as f:
                f.write("POS Safe Receipt\n")
                f.write(f"Amount: {self.safe_amount_entry.get()}\n")
                f.write(f"Type: {self.safe_type_var.get()}\n")
                f.write(f"Date: {datetime.now()}\n")
            messagebox.showinfo("Success", "Receipt printed to file")
