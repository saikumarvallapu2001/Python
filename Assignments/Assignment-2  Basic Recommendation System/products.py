import customtkinter as ctk
from PIL import Image

from product_details import show_product_details

products = [
     {"brand": "Samsung", "model": "Galaxy S24", "rating": 4.7, "price": 79999, "color": ("Black", "Silver"), "prime": True, "image": "./assets/product1.jpg"},
    {"brand": "Apple", "model": "iPhone 15", "rating": 4.8, "price": 99999, "color": ("Blue", "Green"), "prime": True, "image": "./assets/product2.jpg"},
    {"brand": "OnePlus", "model": "11 Pro", "rating": 4.6, "price": 64999, "color": ("Black", "Red"), "prime": False, "image": "./assets/product3.jpg"},
    {"brand": "Xiaomi", "model": "13 Pro", "rating": 4.5, "price": 57999, "color": ("White", "Black"), "prime": True, "image": "./assets/product4.jpg"},
    {"brand": "Google", "model": "Pixel 8", "rating": 4.7, "price": 72999, "color": ("Gray", "Blue"), "prime": False, "image": "./assets/product5.jpg"},
    {"brand": "Realme", "model": "GT Neo", "rating": 4.4, "price": 39999, "color": ("Blue", "Orange"), "prime": True, "image": "./assets/product6.jpg"},
    {"brand": "Vivo", "model": "X90 Pro", "rating": 4.6, "price": 68999, "color": ("Black", "Silver"), "prime": True, "image": "./assets/product7.jpg"},
    {"brand": "Oppo", "model": "Find X6", "rating": 4.3, "price": 59999, "color": ("Gold", "Black"), "prime": False, "image": "./assets/product8.jpg"},
    {"brand": "Nothing", "model": "Phone 2", "rating": 4.2, "price": 44999, "color": ("White", "Transparent"), "prime": True, "image": "./assets/product9.jpg"},
    {"brand": "Motorola", "model": "Edge 40", "rating": 4.5, "price": 52999, "color": ("Black", "Blue"), "prime": False, "image": "./assets/product10.jpg"}
]

def create_product_card(parent, product, row, col, root):
    frame = ctk.CTkFrame(parent, width=300, height=400, fg_color='white')
    frame.grid(row=row, column=col, padx=10, pady=10)

    img = ctk.CTkImage(light_image=Image.open(product["image"]), size=(250, 200))
    img_label = ctk.CTkLabel(frame, image=img, text="")
    img_label.pack()

    ctk.CTkLabel(frame, text=f"{product['brand']} {product['model']}", font=("Arial", 16)).pack()
    ctk.CTkLabel(frame, text=f"₹{product['price']}", font=("Arial", 14), text_color="red").pack()
    ctk.CTkButton(frame, text="View", command=lambda: show_product_details(product, root)).pack(pady=5)
