import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pandas as pd
import os


class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Finstance")

        # Set initial window size
        self.root.geometry("400x400")

        # Set custom icon (Make sure you have an "icon.ico" file in the same directory)
        self.root.iconphoto(False, tk.PhotoImage(file="finance_tracker_app.ico"))  # Replace with your icon path

        # Set background color
        self.root.configure(bg="#f0f4f8")

        # Make the grid layout responsive
        self.root.columnconfigure(1, weight=1)
        for i in range(8):
            self.root.rowconfigure(i, weight=1)

        # Initialize data storage
        self.data_file = "finance_data.csv"
        self.data = self.load_data()

        # Create UI components
        self.create_widgets()

    def load_data(self):
        if os.path.exists(self.data_file):
            return pd.read_csv(self.data_file)
        else:
            return pd.DataFrame(columns=["Date", "Description", "Amount"])

    def save_data(self):
        self.data.to_csv(self.data_file, index=False)

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

        # Search Entry and Button
        tk.Label(self.root, text="Search:", bg="#f0f4f8", fg="#333333", font=("Arial", 10)).grid(row=5, column=0,
                                                                                                 sticky="e")
        self.search_entry = tk.Entry(self.root, bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.search_entry.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        search_button = tk.Button(self.root, text="Search", command=self.search_entries, bg="#ff9800", fg="white",
                                  font=("Arial", 10))
        search_button.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Report Button
        report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report, bg="#9c27b0",
                                  fg="white", font=("Arial", 10))
        report_button.grid(row=7, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def add_entry(self):
        date = self.date_entry.get()
        description = self.desc_entry.get()
        amount = self.amount_entry.get()

        # Validate input fields
        if not date or not description or not amount:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        # Validate amount as a float
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Amount must be a number")
            return

        # Create a new DataFrame for the new entry
        new_entry = pd.DataFrame({"Date": [date], "Description": [description], "Amount": [amount]})

        # Concatenate the new entry to the existing data
        self.data = pd.concat([self.data, new_entry], ignore_index=True)

        # Save data after adding
        self.save_data()
        messagebox.showinfo("Success", "Entry added successfully")

        # Clear entries after adding
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def display_entries(self):
        if self.data.empty:
            messagebox.showinfo("No Data", "No entries to display")
            return

        # Display the data in a new window
        display_window = tk.Toplevel(self.root)
        display_window.title("Entries")
        display_window.configure(bg="#f0f4f8")

        display_window.columnconfigure(0, weight=1)
        display_window.rowconfigure(0, weight=1)

        text = tk.Text(display_window, bg="#ffffff", fg="#333333", font=("Arial", 10))
        text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        text.insert(tk.END, self.data.to_string(index=False))

    def search_entries(self):
        search_term = self.search_entry.get()
        if not search_term:
            messagebox.showwarning("Input Error", "Search term cannot be empty")
            return

        filtered_data = self.data[self.data['Description'].str.contains(search_term, case=False)]
        if filtered_data.empty:
            messagebox.showinfo("No Results", "No entries match the search term")
        else:
            self.display_filtered_entries(filtered_data)

    def display_filtered_entries(self, filtered_data):
        display_window = tk.Toplevel(self.root)
        display_window.title("Filtered Entries")
        display_window.configure(bg="#f0f4f8")

        display_window.columnconfigure(0, weight=1)
        display_window.rowconfigure(0, weight=1)

        text = tk.Text(display_window, bg="#ffffff", fg="#333333", font=("Arial", 10))
        text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        text.insert(tk.END, filtered_data.to_string(index=False))

    def generate_report(self):
        # Ensure amounts are treated as floats
        total_income = float(self.data[self.data['Amount'] > 0]['Amount'].sum())
        total_expense = float(self.data[self.data['Amount'] < 0]['Amount'].sum())
        balance = total_income + total_expense

        # Debugging: Print values to console
        print(f"Total Income (raw): {total_income}")
        print(f"Total Expense (raw): {total_expense}")
        print(f"Balance (raw): {balance}")

        # Format the output to two decimal places
        report = (
            f"Total Income: ${total_income:.2f}\n"
            f"Total Expense: ${total_expense:.2f}\n"
            f"Balance: ${balance:.2f}"
        )
        messagebox.showinfo("Report", report)


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
