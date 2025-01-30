import tkinter as tk
from tkinter import messagebox
from Database import get_connection

def add_product(root):
    def submit():
        name = entry_name.get()
        category = category_var.get().split(":")[0]
        supplier = supplier_var.get().split(":")[0]
        stock = entry_stock.get()
        price = entry_price.get()
        unit = unit_var.get()

        if not (name and category and supplier and stock and price and unit):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Products (ProductName, CategoryID, SupplierID, StockLevel, Price, Unit) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, int(category), int(supplier), int(stock), float(price), unit)
            )
            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Product added successfully!")
            add_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
    categories = cursor.fetchall()
    cursor.execute("SELECT SupplierID, SupplierName FROM Suppliers")
    suppliers = cursor.fetchall()
    cursor.close()
    connection.close()

    add_window = tk.Toplevel(root)
    add_window.title("Add Product")
    add_window.geometry("800x600")
    add_window.configure(bg="#FFDAB9")  

   
    label_style = {
        "font": ("Helvetica", 14, "bold"),
        "bg": "#FFDAB9",  
        "fg": "#333333",  
    }
    input_style = {
        "font": ("Helvetica", 12),
        "bg": "#FFFFFF",  
        "fg": "#333333",  
        "bd": 0,          
        "highlightthickness": 0  
    }

    tk.Label(add_window, text="Add Product", **label_style).pack(pady=10)

    tk.Label(add_window, text="Product Name:", **label_style).pack(anchor="w", padx=20, pady=5)
    entry_name = tk.Entry(add_window, **input_style)
    entry_name.pack(fill="x", padx=20, pady=5)

    tk.Label(add_window, text="Category:", **label_style).pack(anchor="w", padx=20, pady=5)
    category_var = tk.StringVar(add_window)
    category_var.set("Select a Category")
    category_dropdown = tk.OptionMenu(add_window, category_var, *[f"{c[0]}: {c[1]}" for c in categories])
    category_dropdown.config(font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", bd=0, highlightthickness=0)
    category_dropdown.pack(fill="x", padx=20, pady=5)

    tk.Label(add_window, text="Supplier:", **label_style).pack(anchor="w", padx=20, pady=5)
    supplier_var = tk.StringVar(add_window)
    supplier_var.set("Select a Supplier")
    supplier_dropdown = tk.OptionMenu(add_window, supplier_var, *[f"{s[0]}: {s[1]}" for s in suppliers])
    supplier_dropdown.config(font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", bd=0, highlightthickness=0)
    supplier_dropdown.pack(fill="x", padx=20, pady=5)

    tk.Label(add_window, text="Stock Level:", **label_style).pack(anchor="w", padx=20, pady=5)
    entry_stock = tk.Entry(add_window, **input_style)
    entry_stock.pack(fill="x", padx=20, pady=5)

    tk.Label(add_window, text="Price:", **label_style).pack(anchor="w", padx=20, pady=5)
    entry_price = tk.Entry(add_window, **input_style)
    entry_price.pack(fill="x", padx=20, pady=5)

    tk.Label(add_window, text="Unit:", **label_style).pack(anchor="w", padx=20, pady=5)
    unit_var = tk.StringVar(add_window)
    unit_var.set("Select a Unit")
    unit_dropdown = tk.OptionMenu(add_window, unit_var, "kg", "liters", "pcs", "packs", "meters")
    unit_dropdown.config(font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", bd=0, highlightthickness=0)
    unit_dropdown.pack(fill="x", padx=20, pady=5)

    tk.Button(
        add_window,
        text="Submit",
        font=("Helvetica", 14, "bold"),
    
        relief="flat", 
        command=submit
    ).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    add_product(root)
    root.mainloop()
