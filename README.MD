# PDF Utility Functions

This repository contains utility functions for working with PDF files in Python. The functions provided allow you to merge multiple PDF files into a single file, compress a PDF file, protect a PDF file with a password, and convert a PDF file to a Word document.

## Installation

To use these utility functions, you need to have the following dependencies installed:

- PyPDF2
  pdf2docx

You can install them using the following command:

```
pip install PyPDF2 pdf2docx

```

In addition, the compress_pdf function relies on Ghostscript, which needs to be installed separately. Please refer to the Ghostscript documentation for installation instructions.

## Usage

The utility functions are defined in the pdf_utils.py file. Here's an overview of each function and its usage:

## Task1 - Merge PDF Files

```
merge_pdf(input_files, output_file)

```

This function takes a list of input PDF files and merges them into a single PDF file specified by the output_file. Example usage:

```
input_files = ['one.pdf', 'two.pdf']
output_file = 'merged.pdf'
merge_pdf(input_files, output_file)

```

## Task2 - Compress PDF File

```
compress_pdf(input_file, output_file)

```

This function compresses a PDF file specified by the input_file and saves the compressed version to the output_file. Example usage:

```
input_file = 'one.pdf'
output_file = 'compressed.pdf'
compress_pdf(input_file, output_file)

```

## Task3 - Protect PDF File

```
protect_pdf(input_file, output_file, password)

```

This function protects a PDF file specified by the input_file with a password and saves the protected version to the output_file. Example usage:

```
input_file = 'one.pdf'
output_file = 'protected.pdf'
password = 'tariq786'
protect_pdf(input_file, output_file, password)

```

## Task4 - Convert PDF to Word File

```
convert_pdf_to_word(input_file, output_file)

```

This function converts a PDF file specified by the input_file to a Word document and saves it to the output_file. Example usage:

```
input_file = 'two.pdf'
output_file = 'output.docx'
convert_pdf_to_word(input_file, output_file)

```

Feel free to modify and integrate these utility functions into your projects as needed. Happy PDF processing!
