import unittest
from unittest.mock import patch, MagicMock

from pinecone import Pinecone

from utility.pinecone import PineconeVector


class TestPineconeVector(unittest.TestCase):
    def setUp(self):
        self.index_name = "test_index"
        self.pcv = PineconeVector(self.index_name)

    @patch.object(Pinecone, "list_indexes")
    def test_index_created_if_not_exists(self, mock_list_indexes):
        mock_list_indexes.return_value = []
        mock_pc = MagicMock()
        mock_pc.create_index.return_value = None
        mock_pc.describe_index.return_value.status = {"ready": True}

        with patch.object(Pinecone, "__init__", return_value=mock_pc):
            index, pc = self.pcv.create_pinecone_index()

        mock_pc.create_index.assert_called_once_with(
            name=self.index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        mock_pc.describe_index.assert_called_with(self.index_name)
        self.assertEqual(index, mock_pc.Index(self.index_name))
        self.assertEqual(pc, mock_pc)

    @patch.object(Pinecone, "list_indexes")
    def test_index_not_created_if_exists(self, mock_list_indexes):
        mock_list_indexes.return_value = [{"name": self.index_name}]
        mock_pc = MagicMock()

        with patch.object(Pinecone, "__init__", return_value=mock_pc):
            index, pc = self.pcv.create_pinecone_index()

        mock_pc.create_index.assert_not_called()
        mock_pc.describe_index.assert_not_called()
        self.assertEqual(index, mock_pc.Index(self.index_name))
        self.assertEqual(pc, mock_pc)


if __name__ == "__main__":
    unittest.main()