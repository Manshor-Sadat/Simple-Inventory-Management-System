import tkinter as tk
from tkinter import ttk, messagebox
from Database import get_connection

def search_product(parent_window):
    def execute_search():
       
        product_id = product_id_entry.get().strip()
        product_name = product_name_entry.get().strip()
        category = category_entry.get().strip()
        supplier = supplier_entry.get().strip()
        min_price = min_price_entry.get().strip()
        max_price = max_price_entry.get().strip()
        min_stock = min_stock_entry.get().strip()
        max_stock = max_stock_entry.get().strip()

        query = """
            SELECT p.ProductID, p.ProductName, p.Price, c.CategoryName, s.SupplierName, p.StockLevel
            FROM Products p
            JOIN Categories c ON p.CategoryID = c.CategoryID
            JOIN Suppliers s ON p.SupplierID = s.SupplierID
        """
        filters = []
        parameters = []

        if product_id:
            filters.append("p.ProductID = %s")
            parameters.append(product_id)

        if product_name:
            filters.append("p.ProductName LIKE %s")
            parameters.append(f"%{product_name}%")

        if category:
            filters.append("c.CategoryName LIKE %s")
            parameters.append(f"%{category}%")

        if supplier:
            filters.append("s.SupplierName LIKE %s")
            parameters.append(f"%{supplier}%")

        if min_price:
            filters.append("p.Price >= %s")
            parameters.append(min_price)

        if max_price:
            filters.append("p.Price <= %s")
            parameters.append(max_price)

        if min_stock:
            filters.append("p.StockLevel >= %s")
            parameters.append(min_stock)

        if max_stock:
            filters.append("p.StockLevel <= %s")
            parameters.append(max_stock)

     
        if filters:
            query += " WHERE " + " AND ".join(filters)

        try:
         
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            rows = cursor.fetchall()

            
            for item in result_tree.get_children():
                result_tree.delete(item)

          
            if rows:
                for row in rows:
                    result_tree.insert("", "end", values=row)
            else:
                messagebox.showinfo("No Results", "No matching products found.")

            cursor.close()
            connection.close()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


    search_window = tk.Toplevel(parent_window)
    search_window.title("Search and Filter Products")
    search_window.geometry("1000x700")
    search_window.configure(bg="#FFDAB9")

  
    tk.Label(
        search_window,
        text="Search and Filter Products",
        font=("Helvetica", 16, "bold"),

    ).pack(pady=10)

    filter_frame = tk.Frame(search_window, bg="#FFDAB9")
    filter_frame.pack(fill="x", padx=10, pady=10)

   
    tk.Label(filter_frame, text="Product ID:", font=("Helvetica", 14), bg="#FFDAB9").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    product_id_entry = tk.Entry(filter_frame, font=("Helvetica", 14))
    product_id_entry.grid(row=0, column=1, padx=5, pady=5)

    
    tk.Label(filter_frame, text="Product Name:", font=("Helvetica", 14), bg="#FFDAB9").grid(row=0, column=2, padx=5, pady=5, sticky="w")
    product_name_entry = tk.Entry(filter_frame, font=("Helvetica", 14))
    product_name_entry.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(filter_frame, text="Category:", font=("Helvetica", 14), bg="#FFDAB9").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    category_entry = tk.Entry(filter_frame, font=("Helvetica", 14))
    category_entry.grid(row=1, column=1, padx=5, pady=5)

  
    tk.Label(filter_frame, text="Supplier:", font=("Helvetica", 14), bg="#FFDAB9").grid(row=1, column=2, padx=5, pady=5, sticky="w")
    supplier_entry = tk.Entry(filter_frame, font=("Helvetica", 14))
    supplier_entry.grid(row=1, column=3, padx=5, pady=5)

 
    tk.Label(filter_frame, text="Price Range:", font=("Helvetica", 14), bg="#FFDAB9").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    min_price_entry = tk.Entry(filter_frame, font=("Helvetica", 14), width=10)
    min_price_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Label(filter_frame, text="to", font=("Helvetica", 14), bg="#FFDAB9").grid(row=2, column=2, padx=5, pady=5, sticky="w")
    max_price_entry = tk.Entry(filter_frame, font=("Helvetica", 14), width=10)
    max_price_entry.grid(row=2, column=3, padx=5, pady=5)

  
    tk.Label(filter_frame, text="Stock Level:", font=("Helvetica", 14), bg="#FFDAB9").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    min_stock_entry = tk.Entry(filter_frame, font=("Helvetica", 14), width=10)
    min_stock_entry.grid(row=3, column=1, padx=5, pady=5)
    tk.Label(filter_frame, text="to", font=("Helvetica", 14), bg="#FFDAB9").grid(row=3, column=2, padx=5, pady=5, sticky="w")
    max_stock_entry = tk.Entry(filter_frame, font=("Helvetica", 14), width=10)
    max_stock_entry.grid(row=3, column=3, padx=5, pady=5)

  
    tk.Button(
        filter_frame,
        text="Search",
        font=("Helvetica", 14, "bold"),
        command=execute_search
    ).grid(row=4, column=0, columnspan=4, pady=10)


    result_tree = ttk.Treeview(search_window, columns=("ID", "Name", "Price", "Category", "Supplier", "Stock"), show="headings", height=15)
    result_tree.pack(fill="both", expand=True, padx=10, pady=10)

   
    for col in ["ID", "Name", "Price", "Category", "Supplier", "Stock"]:
        result_tree.heading(col, text=col)
        result_tree.column(col, width=150, anchor="center")

  
    scrollbar = ttk.Scrollbar(search_window, orient="vertical", command=result_tree.yview)
    result_tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    search_window.mainloop()
