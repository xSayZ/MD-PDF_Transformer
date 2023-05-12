# Mark2PDF - Markdown to PDF Converter

Mark2PDF is a simple Python script that converts a Markdown (.md) file to a Portable Document Format (PDF) file. It first converts Markdown to HTML using the `markdown` library and then converts the HTML to PDF using the `pdfkit` and `wkhtmltopdf`.

## Prerequisites

This script requires the following Python libraries:
- `markdown`
- `pdfkit`

Also, it needs `wkhtmltopdf` tool installed in the system. You can download it from [here](https://wkhtmltopdf.org/downloads.html).

Ensure that the `wkhtmltopdf` is correctly installed and added to the system PATH. If there are any issues with the PATH, you can specify the `wkhtmltopdf` path directly in the Python script.

## Usage

```bash
python main.py example.md output.pdf
```

Replace `example.md` and `output.pdf` with the path to your input markdown file and desired output PDF file, respectively.

This script will create a PDF version of the input Markdown file.

# Contribution
Feel free to contribute to this project by submitting issues, improvements, or enhancements via pull requests.

# License
This project is licensed under the terms of the MIT license.
