import customtkinter as ctk
from PIL import Image
import itertools
import os

# Image Paths (Ensure these images exist in the "assets" folder)
slider_images = ["./assets/banner1.jpg", "./assets/banner2.jpg", "./assets/banner3.jpg", "./assets/banner4.jpg"]
slider_index = itertools.cycle(range(len(slider_images)))  # Infinite loop for cycling images

def update_slider(root):
    """Creates an image slider that updates every 3 seconds."""
    if not slider_images:
        print(" Error: No images found for the slider.")
        return
    
    for img_path in slider_images:
        if not os.path.exists(img_path):
            print(f"Error: Image file {img_path} does not exist!")

    # Slider Frame (Spans the full width)
    slider_frame = ctk.CTkFrame(root, height=250, fg_color="white")
    slider_frame.pack(fill="x", pady=10)

    try:
        img = ctk.CTkImage(light_image=Image.open(slider_images[0]), size=(1600, 250))
        img_label = ctk.CTkLabel(slider_frame, image=img, text="")
        img_label.image = img  # Prevent garbage collection
        img_label.pack()
    except Exception as e:
        print(f" Error loading slider image: {e}")
        return

    def slide():
        """Changes the slider image every 3 seconds."""
        next_index = next(slider_index)  # Get next image index
        print(f"🔄 Updating slider to image: {slider_images[next_index]}")  # Debugging message
        try:
            new_img = ctk.CTkImage(light_image=Image.open(slider_images[next_index]), size=(1600, 250))
            img_label.configure(image=new_img)
            img_label.image = new_img  # Prevent garbage collection
            root.after(3000, slide)  # Change image every 3 seconds
        except Exception as e:
            print(f"❌ Error updating slider image: {e}")

    root.after(3000, slide)  # Start automatic slider
