# Mini POS System with SQLite Connection
# Includes login and create product pages (4-5 pages total)
# Uses SQLite for simplicity, no server setup required

import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

class POSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini POS System")
        self.root.geometry("400x300")

        self.db_connection = None
        self.connect_db()

        self.frames = {}
        self.create_frames()

        self.show_frame("Login")

    def connect_db(self):
        try:
            self.db_connection = sqlite3.connect('pos_db.sqlite')
            print("Database connected successfully.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
            self.root.quit()

    def create_frames(self):
        # Login Frame
        self.frames["Login"] = tk.Frame(self.root)
        tk.Label(self.frames["Login"], text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.frames["Login"])
        self.username_entry.pack(pady=5)
        tk.Label(self.frames["Login"], text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.frames["Login"], show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self.frames["Login"], text="Login", command=self.login).pack(pady=10)

        # Dashboard Frame
        self.frames["Dashboard"] = tk.Frame(self.root)
        tk.Label(self.frames["Dashboard"], text="Welcome to POS Dashboard").pack(pady=10)
        tk.Button(self.frames["Dashboard"], text="Create Product", command=lambda: self.show_frame("CreateProduct")).pack(pady=5)
        tk.Button(self.frames["Dashboard"], text="View Products", command=lambda: self.show_frame("ViewProducts")).pack(pady=5)
        tk.Button(self.frames["Dashboard"], text="Logout", command=lambda: self.show_frame("Login")).pack(pady=5)

        # Create Product Frame
        self.frames["CreateProduct"] = tk.Frame(self.root)
        tk.Label(self.frames["CreateProduct"], text="Product Name:").pack(pady=5)
        self.product_name_entry = tk.Entry(self.frames["CreateProduct"])
        self.product_name_entry.pack(pady=5)
        tk.Label(self.frames["CreateProduct"], text="Price:").pack(pady=5)
        self.product_price_entry = tk.Entry(self.frames["CreateProduct"])
        self.product_price_entry.pack(pady=5)
        tk.Button(self.frames["CreateProduct"], text="Create", command=self.create_product).pack(pady=10)
        tk.Button(self.frames["CreateProduct"], text="Back", command=lambda: self.show_frame("Dashboard")).pack(pady=5)

        # View Products Frame
        self.frames["ViewProducts"] = tk.Frame(self.root)
        tk.Label(self.frames["ViewProducts"], text="Products List").pack(pady=10)
        self.products_tree = ttk.Treeview(self.frames["ViewProducts"], columns=("ID", "Name", "Price"), show="headings")
        self.products_tree.heading("ID", text="ID")
        self.products_tree.heading("Name", text="Name")
        self.products_tree.heading("Price", text="Price")
        self.products_tree.pack(pady=10)
        tk.Button(self.frames["ViewProducts"], text="Refresh", command=self.load_products).pack(pady=5)
        tk.Button(self.frames["ViewProducts"], text="Back", command=lambda: self.show_frame("Dashboard")).pack(pady=5)

        for frame in self.frames.values():
            frame.pack(fill="both", expand=True)

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)
        if frame_name == "ViewProducts":
            self.load_products()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Simple login check (in real app, hash passwords)
        if username == "admin" and password == "password":
            self.show_frame("Dashboard")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def create_product(self):
        name = self.product_name_entry.get()
        price = self.product_price_entry.get()
        if name and price:
            try:
                cursor = self.db_connection.cursor()
                sql = "INSERT INTO products (name, price) VALUES (?, ?)"
                cursor.execute(sql, (name, float(price)))
                self.db_connection.commit()
                messagebox.showinfo("Success", "Product created successfully")
                self.product_name_entry.delete(0, tk.END)
                self.product_price_entry.delete(0, tk.END)
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Failed to create product: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter name and price")

    def load_products(self):
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id, name, price FROM products")
            products = cursor.fetchall()
            for product in products:
                self.products_tree.insert("", tk.END, values=product)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to load products: {e}")

# Database setup (run this once to create tables)
def setup_database():
    try:
        conn = sqlite3.connect('pos_db.sqlite')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL
            )
        """)
        # Insert default user
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'password')")
        conn.commit()
        conn.close()
        print("Database setup complete.")
    except sqlite3.Error as e:
        print(f"Database setup failed: {e}")

# Run the app
if __name__ == "__main__":
    setup_database()
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()
