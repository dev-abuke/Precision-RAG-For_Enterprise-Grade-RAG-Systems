import unittest
from unittest.mock import patch
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.text_splitters import RecursiveCharacterTextSplitter
from langchain_community.documents import Document


class TestSplitDocuments(unittest.TestCase):
    @patch('langchain_community.document_loaders.PyPDFLoader')
    @patch('langchain_community.text_splitters.RecursiveCharacterTextSplitter')
    def test_split_documents_success(self, mock_text_splitter, mock_directory_loader):
        # Arrange
        mock_directory_loader.return_value.load.return_value = [Document("Test Document")]
        mock_text_splitter.return_value.split_documents.return_value = [Document("Split Document")]

        # Act
        result = split_documents()

        # Assert
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].page_content, "Split Document")

    @patch('langchain_community.document_loaders.PyPDFLoader')
    @patch('langchain_community.text_splitters.RecursiveCharacterTextSplitter')
    def test_split_documents_exception(self, mock_text_splitter, mock_directory_loader):
        # Arrange
        mock_directory_loader.side_effect = Exception("Test Exception")

        # Act & Assert
        with self.assertRaises(Exception) as context:
            split_documents()

        self.assertEqual(str(context.exception), "Failed to split your data")