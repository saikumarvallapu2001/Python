import customtkinter as ctk
from PIL import Image

def show_product_details(product, root):
    overlay = ctk.CTkFrame(root)
    overlay.place(x=0, y=50, relwidth=1, relheight=1)

    details_frame = ctk.CTkFrame(overlay, fg_color="white", width=600, height=600, corner_radius=10)
    details_frame.place(relx=0.5, rely=0.5, anchor="center")

    img = ctk.CTkImage(light_image=Image.open(product["image"]), size=(400, 300))
    ctk.CTkLabel(details_frame, image=img, text="").pack()

    ctk.CTkLabel(details_frame, text=f"{product['brand']} {product['model']}", font=("Arial", 20, "bold")).pack()
    ctk.CTkLabel(details_frame, text=f"Price: ₹{product['price']}", font=("Arial", 16), text_color="red").pack()
    ctk.CTkButton(details_frame, text="Close", command=overlay.destroy).pack(pady=20)
    ctk.CTkButton(details_frame, text="Cart", command=overlay.destroy).pack(pady=20)
