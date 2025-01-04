from fpdf import FPDF
import os

# Function to read data from a file
def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

# Function to generate PDF report
def generate_pdf_report(data, output_path):
    # Create instance of FPDF class
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title and fonts
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Automated Report", ln=True, align="C")

    # Set font for body text
    pdf.set_font('Arial', '', 12)

    # Add data to PDF
    for line in data:
        pdf.multi_cell(0, 10, line)

    # Save the generated PDF
    pdf.output(output_path)
    print(f"PDF report generated and saved as {output_path}")

# Sample usage
def main():
    # Define the input data file and output PDF file
    input_file = 'data.txt'  # Change to your data file path
    output_pdf = 'report.pdf'

    # Read data from file
    data = read_data(input_file)

    if data:
        # Generate the PDF report
        generate_pdf_report(data, output_pdf)
    else:
        print("No data to generate report.")

# Run the script
if __name__ == "__main__":
    main()
