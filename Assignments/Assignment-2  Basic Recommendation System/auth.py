import customtkinter as ctk
from tkinter import messagebox
from user import show_user_dashboard

# ✅ Store user credentials (For real projects, use a database)
users = {"admin": {"password": "admin123", "phone": "0000000000", "user_id": "admin1", "role": "admin"},
         "saikumar": {"password":"1919sai","phone":"6301516308","user_id":"Sai Kumar", "role":"user"}}


def login(email, password, overlay, root):
    """Handles login logic."""
    from user import show_user_dashboard  # ✅ Import inside function

    if email in users and users[email]["password"] == password:
        user_id = users[email]["user_id"]  # Get User ID
        messagebox.showinfo("Success", f"Login Successful! Welcome, {user_id}")
        overlay.destroy()
        show_user_dashboard(root, user_id)  # ✅ Pass user_id
    else:
        messagebox.showerror("Error", "Invalid email or password")

def show_login_overlay(root):
    """Displays the login page."""
    overlay = ctk.CTkFrame(root)
    overlay.place(x=0, y=80, relwidth=1, relheight=1)

    login_frame = ctk.CTkFrame(overlay, fg_color="#ffffff", width=400, height=400, corner_radius=10)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkLabel(login_frame, text='Sign In', font=("Arial", 22, "bold")).pack(pady=10)
    email_input = ctk.CTkEntry(login_frame, width=250, placeholder_text="Email")
    email_input.pack(pady=5)

    password_input = ctk.CTkEntry(login_frame, width=250, show='*', placeholder_text="Password")
    password_input.pack(pady=5)

    ctk.CTkButton(login_frame, text='Login', fg_color='#FFD814', text_color='#0F1111', 
                  command=lambda: login(email_input.get(), password_input.get(), overlay, root)).pack(pady=10)

    ctk.CTkButton(login_frame, text="Sign Up", fg_color='#FFD814', text_color='#0F1111',
                  command=lambda: show_register_overlay(root, overlay)).pack()
    from main import main;
    ctk.CTkButton(login_frame, text='go back to home', fg_color='#ffd814', command=lambda:main(root, main) ).pack()


def show_register_overlay(root, overlay):
    """Displays the user registration form with additional fields."""
    overlay.destroy()  

    register_overlay = ctk.CTkFrame(root)
    register_overlay.place(x=0, y=80, relwidth=1, relheight=1)

    register_frame = ctk.CTkFrame(register_overlay, fg_color="#ffffff", width=400, height=500, corner_radius=10)
    register_frame.place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkLabel(register_frame, text='Sign Up', font=("Arial", 22, "bold")).pack(pady=10)

    email_input = ctk.CTkEntry(register_frame, width=250, placeholder_text="Email")
    email_input.pack(pady=5)

    password_input = ctk.CTkEntry(register_frame, width=250, show='*', placeholder_text="Password")
    password_input.pack(pady=5)

    phone_input = ctk.CTkEntry(register_frame, width=250, placeholder_text="Phone Number")
    phone_input.pack(pady=5)

    user_id_input = ctk.CTkEntry(register_frame, width=250, placeholder_text="User ID")
    user_id_input.pack(pady=5)

    ctk.CTkButton(register_frame, text='Register', fg_color='#FFD814', text_color='#0F1111',
                  command=lambda: register_user(email_input.get(), password_input.get(), phone_input.get(), user_id_input.get(), register_overlay, root)).pack(pady=10)

    ctk.CTkButton(register_frame, text="Back to Login", fg_color='#FFD814', text_color='#0F1111',
                  command=lambda: show_login_overlay(root)).pack()

def register_user(email, password, phone, user_id, overlay, root):
    """Handles user registration with additional fields."""
    if email in users:
        messagebox.showerror("Error", "User already exists")
    elif not email or not password or not phone or not user_id:
        messagebox.showerror("Error", "All fields are required!")
    elif not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Enter a valid 10-digit phone number")
    else:
        users[email] = {"password": password, "phone": phone, "user_id": user_id, "role": "user"}
        messagebox.showinfo("Success", "Account created successfully! You can now log in.")
        overlay.destroy()
        show_login_overlay(root)  
