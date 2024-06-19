import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    """
    Function to assess the strength of a given password.
    It checks for length, complexity (uppercase, lowercase, digits, special characters),
    and uniqueness of characters.
    """
    # Initialize the strength score
    score = 0
    
    # Length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # Complexity: Uppercase, Lowercase, Digits, Special Characters
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[\W_]', password):  # Special characters
        score += 1
    
    # Uniqueness and Entropy
    unique_chars = len(set(password))
    if unique_chars >= len(password) / 2:
        score += 1
    
    # Provide feedback based on the score
    feedback = ""
    if score <= 2:
        feedback = "Very Weak"
    elif score == 3:
        feedback = "Weak"
    elif score == 4:
        feedback = "Moderate"
    elif score == 5:
        feedback = "Strong"
    else:
        feedback = "Very Strong"
    
    return feedback

def on_check_password_strength():
    """
    Function to be called when the 'Check Strength' button is clicked.
    It gets the password from the entry widget, checks its strength,
    and updates the strength label with the feedback.
    """
    password = password_entry.get()
    strength = check_password_strength(password)
    strength_label.config(text=f"Password Strength: {strength}")

# Initialize the main application window
root = tk.Tk()
root.title("Password Strength Checker")

# Set the size of the window
root.geometry("400x300")

# Create a label for the password entry
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

# Create an entry widget to input the password
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

# Create a button to check the password strength
check_button = tk.Button(root, text="Check Strength", command=on_check_password_strength)
check_button.pack(pady=20)

# Create a label to display the password strength
strength_label = tk.Label(root, text="", font=("Helvetica", 12))
strength_label.pack(pady=10)

# Run the main application loop
root.mainloop()
