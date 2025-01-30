import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
from Add_Product import add_product
from Delete_Product import delete_product
from Show_Product import show_products
from Update_Stock import update_stock
from Show_Transaction import show_transactions
from Show_Transaction import log_transaction
from Search_Product import search_product 

USER_CREDENTIALS = {"admin": "pass123"}

def sign_in_page():
    def authenticate():
        username = username_entry.get()
        password = password_entry.get()

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            messagebox.showinfo("Login Successful", "Welcome to the Inventory Management System!")
            root.destroy() 
            main_gui()  
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    root = tk.Tk()
    root.title("Sign In")
    root.geometry("850x650")  
    root.resizable(False, False)  

   
    def set_background(image_path):
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_photo

    set_background("icons/invent.jpg")  
    tk.Label(
        root,
        text="Sign In",
        font=("Helvetica", 26, "bold"),
        bg="#FFFFFF",  
        fg="#333333"
    ).place(x=400, y=195)  

   
    tk.Label(
        root, 
        text="Username:", 
        font=("Helvetica", 14), 
        bg="#FFFFFF", 
        fg="#333333"
    ).place(x=200, y=250)
    username_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
    username_entry.place(x=320, y=250)

    tk.Label(
        root, 
        text="Password:", 
        font=("Helvetica", 14), 
        bg="#FFFFFF", 
        fg="#333333"
    ).place(x=200, y=300)
    password_entry = tk.Entry(root, font=("Helvetica", 14), width=30, show="*")
    password_entry.place(x=320, y=300)


    tk.Button(
        root, 
        text="Login", 
        font=("Helvetica", 14), 
        width=15,
        command=authenticate
    ).place(x=365, y=380)

   
 

    root.mainloop()


def main_gui():
    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("1366x768")  
    root.configure(bg="#FFDAB9")

    
    title_label = tk.Label(
        root,
        text="Inventory Management System",
        font=("Helvetica", 28, "bold"),
        bg="#FFDAB9",
        fg="#333333"
    )
    title_label.pack(pady=24)

    def set_background(image_path):
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((1366, 600), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_photo

    set_background("icons/invv.png")

 
    button_frame = tk.Frame(root, bg="#FFDAB9")
    button_frame.pack(pady=40)

    def load_icon(file_path, size=(60, 60)):  
        image = Image.open(file_path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

    add_icon = load_icon("icons/box.png")
    update_icon = load_icon("icons/update.png")
    delete_icon = load_icon("icons/delete-product.png")
    show_icon = load_icon("icons/shopping-bag.png")
    transaction_icon = load_icon("icons/time.png")
    log_transaction_icon = load_icon("icons/transaction.png")
    search_icon = load_icon("icons/search.png") 


    button_style = {
        "font": ("Helvetica", 14, "bold"),
        "bd": 4,
        "cursor": "hand2",
        "compound": "top", 
        "padx": 10,
        "pady": 10,
    }

   
    tk.Button(button_frame, text="Add Product", image=add_icon, command=lambda: add_product(root), **button_style).grid(row=0, column=0, padx=15, pady=15)
    tk.Button(button_frame, text="Update Stock", image=update_icon, command=lambda: update_stock(root), **button_style).grid(row=0, column=1, padx=15, pady=15)
    tk.Button(button_frame, text="Delete Product", image=delete_icon, command=lambda: delete_product(root), **button_style).grid(row=0, column=2, padx=15, pady=15)
    tk.Button(button_frame, text="Show Products", image=show_icon, command=lambda: show_products(root), **button_style).grid(row=0, column=3, padx=15, pady=15)
    tk.Button(button_frame, text="Log Transaction", image=transaction_icon, command=lambda: log_transaction(root), **button_style).grid(row=0, column=4, padx=15, pady=15)
    tk.Button(button_frame, text="Log Transaction", image=log_transaction_icon, command=lambda: log_transaction(root), **button_style).grid(row=0, column=4, padx=15, pady=15)
    tk.Button(button_frame, text="Show Transactions", image=transaction_icon, command=lambda: show_transactions(root), **button_style).grid(row=0, column=5, padx=15, pady=15)
    tk.Button(button_frame, text="Search Product", image=search_icon, command=lambda: search_product(root), **button_style).grid(row=0, column=6, padx=15, pady=15)

   

  

    root.mainloop()


sign_in_page()
