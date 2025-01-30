import tkinter as tk
from tkinter import messagebox, ttk
from Database import get_connection

def show_products(root):
    def fetch_products():
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Products")
            products = cursor.fetchall()
            cursor.close()
            connection.close()

            if not products:
                messagebox.showinfo("No Products", "No products available in the inventory.")
                return
            
        
            show_window = tk.Toplevel(root)
            show_window.title("Products List")
            show_window.geometry("800x400")  

            tree = ttk.Treeview(show_window, columns=("ID", "Name", "CategoryID", "SupplierID", "StockLevel", "Price"), show="headings")
            tree.pack(fill="both", expand=True, padx=10, pady=10)

          
            tree.heading("ID", text="ID")
            tree.column("ID", width=50, anchor="center")

            tree.heading("Name", text="Product Name")
            tree.column("Name", width=200, anchor="w")

            tree.heading("CategoryID", text="Category ID")
            tree.column("CategoryID", width=100, anchor="center")

            tree.heading("SupplierID", text="Supplier ID")
            tree.column("SupplierID", width=100, anchor="center")

            tree.heading("StockLevel", text="Stock Level")
            tree.column("StockLevel", width=100, anchor="center")

            tree.heading("Price", text="Price")
            tree.column("Price", width=100, anchor="center")

            scrollbar = ttk.Scrollbar(show_window, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")

         
            for row in products:
                tree.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    fetch_products()
