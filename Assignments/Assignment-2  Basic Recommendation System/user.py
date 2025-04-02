import customtkinter as ctk
from PIL import Image
from product_details import show_product_details
from products import products, create_product_card
from slider import update_slider

def show_user_dashboard(root, user_id):  
    """Displays the user dashboard."""
    from utils import logout  # Import inside function

    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar
    navbar = ctk.CTkFrame(root, fg_color="#232f3e", height=50, corner_radius=0)
    navbar.pack(fill='x', side='top')

    # ✅ Amazon Logo
    try:
        logo_img = ctk.CTkImage(light_image=Image.open("./assets/logo.png"), size=(100, 50))
        logo_label = ctk.CTkLabel(navbar, image=logo_img, text="")
        logo_label.pack(side="left", padx=50, pady=10)
    except Exception as e:
        print(f"Error loading logo image: {e}")

    # ✅ Search Bar
    search_frame = ctk.CTkFrame(navbar, fg_color="#232f3e")
    search_frame.pack(side="left", padx=100, pady=10)

    search_entry = ctk.CTkEntry(search_frame, width=400, font=('Arial', 12), placeholder_text='Search...', height=40)
    search_entry.pack(side="left", padx=5)

    search_button = ctk.CTkButton(search_frame, text="Search", fg_color='#FEBD69', height=40, width=80)
    search_button.pack(side="left", padx=5)

    # ✅ Display User ID Next to "Welcome"
    user_label = ctk.CTkLabel(navbar, text=f"Welcome, {user_id}", font=("Arial", 12), text_color="white")
    user_label.pack(side='left', padx=50, pady=10)

    # ✅ Navigation Buttons
    returns_btn = ctk.CTkButton(navbar, text="Returns & Orders", fg_color='#232f3e', text_color="white",
                                command=lambda: show_product_details(products[0], root))
    returns_btn.pack(side='left', padx=10)

    cart_btn = ctk.CTkButton(navbar, text="Cart", fg_color='#232f3e', text_color="white")
    cart_btn.pack(side='left', padx=10)

    logout_button = ctk.CTkButton(navbar, text="Logout", fg_color="#D9534F", text_color="white", command=lambda: logout(root))
    logout_button.pack(side='right', padx=20)

    # ✅ Main Content Frame (Scrollable)
    main_frame = ctk.CTkScrollableFrame(root, width=1600, height=900)
    main_frame.pack(fill="both", expand=True)

    # ✅ Image Slider (Below Navbar)
    update_slider(main_frame)  

    # ✅ Product Grid
    product_frame = ctk.CTkFrame(main_frame)
    product_frame.pack(pady=20)

    cols = 5
    for index, product in enumerate(products):
        row, col = divmod(index, cols)
        create_product_card(product_frame, product, row, col, root)
