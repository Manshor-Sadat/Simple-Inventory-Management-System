import tkinter as tk
from tkinter import messagebox, ttk
from Database import get_connection

def update_stock(root):
    def search_product():
        search_by = search_by_var.get()
        search_term = search_entry.get()

        if not search_term:
            messagebox.showwarning("Input Error", "Please enter a search term!")
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

           
            query = f"SELECT * FROM Products WHERE {search_by} LIKE %s"
            cursor.execute(query, ('%' + search_term + '%',))
            rows = cursor.fetchall()

            if not rows:
                messagebox.showinfo("No Results", "No matching products found.")
            else:
              
                for item in result_tree.get_children():
                    result_tree.delete(item)

               
                for row in rows:
                    result_tree.insert("", "end", values=row)

            cursor.close()
            connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_selected_stock():
        selected_item = result_tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a product to update!")
            return

        new_stock = entry_new_stock.get()
        if not new_stock:
            messagebox.showwarning("Input Error", "Please enter the new stock level!")
            return

        try:
          
            selected_row = result_tree.item(selected_item, 'values')
            product_id = selected_row[0] 

            connection = get_connection()
            cursor = connection.cursor()

          
            cursor.execute(
                "UPDATE Products SET StockLevel = %s WHERE ProductID = %s",
                (int(new_stock), int(product_id))
            )
            connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Stock level updated successfully!")
               
                selected_row = list(selected_row)
                selected_row[5] = new_stock  
                result_tree.item(selected_item, values=selected_row)
            else:
                messagebox.showinfo("Error", "Stock level could not be updated!")

            cursor.close()
            connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

   
    update_window = tk.Toplevel(root)
    update_window.title("Update Stock")
    update_window.geometry("900x700")
    update_window.configure( bg = "#FFDAB9" )  
  
    label_style = {"font": ("Helvetica", 14, "bold"), "bg": "#F0F0F0", "fg": "#333333"}
    entry_style = {"font": ("Helvetica", 14), "bg": "#FFFFFF", "fg": "#333333"}

   
    tk.Label(update_window, text="Search By:", **label_style).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    search_by_var = tk.StringVar(value="ProductID")
    search_by_options = ["ProductID", "ProductName", "Price"]
    search_by_menu = ttk.Combobox(update_window, textvariable=search_by_var, values=search_by_options, state="readonly", font=("Helvetica", 14))
    search_by_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

 
    tk.Label(update_window, text="Search Term:", **label_style).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    search_entry = tk.Entry(update_window, **entry_style, width=30)
    search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

  
    tk.Button(
        update_window,
        text="Search",
        font=("Helvetica", 14, "bold"),
        command=search_product
    ).grid(row=1, column=2, padx=10, pady=10, sticky="w")

  
    result_tree = ttk.Treeview(update_window, columns=("ProductID", "Name", "Price", "Category", "Supplier", "Stock"), show="headings", height=15)
    result_tree.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

   
    for col in ["ProductID", "Name", "Price", "Category", "Supplier", "Stock"]:
        result_tree.heading(col, text=col)
        result_tree.column(col, width=140, anchor="center")

    
    scrollbar = ttk.Scrollbar(update_window, orient="vertical", command=result_tree.yview)
    result_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=2, column=3, sticky="ns")

  
    tk.Label(update_window, text="New Stock Level:", **label_style).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_new_stock = tk.Entry(update_window, **entry_style, width=30)
    entry_new_stock.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    tk.Button(
        update_window,
        text="Update Stock",
        font=("Helvetica", 14, "bold"),
     
        command=update_selected_stock
    ).grid(row=4, column=0, columnspan=3, pady=20)

    update_window.mainloop()
