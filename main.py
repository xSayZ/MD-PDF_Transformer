import markdown
import pdfkit
import codecs
from pdfkit.configuration import Configuration

def convert_md_to_pdf(md_file_path, pdf_file_path):
    # Open the markdown file and read the content
    with codecs.open(md_file_path, mode="r", encoding="utf-8") as md_file:
        text = md_file.read()

    # Convert markdown to html
    html = markdown.markdown(text)

    # Write the HTML to a temporary file
    with codecs.open("temp.html", "w", encoding="utf-8") as temp_file:
        temp_file.write(html)

    # Specify the path to the wkhtmltopdf executable
    config = Configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    # Convert the HTML file to PDF
    pdfkit.from_file("temp.html", pdf_file_path, configuration=config)


if __name__ == "__main__":
    convert_md_to_pdf("example.md", "output.pdf")
