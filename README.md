# Auto BK (book keeper)
#### Video Demo:  <URL (https://youtu.be/Covn5UzqIA8)>
#### Description:
Bank Statement Importer
## Overview
The Auto BookKeeper is a Flask-based web application designed to automate the extraction of transaction data from bank statements. This tool focuses on converting bank statements in PDF format, specifically targeting negative transactions (expenses), and exporting them into a CSV file. The application is built with simplicity, efficiency, and local execution in mind, ensuring user data remains secure by processing files locally without the need for internet access. This Project has a bank statement pdf example inside the uploads folder. You can delete the existing outputs bank statement csv and try it for yourself. Because of the sensitive nature of bank statements I did not include any real bank statements in this project, you may do so locally on your own computer. As mentioned it works specifically with bank statements in a pdf format that has the expenses as a negative numbers. This is great for banks such as Bank Of America which has that format. It is great for book keepers who would like to save roughly 1-2 hours of time doing data entry PER ACCOUNT.
If you have multiple BOA accounts such as 10 per person per month. thats roughly 10-20 hrs of data entry automated per month.

## Features
- PDF Upload: Users can upload their bank statement files in PDF format directly through the user-friendly web interface.
- Automatic Extraction: The application automatically extracts negative transaction values from the uploaded PDF, identifying expenses.
- CSV Generation: Extracted transactions are compiled into a CSV file, making it easy to import into spreadsheet software like Microsoft Excel for further analysis.
- Local Processing: All processing is done locally, ensuring the confidentiality and integrity of financial data.

## Installation
Prerequisites
Python 3.8 or higher
Flask
pdfplumber
pytesseract
Tesseract OCR
Setting Up the Environment
Install Python: Ensure you have Python 3.8 or higher installed on your system. You can download it from the official Python website.

Install Tesseract OCR: Tesseract OCR is necessary for reading image-based PDFs. Download and install Tesseract from its official GitHub repository. Remember to add the Tesseract installation path to your system's PATH environment variable.

Clone the Repository: Clone this repository to your local machine using Git:

bash
Copy code
git clone https://github.com/your-username/bank-statement-importer.git
cd bank-statement-importer
Install Required Python Packages: Run the following command to install the necessary Python libraries:

Copy code
pip install -r requirements.txt
Usage
Start the Application: Navigate to the project directory and start the Flask application using:

arduino
Copy code
py -m flask run
OR
flask run
This command will start the local development server. You should see output indicating that the server is running.

Access the Web Interface: Open a web browser. You should see the Bank Statement Importer's home page.

Upload a Bank Statement: Click on the "Import PDF" button and select a bank statement file (PDF format) from your computer. After the file is uploaded, the "Run Program" button will become active.

Process the File: Click on "Run Program" to start the extraction process. The application will read the bank statement, identify negative transactions, and generate a CSV file.

Download the CSV File: After processing, a download link for the CSV file will be provided. Click the link to download the file containing the extracted transactions.

## Technical Details
Backend Processing
The backend, built with Flask, handles file uploads, processes PDF files, and generates CSV files. It uses pdfplumber to extract text from PDFs and pytesseract for OCR capabilities to read image-based PDFs. The processing logic isolates negative transactions, treating them as expenses, and then compiles them into a CSV format.

Frontend Interface
The frontend is a simple web interface built with HTML, CSS, and JavaScript. It allows users to upload PDF files, initiate processing, and download the resulting CSV file. Bootstrap is used to enhance the UI, making it responsive and user-friendly.

Security and Efficiency
Given the sensitive nature of bank statements, the application is designed to run locally, eliminating the risks associated with online data transmission. Processing efficiency is achieved through streamlined backend logic, ensuring quick turnaround times even for large, multipage PDFs.

## PROJECT OUTLINE:
Project Outline: Bank Statement Importer
Frontend (HTML + Bootstrap + JavaScript)

HTML structure: Basic layout with an import button for PDF files and a button to run the program.
Bootstrap: For styling the import button, run program button, and overall layout.
JavaScript:
Handle the click event on the import button to trigger the file input for PDF selection.
Send the selected PDF to the Flask backend when the "Run Program" button is clicked (potentially using fetch or XMLHttpRequest).
Backend (Flask + Python)

## Flask Setup:
Route for rendering the frontend (index.html).
Route for handling the file upload and processing.
Python Logic:
Extract text from the PDF file (consider using a library like PyPDF2 or pdfplumber).
Parse the extracted text to find and isolate the negative numbers (expenses).
Generate a CSV file containing all the found negative numbers.
Data Flow

User uploads a PDF file through the frontend.
JavaScript sends the file to the Flask backend.
Flask receives the PDF and passes it to the Python processing function.
Python processes the PDF, extracts negative numbers, and generates a CSV file.
Flask sends the CSV file back to the frontend for the user to download.
Security and Performance

Run locally to avoid online security issues.
Keep the processing simple and efficient to handle multipage PDFs quickly.
Development Notes

Keep it simple: The focus is on basic data entry automation, not on creating a complex system.
Local Execution: Ensure the application can run locally on a machine without needing internet access, minimizing security risks.

- Written alongside Chat GPT 4
- Edited and updated by me

## SPECIAL THANKS:
Chat GPT
Harvard CS50
CS50 AI DUCK
David Malan and the courses preceptors