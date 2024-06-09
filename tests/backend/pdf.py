import unittest
from unittest.mock import patch, mock_open

class TestPDFLoader(unittest.TestCase):
    def setUp(self):
        self.pdf_loader = PDFLoader('test.pdf')

    def test_convert_pdf_to_txt(self):
        # Test case: Output file is created and text is written successfully
        with patch('builtins.open', mock_open()) as mock_file:
            self.pdf_loader.convert_pdf_to_txt('output.txt')
            mock_file.assert_called_with('output.txt', 'w', encoding='utf-8')
            handle = mock_file()
            handle.write.assert_called_once_with('test text')

    def test_convert_pdf_to_txt_exception(self):
        # Test case: Exception is raised when opening PDF file
        with patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                self.pdf_loader.convert_pdf_to_txt('output.txt')

    def test_convert_pdf_to_txt_exception_2(self):
        # Test case: Exception is raised when writing to output file
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.side_effect = [mock_open(), mock_open()]
            mock_file.side_effect.return_value.write.side_effect = IOError
            with self.assertRaises(IOError):
                self.pdf_loader.convert_pdf_to_txt('output.txt')