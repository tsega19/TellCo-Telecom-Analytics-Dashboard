import unittest
import pandas as pd
from users_overview import load_data_from_postgres, clean_data, aggregate_user_data, save_aggregated_data

class TestUsersOverview(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'MSISDN/Number': [1, 2, 3, 4, 5],
            'Dur. (ms)': [100, 200, 300, 400, 500],
            'Total DL (Bytes)': [1000, 2000, 3000, 4000, 5000],
            'Total UL (Bytes)': [100, 200, 300, 400, 500]
        }
        self.df = pd.DataFrame(data)

    def test_load_data_from_postgres(self):
        query = "SELECT * FROM xdr_data"
        df = load_data_from_postgres(query)
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_data(self):
        df = clean_data(self.df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_aggregate_user_data(self):
        df = aggregate_user_data(self.df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_save_aggregated_data(self):
        save_aggregated_data(self.df)
        self.assertTrue(os.path.exists('data/aggregated_user_data.csv'))

if __name__ == '__main__':
    unittest.main()