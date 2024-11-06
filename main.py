#This code will run by itself, but its is not hooked up to a database. Also the program is very basic in design.
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pandas as pd


class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        # Set initial window size
        self.root.geometry("300x200")
       
        # Set custom icon (Make sure you have an "icon.ico" file in the same directory)
        self.root.iconphoto(False, tk.PhotoImage(file="finance_tracker_app.ico"))  # Replace with your icon path

        # Set background color
        self.root.configure(bg="#f0f4f8")  # Light background color

        # Make the grid layout responsive
        self.root.columnconfigure(1, weight=1)
        for i in range(3):
            self.root.rowconfigure(i, weight=1)

        # Initialize data storage
        self.data = pd.DataFrame(columns=["Date", "Description", "Amount"])

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for Date with custom colors
        tk.Label(self.root, text="Date:", bg="#f0f4f8", fg="#333333", font=("Arial", 10)).grid(row=0, column=0,
                                                                                               sticky="e")
        self.date_entry = DateEntry(self.root, width=12, background='#0066cc', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Label and Entry for Description
        tk.Label(self.root, text="Description:", bg="#f0f4f8", fg="#333333", font=("Arial", 10)).grid(row=1, column=0,
                                                                                                      sticky="e")
        self.desc_entry = tk.Entry(self.root, bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.desc_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Label and Entry for Amount
        tk.Label(self.root, text="Amount:", bg="#f0f4f8", fg="#333333", font=("Arial", 10)).grid(row=2, column=0,
                                                                                                 sticky="e")
        self.amount_entry = tk.Entry(self.root, bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.amount_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Add Entry Button with custom colors
        add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry, bg="#4caf50", fg="white",
                               font=("Arial", 10))
        add_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Display Entries Button with custom colors
        display_button = tk.Button(self.root, text="Display Entries", command=self.display_entries, bg="#2196f3",
                                   fg="white", font=("Arial", 10))
        display_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def add_entry(self):
        date = self.date_entry.get()  # Get date from DateEntry widget
        description = self.desc_entry.get()
        amount = self.amount_entry.get()

        # Validate input fields
        if not date or not description or not amount:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        # Validate amount as a float
        try:
            amount = float(amount)
