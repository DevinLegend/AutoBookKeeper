import os
from flask import Flask, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import pdfplumber
import re
import csv
import pytesseract

# Setting the path for tesseract OCR executable
# Decided to use pytesseract for OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# initializing flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['OUTPUT_FOLDER'] = 'outputs/'

# Function to check if the uploaded file is in PDF format
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads
# Structured Upload logic, with refinements from GPT
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')    # GPT 4 helped with file_path and jsonify
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    return jsonify({'message': 'Invalid file type'}), 400

# Route to process the uploaded file, architected by me, refined by gpt
@app.route('/process', methods=['GET'])
def process_file():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'message': 'No filename provided'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename) #GPT 4 helped here
    if not os.path.exists(file_path):
        return jsonify({'message': 'File not found'}), 404

    negative_amounts = read_bank_statement(file_path)
    output_file_path = generate_csv(negative_amounts, filename)

    return send_from_directory(app.config['OUTPUT_FOLDER'], os.path.basename(output_file_path), as_attachment=True) #GPT with the os.path basename and attachment true

# Function to read the bank statement and extract negative transactions
# Integrated pdfplumber and pytesseract for OCR, GPT provided guidance and optimization
def read_bank_statement(file_path):
    negative_amounts = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text or len(text.strip()) == 0:
                # Convert the PDF page to an image
                image = page.to_image()

                # Use pytesseract to perform OCR on the image
                text = pytesseract.image_to_string(image.original, config='--dpi 300')

            print("Extracted Text:", text)  # Debugging line to inspect the extracted text

            for line in text.split('\n'):
                match = re.search(r'(-\d+\.\d{2})', line) # GPT 4 to help with the code to help determine if something is a negative number
                if match:
                    amount = float(match.group(1))
                    negative_amounts.append(amount)

    return negative_amounts




# Function to generate the CSV file from extracted negative transactions
# CSV logic writing was developed by me, refined w gpt
def generate_csv(negative_amounts, filename):  #os pathing was difficult for me and gpt 4 explained to me how it worked.
    output_file_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{os.path.splitext(filename)[0]}_expenses.csv")
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if negative_amounts: # simple if conditional and for loop checking if the amount is negative to write the csv
            for amount in negative_amounts:
                writer.writerow([amount])
        else:
            writer.writerow(['No expenses found'])

    return output_file_path

# Route to serve the generated CSV file to the user
@app.route('/files/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

# Main execution of the Flask app
if __name__ == '__main__':
    app.run(debug=True)
