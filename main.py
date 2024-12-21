import tkinter as tk
from tkinter import ttk
from billing import Billing
from tkinter import messagebox

class Restaurant:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurant Management System")
        self.root.geometry("1200x650")  

        # Add the title at the top
        self.add_title()

    def add_title(self):
        # Create a frame for the title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=10)  # Add vertical padding for spacing

        # Create the title label with styling
        title_label = tk.Label(
            title_frame,
            text="Restaurant Management System",
            font=("Arial", 36, "bold"),  # Large bold font
            bg="lightgrey",
            bd=8,
            relief="groove"
        )
        title_label.pack(side="top", fill="x")

        self.main_frame = tk.Frame(self.root, bg="lightgrey", bd=6, relief="groove")
        self.main_frame.place(x=200, y=150, width=800, height=450)

        self.login_label = tk.Label(
            self.main_frame,
            text="LOGIN",
            bg="lightgrey",
            bd=6, relief="groove",
            anchor="center", 
            font=("sans-serif", 25, "bold")
        )
        self.login_label.pack(side="top", fill="x")

        self.entry_frame = tk.LabelFrame(self.main_frame, text="Enter Details", bd=6, bg="lightgrey",
                                         font=("sans-serif", 25, "bold"))
        self.entry_frame.pack(fill="both", expand=True)

        # Variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Enter username
        self.entryname_label = tk.Label(
            self.entry_frame, text="Enter Your Username:", bg="lightgrey", font=("sans-serif", 15))
        self.entryname_label.grid(row=0, column=0, padx=2, pady=6)

        self.entryname = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.username)
        self.entryname.grid(row=0, column=1, padx=2, pady=6)

        # Enter password
        self.entrypass_label = tk.Label(
            self.entry_frame, text="Enter Your Password:", bg="lightgrey", font=("sans-serif", 15))
        self.entrypass_label.grid(row=1, column=0, padx=1, pady=2)

        self.entrypass = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.password, show="*")
        self.entrypass.grid(row=1, column=1, padx=2, pady=2)

        # Eye button
        self.show_password = False  # State variable for toggle
        self.eye_button = tk.Button(
            self.entry_frame, text="👁", font=("Arial", 10), relief="flat", command=self.toggle_password
        )
        self.eye_button.grid(row=1, column=2, padx=2, pady=2)

        # Buttons
        self.button_frame = tk.Frame(self.entry_frame, bg="lightgrey")
        self.button_frame.place(x=5, y=100, width=770, height=60)

        self.login_btn = tk.Button(
            self.button_frame, text="LOGIN", relief="raised", bd=5, font=("Arial", 13, "bold"), width=15, command=self.check_login #command=self.check_login
        )
        self.login_btn.grid(row=0, column=0, padx=15, pady=2)

        self.billing_btn = tk.Button(
            self.button_frame, text="BILLING", relief="raised", bd=5, font=("Arial", 13, "bold"), width=15, command=self.billing
        )
        self.billing_btn.grid(row=0, column=1, padx=100, pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = tk.Button(
            self.button_frame, text="RESET", relief="raised", bd=5, font=("Arial", 13, "bold"), width=15, command=self.reset
        )
        self.reset_btn.grid(row=0, column=2, padx=15, pady=2)
     
        
    def billing(self):
        self.new_win = tk.Toplevel(self.root)
        self.app = Billing(self.new_win)
   
    
    def toggle_password(self):
        """Toggle the visibility of the password entry."""
        if self.show_password:
            self.entrypass.config(show="*")
            self.eye_button.config(text="👁")
        else:
            self.entrypass.config(show="")
            self.eye_button.config(text="👁‍🗨")
        self.show_password = not self.show_password

    def check_login(self):
        if self.username.get() == "mrx" and self.password.get() == "12345":
            self.billing_btn.config(state="normal")
        else:
            messagebox.showinfo("Error", "Please enter valid credentials.\nusername - mrx\npass-12345")

    def reset(self):
        self.username.set("")
        self.password.set("")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()
