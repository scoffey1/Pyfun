#This code will run by itself, but its is not hooked up to a database. Also the program is very basic in design.
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime


class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        # Make the grid layout responsive
        self.root.columnconfigure(1, weight=1)
        for i in range(3):  # Configure rows to expand as needed
            self.root.rowconfigure(i, weight=1)

        # Initialize data storage
        self.data = pd.DataFrame(columns=["Date", "Description", "Amount"])

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Entry for Date
        tk.Label(self.root, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="e")
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Entry for Description
        tk.Label(self.root, text="Description:").grid(row=1, column=0, sticky="e")
        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Entry for Amount
        tk.Label(self.root, text="Amount:").grid(row=2, column=0, sticky="e")
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Add Button
        add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        add_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Display Button
        display_button = tk.Button(self.root, text="Display Entries", command=self.display_entries)
        display_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def add_entry(self):
        date = self.date_entry.get()
        description = self.desc_entry.get()
        amount = self.amount_entry.get()

        # Validate input fields
        if not date or not description or not amount:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Date must be in YYYY-MM-DD format")
            return

        # Validate amount as a float
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Amount must be a number")
            return

        # Add entry to the data
        self.data = self.data.append({"Date": date, "Description": description, "Amount": amount}, ignore_index=True)
        messagebox.showinfo("Success", "Entry added successfully")

        # Clear entries after adding
        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def display_entries(self):
        if self.data.empty:
            messagebox.showinfo("No Data", "No entries to display")
            return

        # Display the data in a new window
        display_window = tk.Toplevel(self.root)
        display_window.title("Entries")

        display_window.columnconfigure(0, weight=1)  # Make text widget responsive
        display_window.rowconfigure(0, weight=1)

        text = tk.Text(display_window)
        text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)  # Make text widget fill the window

        text.insert(tk.END, self.data.to_string(index=False))


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
