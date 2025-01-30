import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  
from Database import get_connection
import datetime


def log_transaction(root):
    def submit():
        product_id = product_var.get().split(":")[0]  
        quantity = entry_quantity.get()
        transaction_type = transaction_type_var.get()
        transaction_date = date_entry.get()  

        if not (product_id and quantity and transaction_type and transaction_date):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

  
        try:
            transaction_date_obj = datetime.datetime.strptime(transaction_date, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Date Error", "Please enter a valid date in YYYY-MM-DD format.")
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

         
            cursor.execute(
                "INSERT INTO Transactions (ProductID, Quantity, TransactionDate, TransactionType) VALUES (%s, %s, %s, %s)",
                (int(product_id), int(quantity), transaction_date_obj, transaction_type)
            )

           
            if transaction_type == "IN":
                cursor.execute(
                    "UPDATE Products SET StockLevel = StockLevel + %s WHERE ProductID = %s",
                    (int(quantity), int(product_id))
                )
            elif transaction_type == "OUT":
                cursor.execute(
                    "UPDATE Products SET StockLevel = StockLevel - %s WHERE ProductID = %s",
                    (int(quantity), int(product_id))
                )

            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Transaction logged successfully!")
            transaction_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

   
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT ProductID, ProductName FROM Products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()

 
    transaction_window = tk.Toplevel(root)
    transaction_window.title("Log Transaction")
    transaction_window.geometry("800x600")
    transaction_window.configure(bg="#FFDAB9")  

  
    label_style = {
        "font": ("Helvetica", 12, "bold"),
        "bg": "#FFDAB9",
        "fg": "#333333",
    }

    input_style = {
        "font": ("Helvetica", 12),
        "bg": "#FFFFFF",
        "fg": "#333333",
        "relief": "solid",
    }

    tk.Label(
        transaction_window,
        text="Log Transaction",
        font=("Helvetica", 16, "bold"),
        bg="#FFDAB9",
        fg="#333333"
    ).pack(pady=10)

   
    tk.Label(transaction_window, text="Product:", **label_style).pack(anchor="w", padx=20, pady=5)
    product_var = tk.StringVar(transaction_window)
    product_dropdown = ttk.OptionMenu(transaction_window, product_var, "Select a product", *[f"{p[0]}: {p[1]}" for p in products])
    product_dropdown.pack(fill="x", padx=20, pady=5)

 
    tk.Label(transaction_window, text="Quantity:", **label_style).pack(anchor="w", padx=20, pady=5)
    entry_quantity = tk.Entry(transaction_window, **input_style)
    entry_quantity.pack(fill="x", padx=20, pady=5)

  
    tk.Label(transaction_window, text="Transaction Type:", **label_style).pack(anchor="w", padx=20, pady=5)
    transaction_type_var = tk.StringVar(transaction_window)
    ttk.OptionMenu(transaction_window, transaction_type_var, "Select type", "IN", "OUT").pack(fill="x", padx=20, pady=5)

    
    tk.Label(transaction_window, text="Transaction Date:", **label_style).pack(anchor="w", padx=20, pady=5)
    date_entry = DateEntry(
        transaction_window,
        font=("Helvetica", 12),
        width=18,
        background="darkblue",
        foreground="white",
        borderwidth=2,
        date_pattern="yyyy-MM-dd"  
    )
    date_entry.set_date(datetime.date.today())  
    date_entry.pack(fill="x", padx=20, pady=5)

    tk.Button(
        transaction_window,
        text="Submit",
        font=("Helvetica", 14, "bold"),
        command=submit
    ).pack(pady=20)


def show_transactions(root):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT TransactionID, ProductID, Quantity, TransactionDate, TransactionType 
            FROM Transactions
        """)
        transactions = cursor.fetchall()
        cursor.close()
        connection.close()

        if not transactions:
            messagebox.showinfo("No Transactions", "No transactions available.")
            return

  
        transaction_window = tk.Toplevel(root)
        transaction_window.title("Transactions")
        transaction_window.geometry("800x400")  

        tree = ttk.Treeview(transaction_window, columns=("ID", "ProductID", "Quantity", "Date", "Type"), show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        
        tree.heading("ID", text="Transaction ID")
        tree.column("ID", width=100, anchor="center")

        tree.heading("ProductID", text="Product ID")
        tree.column("ProductID", width=100, anchor="center")

        tree.heading("Quantity", text="Quantity")
        tree.column("Quantity", width=100, anchor="center")

        tree.heading("Date", text="Transaction Date")
        tree.column("Date", width=150, anchor="center")

        tree.heading("Type", text="Transaction Type")
        tree.column("Type", width=100, anchor="center")

     
        scrollbar = ttk.Scrollbar(transaction_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

     
        for row in transactions:
            tree.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
