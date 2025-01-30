import tkinter as tk
from tkinter import messagebox, ttk
from Database import get_connection

def delete_product(root):
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

    def confirm_and_delete():
        selected_item = result_tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a product to delete!")
            return

        try:
         
            selected_row = result_tree.item(selected_item, 'values')
            product_id = selected_row[0]  

            connection = get_connection()
            cursor = connection.cursor()

          
            cursor.execute("DELETE FROM Products WHERE ProductID = %s", (int(product_id),))
            connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Product deleted successfully!")
                result_tree.delete(selected_item)  
            else:
                messagebox.showinfo("Error", "Product could not be deleted!")

            cursor.close()
            connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Product")
    delete_window.geometry("900x600")
    delete_window.configure(bg="#FFDAB9")  

  
    tk.Label(delete_window, text="Delete Product", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#333333").grid(row=0, column=0, columnspan=3, pady=10)

   
    tk.Label(delete_window, text="Search By:", font=("Helvetica", 12), bg="#FFFFFF", fg="#333333").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    search_by_var = tk.StringVar(value="ProductID")
    search_by_options = ["ProductID", "ProductName", "Price"]
    search_by_menu = ttk.Combobox(delete_window, textvariable=search_by_var, values=search_by_options, state="readonly", font=("Helvetica", 12))
    search_by_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

   
    tk.Label(delete_window, text="Search Term:", font=("Helvetica", 12), bg="#FFFFFF", fg="#333333").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    search_entry = tk.Entry(delete_window, font=("Helvetica", 12), width=30)
    search_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    
    tk.Button(
        delete_window,
        text="Search",
        font=("Helvetica", 12, "bold"),
    
        command=search_product
    ).grid(row=2, column=2, padx=10, pady=10)

   
    result_tree = ttk.Treeview(delete_window, columns=("ProductID", "Name", "Price", "Category", "Supplier", "Stock"), show="headings", height=15)
    result_tree.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

    for col in ["ProductID", "Name", "Price", "Category", "Supplier", "Stock"]:
        result_tree.heading(col, text=col)
        result_tree.column(col, width=120, anchor="center")  

   
    scrollbar = ttk.Scrollbar(delete_window, orient="vertical", command=result_tree.yview)
    result_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=3, column=3, sticky="ns")

    tk.Button(
        delete_window,
        text="Delete Selected",
        font=("Helvetica", 12, "bold"),
    
        command=confirm_and_delete
    ).grid(row=4, column=0, columnspan=3, pady=20)

    delete_window.mainloop()