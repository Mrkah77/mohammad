#ثبت نام کاربر
import re
from fpdf import FPDF

def get_user_input(prompt):
    value = input(prompt).strip()
    return value

def validate_input(value, pattern):
    if not re.match(pattern, value):
        raise ValueError("Invalid input!")
    return True

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Personal Information', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.ln(10)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, content):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)
        self.ln()

def save_to_pdf(filename, data):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_body(data)
    pdf.output(filename)

try:
    # Prompt the user for personal information
    name = get_user_input("Enter your name: ")
    lastname = get_user_input("Enter your lastname: ")
    bus_number = get_user_input("Enter your bus number: ")
    bus_model = get_user_input("Enter your bus model: ")
    working_hours = get_user_input("Enter your working hours: ")
    phone_number = get_user_input("Enter your phone number: ")
    national_code = get_user_input("Enter your national code: ")

    # Validate inputs
    validate_input(name, r'^[A-Za-z ]+$')
    validate_input(lastname, r'^[A-Za-z ]+$')
    validate_input(bus_number, r'^\d+$')
    validate_input(phone_number, r'^\d+$')
    validate_input(national_code, r'^\d+$')

    # Create a unique filename using the person's name
    filename = f"{name}_{lastname}.pdf"

    # Build the content to be saved in the file
    content = f"Name: {name}\nLastname: {lastname}\nBus Number: {bus_number}\nBus Model: {bus_model}" \
              f"\nWorking Hours: {working_hours}\nPhone Number: {phone_number}\nNational Code: {national_code}"

    # Save the data to the PDF file
    save_to_pdf(filename, content)

    print(f"Data saved successfully in {filename}!")
except ValueError as e:
    print("Invalid input! Please try again.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
