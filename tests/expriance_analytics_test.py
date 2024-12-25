import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
from scripts.expriance_analytics import (
    load_and_prepare_data,
    treat_missing_and_outliers,
    aggregate_per_customer
)

class TestExprianceAnalytics(unittest.TestCase):

    @patch('scripts.expriance_analytics.load_data_from_postgres')
    @patch('scripts.expriance_analytics.clean_data')
    def test_load_and_prepare_data(self, mock_clean_data, mock_load_data_from_postgres):
        # Mock the data loading and cleaning
        mock_load_data_from_postgres.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_clean_data.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

        query = "SELECT * FROM xdr_data"
        df = load_and_prepare_data(query)
        self.assertIsInstance(df, pd.DataFrame)
        mock_load_data_from_postgres.assert_called_once_with(query)
        mock_clean_data.assert_called_once()

    def test_treat_missing_and_outliers(self):
        # Sample data for testing
        data = {
            'numeric_col': [1, 2, np.nan, 4, 1000],
            'categorical_col': ['A', 'B', np.nan, 'A', 'B']
        }
        df = pd.DataFrame(data)
        treated_df = treat_missing_and_outliers(df)
        self.assertIsInstance(treated_df, pd.DataFrame)
        self.assertFalse(treated_df.isnull().values.any())
        self.assertTrue((treated_df['numeric_col'] <= treated_df['numeric_col'].mean() + 3 * treated_df['numeric_col'].std()).all())
        self.assertTrue((treated_df['numeric_col'] >= treated_df['numeric_col'].mean() - 3 * treated_df['numeric_col'].std()).all())

    def test_aggregate_per_customer(self):
        # Sample data for testing
        data = {
            'MSISDN/Number': [1, 1, 2, 2],
            'TCP DL Retrans. Vol (Bytes)': [100, 200, 300, 400],
            'Avg RTT DL (ms)': [10, 20, 30, 40],
            'Handset Type': ['Handset1', 'Handset1', 'Handset2', 'Handset2'],
            'Avg Bearer TP DL (kbps)': [1000, 2000, 3000, 4000]
        }
        df = pd.DataFrame(data)
        user_aggregated_data = aggregate_per_customer(df)
        self.assertIsInstance(user_aggregated_data, pd.DataFrame)
        self.assertIn('avg_tcp_retransmission', user_aggregated_data.columns)
        self.assertIn('avg_rtt', user_aggregated_data.columns)
        self.assertIn('handset_type', user_aggregated_data.columns)
        self.assertIn('avg_throughput', user_aggregated_data.columns)

if __name__ == '__main__':
    unittest.main()