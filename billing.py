import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from pdf import PDF
from check import check_name


class Billing:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1200x650")  
        
        self.prices = []
        
        self.bills = []
        
        self.products = []
        
        self.add_title()
        
    def add_title(self):
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
        self.main_frame.place(x=40, y=110, width=450, height=500)
        
        self.entry_frame = tk.LabelFrame(self.main_frame, text="Enter Item Details", bd=6, bg="lightgrey",
                                         font=("sans-serif", 25, "bold"))
        self.entry_frame.pack(fill="both", expand=True)
        
        self.variable()        
        
        
        #Enteries
        
        #bill number
        self.bill_label = tk.Label(
            self.entry_frame, text="Bill Number:", bg="lightgrey", font=("sans-serif", 15))
        self.bill_label.grid(row=0, column=0, padx=2, pady=2)

        self.bill = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.bill_var)
        self.bill.grid(row=0, column=1, padx=2, pady=2)
        self.bill.config(state="disabled")
        
        #customer name
        self.customername_label = tk.Label(
            self.entry_frame, text="Customer name:", bg="lightgrey", font=("sans-serif", 15))
        self.customername_label.grid(row=1, column=0, padx=2, pady=2)

        self.customername = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.customername_var)
        self.customername.grid(row=1, column=1, padx=2, pady=2)
        
        
        #customer contact
        self.customercontact_label = tk.Label(
            self.entry_frame, text="Customer Contact:", bg="lightgrey", font=("sans-serif", 15))
        self.customercontact_label.grid(row=3, column=0, padx=2, pady=2)

        self.customercontact = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.customercontact_var)
        self.customercontact.grid(row=3, column=1, padx=2, pady=2)
        
        
        #Date
        self.date_label = tk.Label(
            self.entry_frame, text="Date:", bg="lightgrey", font=("sans-serif", 15))
        self.date_label.grid(row=4, column=0, padx=2, pady=2)

        self.date = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.date_var)
        self.date.grid(row=4, column=1, padx=2, pady=2)
        self.date.config(state="disabled")
        
        current_datetime = str(datetime.now())
        current_date = current_datetime[0:10]
        self.date_var.set(current_date)
        
        
        #item purchased
        self.itempurchase_label = tk.Label(
            self.entry_frame, text="Item Purchased:", bg="lightgrey", font=("sans-serif", 15))
        self.itempurchase_label.grid(row=5, column=0, padx=2, pady=2)

        self.itempurchase = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.itempurchase_var)
        self.itempurchase.grid(row=5, column=1, padx=2, pady=2)
        
        
        #item quantity
        self.itemquantity_label = tk.Label(
            self.entry_frame, text="Item Quantity:", bg="lightgrey", font=("sans-serif", 15))
        self.itemquantity_label.grid(row=6, column=0, padx=2, pady=2)

        self.itemquantity = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.itemquantity_var)
        self.itemquantity.grid(row=6, column=1, padx=2, pady=2)
        
        
        #cost
        self.cost_label = tk.Label(
            self.entry_frame, text="Cost of One:", bg="lightgrey", font=("sans-serif", 15))
        self.cost_label.grid(row=7, column=0, padx=2, pady=2)

        self.cost = tk.Entry(self.entry_frame, font=("sans-serif", 15), bd=6, textvariable=self.cost_var)
        self.cost.grid(row=7, column=1, padx=2, pady=2)

        
        
        #buttons
        self.button_frame = tk.Frame(self.main_frame, bg="lightgrey")
        self.button_frame.place(x=7,y=340,width=420,height=140)
        
        #add
        self.adding_btn = tk.Button(
            self.button_frame, text="ADD", relief="raised", bd=5, font=("Arial", 13, "bold"), width=11, command=self.add_bill
        )
        self.adding_btn.grid(row=0, column=0, padx=6, pady=10)
        self.adding_btn.config(state="disabled")
        
        
        #generate
        self.generate_btn = tk.Button(
            self.button_frame, text="GENERATE", relief="raised", bd=5, font=("Arial", 13, "bold"), width=11, command=self.generate_bill
        )
        self.generate_btn.grid(row=0, column=2, padx=2, pady=2)
        
        #clear
        self.clear_btn = tk.Button(
            self.button_frame, text="CLEAR", relief="raised", bd=5, font=("Arial", 13, "bold"), width=11,command=self.clear
        )
        self.clear_btn.grid(row=1, column=3, padx=6, pady=2)
        
        #total
        self.undo_btn = tk.Button(
            self.button_frame, text="UNDO", relief="raised", bd=5, font=("Arial", 13, "bold"), width=11, command=self.undo
        )
        self.undo_btn.grid(row=1, column=0, padx=2, pady=2)
        
        #reset
        self.reset_btn = tk.Button(
            self.button_frame, text="RESET", relief="raised", bd=5, font=("Arial", 13, "bold"), width=11, command=self.reset
        )
        self.reset_btn.grid(row=1, column=2, padx=2, pady=2)
        
        #save
        self.save_btn = tk.Button(
            self.button_frame, text="SAVE", relief="raised", bd=5, font=("Arial", 13, "bold"), width=11, command=self.save_bill_as_pdf
        )
        self.save_btn.grid(row=0, column=3, padx=6, pady=2)
        
        
        
        #Calculator
        self.calc_frame = tk.Frame(self.root, bd=6, bg="lightgrey", relief="groove")
        self.calc_frame.place(x=550, y=110, width=610, height=280)
        
        self.calc_entry = tk.Entry(self.calc_frame, font=("Arial",18),bd=6, relief="groove", width=44, justify="right")
        self.calc_entry.grid(row=0,column=0, padx=0, pady=2, columnspan=50)
        
         #for key presses
        self.calc_entry.bind("<Key>", self.key_pressed)
        
        #buttons
        self.cross_btn = tk.Button(self.calc_frame, text="❌", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=self.last_entry)
        self.cross_btn.grid(row=1, column=0, padx=0, pady=2)
        
        self.c_btn = tk.Button(self.calc_frame, text="C", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=self.reset_calc)
        self.c_btn.grid(row=2, column=0, padx=0, pady=2)
        
        self.key_btn = tk.Button(self.calc_frame, text="KEY", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=self.focus)
        self.key_btn.grid(row=3, column=0, padx=0, pady=2)
        
        self.dot_btn = tk.Button(self.calc_frame, text=".", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked("."))
        self.dot_btn.grid(row=4, column=0, padx=0, pady=2)
        
        self.seven_btn = tk.Button(self.calc_frame, text="7", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(7))
        self.seven_btn.grid(row=1, column=1, padx=0, pady=2)

        
        self.eight_btn = tk.Button(self.calc_frame, text="8", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(8))
        self.eight_btn.grid(row=1, column=2, padx=0, pady=2)
        
        self.nine_btn = tk.Button(self.calc_frame, text="9", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(9))
        self.nine_btn.grid(row=1, column=4, padx=0, pady=2)
        
        self.four_btn = tk.Button(self.calc_frame, text="4", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(4))
        self.four_btn.grid(row=2, column=1, padx=0, pady=2)
        
        self.five_btn = tk.Button(self.calc_frame, text="5", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(5))
        self.five_btn.grid(row=2, column=2, padx=0, pady=2)
        
        self.six_btn = tk.Button(self.calc_frame, text="6", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(6))
        self.six_btn.grid(row=2, column=4, padx=0, pady=2)
        
        self.one_btn = tk.Button(self.calc_frame, text="1", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(1))
        self.one_btn.grid(row=3, column=1, padx=0, pady=2)
        
        self.second_btn = tk.Button(self.calc_frame, text="2", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(2))
        self.second_btn.grid(row=3, column=2, padx=0, pady=2)
        
        self.three_btn = tk.Button(self.calc_frame, text="3", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(3))
        self.three_btn.grid(row=3, column=4, padx=0, pady=2)
        
        self.zero_btn = tk.Button(self.calc_frame, text="0", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_clicked(0))
        self.zero_btn.grid(row=4, column=2, padx=0, pady=2)
        
        
        
        self.percent_btn = tk.Button(self.calc_frame, text="%", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_operator("%"))
        self.percent_btn.grid(row=4, column=1, padx=0, pady=2)
        
        self.divide_btn = tk.Button(self.calc_frame, text="/", bd=6, relief="groove", width=15, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_operator("/"))
        self.divide_btn.grid(row=4, column=4, padx=0, pady=2)
        
        self.multiply_btn_btn = tk.Button(self.calc_frame, text="*", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_operator("*"))
        self.multiply_btn_btn.grid(row=1, column=5, padx=0, pady=2)
        
        self.sub_btn = tk.Button(self.calc_frame, text="-", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_operator("-"))
        self.sub_btn.grid(row=2, column=5, padx=0, pady=2)
        
        self.add_btn = tk.Button(self.calc_frame, text="+", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=lambda: self.button_operator("+"))
        self.add_btn.grid(row=3, column=5, padx=0, pady=2)
        
        self.equal_btn = tk.Button(self.calc_frame, text="=", bd=6, relief="groove", width=9, height=2,font=("sans-serif",10, "bold"), command=self.calculate)
        self.equal_btn.grid(row=4, column=5, padx=0, pady=2)
        
        
        # Bill Area
        self.bill_frame = tk.LabelFrame(self.root, text="Bill Area", bd=6, bg="lightgrey", relief="groove", font=("Arial", 15, "bold"))
        self.bill_frame.place(x=550, y=410, width=610, height=197)

        # Add scrollbar
        self.scrollbar = tk.Scrollbar(self.bill_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Text widget
        self.bill_text = tk.Text(self.bill_frame, yscrollcommand=self.scrollbar.set)
        self.bill_text.pack(fill="both", expand=True)
        self.default_text()


        # Link scrollbar and text widget
        self.scrollbar.config(command=self.bill_text.yview)   
    
    def variable(self):
        #Variables
        self.bill_var = tk.StringVar()
        self.customername_var = tk.StringVar()
        self.customercontact_var  = tk.StringVar()
        self.date_var  = tk.StringVar()
        self.itempurchase_var = tk.StringVar()
        self.itemquantity_var = tk.StringVar()
        self.cost_var = tk.StringVar()
    
    
    def default_text(self):
        date = self.date_var.get()
        
        self.bill_text.insert(tk.END, f"Date: {date}\t\t\t  X Restaurant Ltd.")
        self.bill_text.insert(tk.END, "\n\t\t  Victoria, Clyde North, Azzam street")
        self.bill_text.insert(tk.END, "\n\t\t      Contact no. - 1122334455")
     
    def generate_bill(self):
        
        self.bill_check()
        
        bill_num = self.bill_var.get()
        self.bill_text.insert(tk.END, f"\n\nBill number: {bill_num}")
        
        customer_name = self.customername_var.get()
        self.bill_text.insert(tk.END, f"\nCustomer Name: {customer_name}")
        
        customer_contact = self.customercontact_var.get()
        self.bill_text.insert(tk.END, f"\nCustomer Contact: {customer_contact}")
        
        self.bill_text.insert(tk.END, "\n\nName\t\t\tQuantity\t\t   Cost\t\t   Price")
           
        self.bill_text.insert(tk.END, "\n------------------------------------------------------------------------")
        
        self.generate_btn.config(state="disabled")
        self.adding_btn.config(state="normal")
        
    def add_bill(self):
        item_purchase = self.itempurchase_var.get()
        item_quantity = self.itemquantity_var.get()
        item_cost = self.cost_var.get()
        
        # Ensure valid input
        if item_purchase != "" and item_quantity.isdigit() and item_cost.isdigit():
            item_price = int(item_quantity) * int(item_cost)
            self.prices.append(item_price)
            
            #append product details
            self.products.append({
                "name": item_purchase,
                "quantity": int(item_quantity),
                "cost": int(item_cost),
                "price": item_price
                
            })

            # Insert the product details into the bill
            self.bill_text.insert(tk.END, f"\n{item_purchase}\t\t\t{item_quantity}\t\t   {item_cost}\t\t   {item_price}")
            self.bill_text.insert(tk.END, "\n------------------------------------------------------------------------")
            
            # Remove the previous "GRAND TOTAL" if it exists
            content = self.bill_text.get(1.0, tk.END).splitlines()
            for i, line in enumerate(content):
                if "GRAND TOTAL" in line:
                    self.bill_text.delete(f"{i + 1}.0", f"{i + 2}.0")
                    break

            # Calculate and insert the new grand total
            self.grand_total = sum(self.prices)
            self.bill_text.insert(tk.END, f"\n\t\t\tGRAND TOTAL: {self.grand_total}")
            
            #clear item related entries
            self.itempurchase_var.set("")
            self.itemquantity_var.set("")
            self.cost_var.set("")
                
                            
        else:
            # Handle invalid input
            print("Please provide valid input for all fields.")

    
    def bill_check(self):
        
        for bill in range(1, 1000000000000000):
            bill = str(bill)
            check_bill = check_name(f"Bill_{bill}.pdf")
            
            if check_bill == "no":
                self.bills.append(bill)
                break
            
        current_bill = self.bills[0]
        self.bill_var.set(current_bill)
        

    def save_bill_as_pdf(self):
         # Initialize the PDF object
        
        check_bill = check_name(f"Bill_1.pdf")
        if check_bill == "no":
            self.bills.pop(0)
        
        #main info
        pdf = PDF()
        pdf.add_page()
        
        #customer info
        bill_number = self.bill_var.get()
        customer_name = self.customername_var.get()
        customer_contact = self.customercontact_var.get()
        pdf.add_customer_info(bill_number, customer_name, customer_contact)
        
        #products info and total
        pdf.add_product_table(self.products)
        pdf.add_grand_total(self.grand_total)
        
        filename = f"Bill_{self.bill_var.get()}.pdf"
        pdf.output(filename)
        
        self.reset()
        messagebox.showinfo("SUCCESS", "YOUR BILL HAS BEEN SAVED SUCCESSFULLY")
                      
    def clear(self):
        self.bill_var.set("")
        self.customername_var.set("")
        self.customercontact_var.set("")
        self.itempurchase_var.set("")
        self.itemquantity_var.set("")
        self.cost_var.set("")            
    
    
    def undo(self):
        if self.prices and len(self.prices) == 1:
            self.prices.pop()
            content = self.bill_text.get(1.0, tk.END).split("\n")
            self.bill_text.delete(1.0, tk.END)
            
            # Reinsert lines except the last ones being removed
            for i, line in enumerate(content[:-4]):
                if i < len(content[:-4]) - 1:
                    self.bill_text.insert(tk.END, line + "\n")
                else:
                    self.bill_text.insert(tk.END, line)


        elif self.prices and len(self.prices) > 1:
            self.prices.pop()
            content = self.bill_text.get(1.0, tk.END).split("\n")
            self.bill_text.delete(1.0, tk.END)
            
            for line in content[:-4]:
                    self.bill_text.insert(tk.END, line + "\n")
                    
            total = sum(self.prices)
            self.bill_text.insert(tk.END, f"\t\t\tGRAND TOTAL: {total}")
            

    def reset(self):
        self.reset_calc()
        self.clear()
        self.bill_text.delete(1.0, tk.END)     
        self.default_text()  
        self.generate_btn.config(state="normal")
        self.adding_btn.config(state="disabled")
           
    def key_pressed(self, event):
         # Check for special keys
            if event.keysym == "Return":  # Enter key
                self.calculate()
        
                
            elif event.char.lower() == "c" or event.keysym == "Escape":  # C key or Escape
                self.reset()

        
    def focus(self):
        self.calc_entry.focus()
    
    def calculate(self):
        try:
            result = eval(self.calc_entry.get())
            self.calc_entry.delete(0, tk.END)
            self.calc_entry.insert(tk.END, str(result))
        except:
            self.calc_entry.delete(0, tk.END)
            self.calc_entry.insert(tk.END, "Error")
            self.root.after(1000, self.reset)
    
    
    def button_clicked(self, value):
        
        current = self.calc_entry.get()#get current value in the entry
         # Check if the last character is the same as the current one

        self.calc_entry.delete(0, tk.END)#delete existing number
        self.calc_entry.insert(tk.END, current+str(value))#add new number and show all together
   
    
    def button_operator(self, operator):
        current = self.calc_entry.get()  # Get the current value
        
        # Only add the operator if the last character is not already the same operator
        if current and current[-1] in ["+", "-"]:
            return  # Skip appending the operator if the last character is already an operator

        # Add operator if the entry is not empty and does not already end with an operator
        if current and current[-1].isdigit():
            self.calc_entry.insert(tk.END, " " + operator + " ")  # Append the operator with space
        elif not current:  # If entry is empty, don't append operator
            return  # Prevent operator input without an initial number

    def last_entry(self):
        current = self.calc_entry.get()
        self.calc_entry.delete(len(current)-1, tk.END)
    
   
    def reset_calc(self):
        self.calc_entry.delete(0, tk.END)