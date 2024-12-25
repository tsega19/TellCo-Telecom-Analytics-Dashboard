import unittest
import pandas as pd
from scripts.EDA import load_and_prepare_data, describe_variables, segment_users, basic_metrics

class TestEDA(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'Dur. (ms)': [1000, 2000, 3000, 4000, 5000],
            'Total DL (Bytes)': [100, 200, 300, 400, 500],
            'Total UL (Bytes)': [10, 20, 30, 40, 50]
        }
        self.df = pd.DataFrame(data)

    def test_load_and_prepare_data(self):
        # Assuming load_data_from_postgres and clean_data are mocked
        query = "SELECT * FROM xdr_data"
        df = load_and_prepare_data(query)
        self.assertIsInstance(df, pd.DataFrame)

    def test_describe_variables(self):
        description, data_types = describe_variables(self.df)
        self.assertIsInstance(description, pd.DataFrame)
        self.assertIsInstance(data_types, pd.Series)

    def test_segment_users(self):
        decile_data = segment_users(self.df)
        self.assertIsInstance(decile_data, pd.DataFrame)
        self.assertIn('total_duration', decile_data.columns)
        self.assertIn('total_data', decile_data.columns)

    def test_basic_metrics(self):
        metrics = basic_metrics(self.df)
        self.assertIsInstance(metrics, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()