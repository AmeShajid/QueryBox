import tkinter as tk  # Import the Tkinter library and give it the nickname 'tk'
from tkinter import PhotoImage  # Import the PhotoImage class for handling images
import webbrowser  # Import the webbrowser library to open URLs in the browser

# Function that opens Google search with the query from the entry box
def search_google():
    query = question_entry.get()  # Get the text entered by the user in the entry box
    if query:  # Check if the query is not empty
        url = f"https://www.google.com/search?q={query}"  # Create a Google search URL with the query
        webbrowser.open(url)  # Open the URL in the default web browser
    else:
        tk.messagebox.showwarning("Warning", "Please enter a question.")  # Show a warning if the query is empty

# Main window setup
root = tk.Tk()  # Create the main window of the application
root.title("Ask a Question")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window to 400x300 pixels
root.configure(bg='#f0f0f0')  # Set the background color of the window to light gray

# Create a frame to contain the widgets
frame = tk.Frame(root, bg='#ffffff', padx=20, pady=20, relief='raised', borderwidth=2)  # Create a frame with a white background, padding, raised border, and border width
frame.pack(padx=10, pady=10, expand=True)  # Add the frame to the main window with padding around it and make it expand to fill the space

# Load and display the Google logo
try:
    logo_image = PhotoImage(file="google_logo.png")  # Try to load the Google logo image
    logo_label = tk.Label(frame, image=logo_image, bg='#ffffff')  # Create a label with the logo image and a white background
    logo_label.pack(pady=10)  # Add the label to the frame with padding above and below
except tk.TclError:
    print("Google logo image file not found.")  # Print a message if the image file is not found

# Styling the entry widget
question_entry = tk.Entry(frame, width=40, font=('Arial', 12), bd=2, relief='solid', justify='center')  # Create a text entry box with specific styling
question_entry.pack(pady=10)  # Add the entry box to the frame with padding above and below

# Styling the button widget
search_button = tk.Button(frame, text="Search Google", command=search_google, font=('Arial', 12, 'bold'), bg='#4285F4', fg='white', padx=20, pady=10, relief='raised')  # Create a button with specific styling and set its command to the search_google function
search_button.pack(pady=20)  # Add the button to the frame with padding above and below

# Run the application
root.mainloop()  # Start the Tkinter event loop to display the window and wait for user interactions
