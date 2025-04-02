import customtkinter as ctk

def logout(root):
    """Logs out the user and returns to the main login page."""
    from auth import show_login_overlay  # ✅ Import inside function

    for widget in root.winfo_children():
        widget.destroy()

    show_login_overlay(root)
