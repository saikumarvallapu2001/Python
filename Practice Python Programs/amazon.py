import tkinter as tk
from tkinter import messagebox

# Sample product data (product_id, name, price)
products = {
    1: ("Laptop", 50000.0),
    2: ("Smartphone", 20000.0),
    3: ("Headphones", 2000.0),
    4: ("Smartwatch", 5000.0)
}

# User's shopping cart
cart = {}

# User and Admin credentials
users = {"user": "user123", "admin": "admin123"}
current_user = None

def login():
    global current_user
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        current_user = username
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

def add_to_cart():
    if current_user is None:
        messagebox.showerror("Error", "Please log in first.")
        return
    try:
        product_id = int(product_id_entry.get())
        quantity = int(quantity_entry.get())
        if product_id in products:
            cart[product_id] = cart.get(product_id, 0) + quantity
            messagebox.showinfo("Cart Update", f"Added {quantity} {products[product_id][0]}(s) to cart.")
        else:
            messagebox.showerror("Error", "Invalid product ID!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def view_cart():
    if current_user is None:
        messagebox.showerror("Error", "Please log in first.")
        return
    cart_items = "\n".join([f"{products[pid][0]} - {qty} x Rs. {products[pid][1]}" for pid, qty in cart.items()])
    messagebox.showinfo("Your Cart", cart_items if cart_items else "Cart is empty.")

def place_order():
    if current_user is None:
        messagebox.showerror("Error", "Please log in first.")
        return
    if not cart:
        messagebox.showerror("Error", "Cart is empty! Add items before placing an order.")
        return
    messagebox.showinfo("Order Placed", "Thank you for shopping!")
    cart.clear()

def create_gui():
    global username_entry, password_entry, product_id_entry, quantity_entry
    root = tk.Tk()
    root.title("E-Commerce System")

    tk.Label(root, text="Username:").grid(row=0, column=0)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1)
    
    tk.Label(root, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1)
    
    tk.Button(root, text="Login", command=login).grid(row=2, columnspan=2)
    
    tk.Label(root, text="Product ID:").grid(row=3, column=0)
    product_id_entry = tk.Entry(root)
    product_id_entry.grid(row=3, column=1)
    
    tk.Label(root, text="Quantity:").grid(row=4, column=0)
    quantity_entry = tk.Entry(root)
    quantity_entry.grid(row=4, column=1)
    
    tk.Button(root, text="Add to Cart", command=add_to_cart).grid(row=5, columnspan=2)
    tk.Button(root, text="View Cart", command=view_cart).grid(row=6, columnspan=2)
    tk.Button(root, text="Place Order", command=place_order).grid(row=7, columnspan=2)
    tk.Button(root, text="Exit", command=root.quit).grid(row=8, columnspan=2)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
