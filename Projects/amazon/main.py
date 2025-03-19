import customtkinter as ctk
from PIL import Image
from auth import show_login_overlay  # Import the login overlay function
from product_details import show_product_details
from products import products, create_product_card
from slider import update_slider  # Import the slider function

def main():
    """Main function to initialize the root window and display the homepage."""
    root = ctk.CTk()  # Initialize the window
    root.title("Amazon Clone")
    root.geometry('1600x900')
    root.configure(bg='#fff')

    # Navbar
    navbar = ctk.CTkFrame(root, fg_color="#232f3e", height=50, corner_radius=0)  
    navbar.pack(fill='x')

    # Reload Logo Image (Create the image each time)
    logo_img = ctk.CTkImage(light_image=Image.open("./assets/logo.png"), size=(100, 50))
    logo_label = ctk.CTkLabel(navbar, image=logo_img, text="")
    logo_label.pack(side="left", padx=50, pady=10)

    # Search Bar Frame
    search_frame = ctk.CTkFrame(navbar, fg_color="#232f3e")  # Keeps search bar and button together
    search_frame.pack(side="left", padx=200, pady=10)

    # Search Bar Input
    search_entry = ctk.CTkEntry(search_frame, width=400, font=('Arial', 12), placeholder_text='Search...', height=40)
    search_entry.pack(side="left", padx=0)

    # Search Button
    search_button = ctk.CTkButton(search_frame, text="Search", fg_color='#FEBD69', height=40, width=80)
    search_button.pack(side="left", padx=0)

    # Navbar Buttons
    sign_in_btn = ctk.CTkButton(navbar, text="Hello, Sign in", fg_color='#232f3e', command=lambda: show_login_overlay(root))
    sign_in_btn.pack(side='left', padx=10)

    returns_btn = ctk.CTkButton(navbar, text="Returns & Orders", fg_color='#232f3e', command=lambda: show_product_details(products[0], root))
    returns_btn.pack(side='left', padx=10)

    cart_btn = ctk.CTkButton(navbar, text="Cart", fg_color='#232f3e')
    cart_btn.pack(side='left', padx=10)

    # Main Content
    main_frame = ctk.CTkScrollableFrame(root, width=1600, height=900)
    main_frame.pack(fill="both", expand=True)

    # Image Slider (Placed Below Navbar)
    update_slider(main_frame)  # Starts the image slider

    # Product Grid
    product_frame = ctk.CTkFrame(main_frame)
    product_frame.pack(pady=20)

    cols = 5
    for index, product in enumerate(products):
        row, col = divmod(index, cols)
        create_product_card(product_frame, product, row, col, root)

    root.mainloop()

if __name__ == "__main__":
    main()
