import customtkinter as ctk
from PIL import Image

def show_admin_dashboard(root):
    """Displays the admin dashboard with a navbar and a logout button."""
    from utils import logout  # ✅ Import inside function

    # Clear previous content
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar (Same as main page, but without extra buttons)
    navbar = ctk.CTkFrame(root, fg_color="#232f3e", height=50, corner_radius=0)
    navbar.pack(fill='x')

    # ✅ Corrected: Load Amazon Logo using PIL.Image
    try:
        logo_img = ctk.CTkImage(light_image=Image.open("./assets/logo.png"), size=(100, 50))
        logo_label = ctk.CTkLabel(navbar, image=logo_img, text="")
        logo_label.pack(side="left", padx=50, pady=10)
    except Exception as e:
        print(f"Error loading logo image: {e}")


    admin_label=ctk.CTkLabel(navbar,  text="Admin Dashboard",text_color='white', font=("Arial", 22, "bold")).pack(side='left',padx=200,pady=20)
    

    # Logout Button
    logout_button = ctk.CTkButton(navbar, text="Logout", fg_color="#D9534F", text_color="white", command=lambda: logout(root))
    logout_button.pack(side='left',padx=300, pady=20)


    
    # Admin Dashboard Content
    admin_frame = ctk.CTkFrame(admin_frame, fg_color="white", width=800, height=500)
    admin_frame.place(relx=0.5, rely=0.5, anchor="center")
