# Markdown to PDF Converter

This script converts a structured set of Markdown files into PDFs, based on the organization defined in a SUMMARY.md file.

## Prerequisites

- Python 3.6 or later
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/markdown-to-pdf-converter.git
   cd markdown-to-pdf-converter
   ```

2. Install the required packages:
   ```
   pip install markdown2 weasyprint
   ```

   Note: WeasyPrint may require additional system dependencies. Please refer to the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) for your specific operating system.

## Usage

1. Ensure your Markdown files are organized in folders, and you have a SUMMARY.md file in the root directory that outlines the structure and order of your documents.

2. Place the `create_pdfs.py` script in the same directory as your SUMMARY.md file.

3. Run the script:
   ```
   python create_pdfs.py
   ```

4. The script will create an `output_pdfs` directory containing a PDF for each folder specified in SUMMARY.md.

## SUMMARY.md Format

The SUMMARY.md file should be structured as follows:

## Folder1
- File1
- File2

## Folder2
- File3
- File4

  
Each `## ` section represents a folder, and the links underneath represent the files in that folder, in the order they should appear in the PDF.

## Customization

You can customize the PDF styling by modifying the CSS in the `create_pdf` function within the `create_pdfs.py` script.

## License

This project is open source and available under the [MIT License](LICENSE).
