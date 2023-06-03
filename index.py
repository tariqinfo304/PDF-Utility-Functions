import PyPDF2
import subprocess
import os
from pdf2docx import Converter

#Task1 - Merging two PDF files
def merge_pdf(input_files, output_file):
    merger = PyPDF2.PdfMerger()
    
    
    for file in input_files:
        with open(file, 'rb') as f:
            merger.append(f)

    with open(output_file, 'wb') as f:
        merger.write(f)

# Example usage:
input_files1 = ['one.pdf', 'two.pdf']
output_file1 = 'merged.pdf'
merge_pdf(input_files1, output_file1)



#Task2 - Compressing the PDF file

def compress_pdf(input_file, output_file):
    # Extract content from PDF
    reader = PyPDF2.PdfReader(open(input_file, "rb"))
    writer = PyPDF2.PdfWriter()
    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])

    # Save extracted content to a temporary file
    temp_file = "temp.pdf"
    with open(temp_file, "wb") as f:
        writer.write(f)

    # Compress the temporary file using Ghostscript
    subprocess.call(['gswin64', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile=' + output_file, temp_file])

    # Remove the temporary file
    os.remove(temp_file)

# Example usage:
input_file2 = 'one.pdf'
output_file2 = 'compressed.pdf'
compress_pdf(input_file2, output_file2)


# Task3 - Protecting the PDF file

def protect_pdf(input_file, output_file, password):
    reader = PyPDF2.PdfReader(open(input_file, 'rb'))
    writer = PyPDF2.PdfWriter()

    for page_number in range(len(reader.pages)):
        writer.add_page(reader.pages[page_number])

    writer.encrypt(password)

    with open(output_file, 'wb') as f:
        writer.write(f)

# Example usage:
input_file3 = 'one.pdf'
output_file3 = 'protected.pdf'
password = 'tariq786'
protect_pdf(input_file3, output_file3, password)


#Task4 - PDF to Word file

def convert_pdf_to_word(input_file, output_file):
    cv = Converter(input_file)
    cv.convert(output_file, start=0, end=None)
    cv.close()

# Example usage:
input_file4 = 'two.pdf'
output_file4 = 'output.docx'
convert_pdf_to_word(input_file4, output_file4)

