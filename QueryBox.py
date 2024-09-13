import tkinter as tk
from tkinter import messagebox

# Function that shows the pop-up when called
def show_popup():
    messagebox.showinfo("Pop-up", "Here is the information you asked for!")

# Main window setup
root = tk.Tk()
root.title("Ask a Question")

# Button that triggers the pop-up
ask_button = tk.Button(root, text="Ask me a question", command=show_popup)
ask_button.pack(pady=20)

# Run the application
root.mainloop()
