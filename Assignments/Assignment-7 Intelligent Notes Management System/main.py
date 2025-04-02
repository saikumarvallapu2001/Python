import os
import re
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Define positive and negative word lists
positive_words = ["good", "great", "excellent", "happy", "love", "positive", "success"]
negative_words = ["bad", "sad", "terrible", "worst", "hate", "negative", "failure"]

# Ensure the 'usernotes' directory exists
if not os.path.exists("usernotes"):
    os.makedirs("usernotes")

def analyze_note():
    """Analyze a specific note for sentiment."""
    filename = filedialog.askopenfilename(initialdir="usernotes", title="Select a Note",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if not filename:
        return
    
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().lower()
    
    positive_count = len(re.findall(r'\b(' + '|'.join(positive_words) + r')\b', content))
    negative_count = len(re.findall(r'\b(' + '|'.join(negative_words) + r')\b', content))

    result = f"Positive words: {positive_count}, Negative words: {negative_count}\n"
    if positive_count > negative_count:
        result += "Overall Sentiment: Positive 😊"
    elif negative_count > positive_count:
        result += "Overall Sentiment: Negative 😞"
    else:
        result += "Overall Sentiment: Neutral 😐"
    
    messagebox.showinfo("Sentiment Analysis", result)

def create_note():
    """Create a new note."""
    filename = simpledialog.askstring("New Note", "Enter filename (without extension):")
    if not filename:
        return
    filename += ".txt"
    content = simpledialog.askstring("Note Content", "Enter note content:")
    
    with open(f"usernotes/{filename}", "w", encoding="utf-8") as file:
        file.write(content)
    
    messagebox.showinfo("Success", f"Note '{filename}' created successfully!")

def modify_note():
    """Modify an existing note."""
    filename = filedialog.askopenfilename(initialdir="usernotes", title="Select a Note to Modify",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if not filename:
        return
    
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    new_content = simpledialog.askstring("Edit Note", "Modify the content:", initialvalue=content)
    if new_content is None:
        return
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_content)
    
    messagebox.showinfo("Success", f"Note '{os.path.basename(filename)}' updated successfully!")

def main():
    """Main GUI Window."""
    root = tk.Tk()
    root.title("Intelligent Notes Management System")
    root.geometry("400x300")
    
    tk.Label(root, text="Notes Management System", font=("Arial", 14, "bold")).pack(pady=10)
    
    tk.Button(root, text="Analyze Note", command=analyze_note, width=20, height=2).pack(pady=5)
    tk.Button(root, text="Create Note", command=create_note, width=20, height=2).pack(pady=5)
    tk.Button(root, text="Modify Note", command=modify_note, width=20, height=2).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=20, height=2, bg="red", fg="white").pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
