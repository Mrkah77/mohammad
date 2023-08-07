import re
from fpdf import FPDF

def get_user_input(prompt):
    user_input = input(prompt)
    return user_input

def validate_input(input_str, pattern):
    if not re.match(pattern, input_str):
        raise ValueError("Invalid input format")

def save_to_pdf(filename, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 10, content)
    pdf.output(filename, 'F')

try:
    # Prompt the user for personal information
    name = get_user_input("Enter your name: ")
    lastname = get_user_input("Enter your lastname: ")
    choice = get_user_input("Was it useful?! (yes/no) ")

    if choice.lower() == "yes":
        print("Thanks for your collaboration")
        validate_input(name, r'^[A-Za-z ]+$')
        validate_input(lastname, r'^[A-Za-z ]+$')
        validate_input(choice, r'^[A-Za-z ]+$')
        filename = f"{name}_{lastname}.pdf"
        content = f"Name: {name}\nLastname: {lastname}\nChoice: {choice}"
        save_to_pdf(filename, content)
        print(f"Data saved successfully in {filename}!")

    else:
        problem = get_user_input("What's your problem? ")
        print("Thanks for your collaboration")
        validate_input(problem, r'^[A-Za-z ]+$')
        filename = f"{name}_{lastname}.pdf"
        content = f"Name: {name}\nLastname: {lastname}\nChoice: {choice}\nproblem: {problem}"
        
        save_to_pdf(filename, content)
        print(f"Data saved successfully in {filename}!")

except ValueError as e:
    print("Invalid input! Please try again.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
