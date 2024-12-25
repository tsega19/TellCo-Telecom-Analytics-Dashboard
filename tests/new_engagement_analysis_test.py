import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from scripts.new_engagement_analysis import (
    load_and_prepare_data,
    aggregate_metrics,
    top_10_customers,
    normalize_and_cluster
)

class TestNewEngagementAnalysis(unittest.TestCase):

    @patch('scripts.new_engagement_analysis.load_data_from_postgres')
    @patch('scripts.new_engagement_analysis.clean_data')
    def test_load_and_prepare_data(self, mock_clean_data, mock_load_data_from_postgres):
        # Mock the data loading and cleaning
        mock_load_data_from_postgres.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_clean_data.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

        query = "SELECT * FROM xdr_data"
        df = load_and_prepare_data(query)
        self.assertIsInstance(df, pd.DataFrame)
        mock_load_data_from_postgres.assert_called_once_with(query)
        mock_clean_data.assert_called_once()

    def test_aggregate_metrics(self):
        # Sample data for testing
        data = {
            'MSISDN/Number': [1, 1, 2, 2],
            'Bearer Id': [1, 2, 3, 4],
            'Dur. (ms)': [100, 200, 300, 400],
            'Total DL (Bytes)': [1000, 2000, 3000, 4000],
            'Total UL (Bytes)': [100, 200, 300, 400]
        }
        df = pd.DataFrame(data)
        user_aggregated_data = aggregate_metrics(df)
        self.assertIsInstance(user_aggregated_data, pd.DataFrame)
        self.assertIn('total_data_volume', user_aggregated_data.columns)

    def test_top_10_customers(self):
        # Sample data for testing
        data = {
            'MSISDN/Number': range(1, 21),
            'sessions_frequency': range(1, 21),
            'total_session_duration': range(1, 21),
            'total_data_volume': range(1, 21)
        }
        user_aggregated_data = pd.DataFrame(data)
        top_10_sessions, top_10_duration, top_10_data_volume = top_10_customers(user_aggregated_data)
        self.assertEqual(len(top_10_sessions), 10)
        self.assertEqual(len(top_10_duration), 10)
        self.assertEqual(len(top_10_data_volume), 10)

    @patch('scripts.new_engagement_analysis.StandardScaler')
    @patch('scripts.new_engagement_analysis.KMeans')
    def test_normalize_and_cluster(self, mock_kmeans, mock_standard_scaler):
        # Sample data for testing
        data = {
            'sessions_frequency': [1, 2, 3, 4, 5],
            'total_session_duration': [100, 200, 300, 400, 500],
            'total_download_data': [1000, 2000, 3000, 4000, 5000],
            'total_upload_data': [100, 200, 300, 400, 500],
            'total_data_volume': [1100, 2200, 3300, 4400, 5500]
        }
        user_aggregated_data = pd.DataFrame(data)

        # Mock the scaler and kmeans
        mock_scaler_instance = MagicMock()
        mock_standard_scaler.return_value = mock_scaler_instance
        mock_scaler_instance.fit_transform.return_value = user_aggregated_data

        mock_kmeans_instance = MagicMock()
        mock_kmeans.return_value = mock_kmeans_instance
        mock_kmeans_instance.fit_predict.return_value = [0, 1, 2, 0, 1]

        clustered_data = normalize_and_cluster(user_aggregated_data)
        self.assertIsInstance(clustered_data, pd.DataFrame)
        self.assertIn('cluster', clustered_data.columns)

if __name__ == '__main__':
    unittest.main()