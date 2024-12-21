from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for header
        self.set_font('Arial', 'B', 15)
        # Add the date and restaurant name in the same line
        self.cell(5, 10, '2024-12-20', align='L')  # Left-aligned Date
        self.cell(180, 10, 'X Restaurant Ltd', align='C')  # Centered Restaurant Name
        self.ln(10)  # Line break

        # Add the address and contact information
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Victoria, Clyde North, Azzam street', align='C')  # Address
        self.ln(5)  # Line break
        self.cell(0, 10, 'Contact no. - 1122334455', align='C')  # Contact Info
        self.ln(15)  # Two line breaks for spacing

    def add_customer_info(self, bill_number, customer_name, customer_contact):
        # Set font for customer info
        self.set_font('Arial', '', 11)
        self.cell(50, 10, f'Bill number: {bill_number}', align='L')
        self.ln(6)
        self.cell(50, 10, f'Customer Name: {customer_name}', align='L')
        self.ln(6)
        self.cell(50, 10, f'Customer Contact: {customer_contact}', align='L')
        self.ln(20)  # Line break after customer info

        # Add table headers: Name, Quantity, Cost, Price
        self.set_font('Arial', 'B', 10)
        self.cell(90, 10, 'Name', border=1, align='L')  # More space for Name
        self.cell(30, 10, 'Quantity', border=1, align='C')
        self.cell(30, 10, 'Cost', border=1, align='C')
        self.cell(30, 10, 'Price', border=1, align='C')
        self.ln(10)  # Line break for table
        
        
    def add_product_table(self, products):
        self.set_font('Arial', '', 10)
        for product in products:
            self.cell(90, 10, product['name'], border=1, align='L')
            self.cell(30, 10, str(product['quantity']), border=1, align='C')
            self.cell(30, 10, str(product['cost']), border=1, align='C')
            self.cell(30, 10, str(product['price']), border=1, align='C')
            self.ln(10)  # Line break after each product

    def add_grand_total(self, grand_total):
        # Add grand total at the bottom of the bill
        self.set_font('Arial', 'B', 12)
        self.cell(182, 10, f'GRAND TOTAL: {grand_total}', align='R')  # Right aligned total
        self.ln(10)  # Line break for spacing

