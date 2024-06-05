import PyPDF2

class PDFLoader():
    def __init__(self, pdf_path):
        """
        Initialize a PDFLoader object.

        Args:
            pdf_path (str): The path to the PDF file.
        """
        # Assign the given PDF file path to the instance variable 'pdf_path'.
        self.pdf_path = pdf_path

    def convert_pdf_to_txt(self, output_txt_path):
        """
        Converts a PDF file to a text file.

        Args:
            output_txt_path (str): The path to the output text file.
        """
        # Open the PDF file in read-binary mode
        with open(self.pdf_path, 'rb') as pdf_file:
            # Initialize a PDF file reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Use PyPDF2's getPage() method to extract all text from all pages at once
            text = ' '.join(pdf_reader.getPage(page_num).extract_text()
                            for page_num in range(len(pdf_reader.pages)))

        # Write the text to a text file
        with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
            # Write the text to the file
            txt_file.write(text)
            # txt_file.write(text)

