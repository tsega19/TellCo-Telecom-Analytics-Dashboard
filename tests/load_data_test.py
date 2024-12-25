import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from scripts.load_data import load_data_from_postgres

class TestLoadData(unittest.TestCase):

    @patch('scripts.load_data.create_engine')
    @patch('scripts.load_data.pd.read_sql_query')
    def test_load_data_from_postgres(self, mock_read_sql_query, mock_create_engine):
        # Mock the database engine
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        # Mock the SQL query result
        mock_read_sql_query.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

        query = "SELECT * FROM xdr_data"
        db_url = "postgresql://username:password@localhost:5432/mydatabase"
        df = load_data_from_postgres(query, db_url)

        # Verify the result
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertEqual(list(df.columns), ['col1', 'col2'])

        # Verify the SQL query was executed
        mock_read_sql_query.assert_called_once_with(query, mock_engine)

if __name__ == '__main__':
    unittest.main()