import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from dashboard import (
    user_engagement_analysis,
    experience_analysis,
    satisfaction_analysis
)

class TestDashboard(unittest.TestCase):

    @patch('scripts.dashboard.st.pyplot')
    @patch('scripts.dashboard.st.dataframe')
    @patch('scripts.dashboard.aggregate_metrics')
    @patch('scripts.dashboard.normalize_and_cluster')
    def test_user_engagement_analysis(self, mock_normalize_and_cluster, mock_aggregate_metrics, mock_st_dataframe, mock_st_pyplot):
        # Mock the data
        mock_aggregate_metrics.return_value = pd.DataFrame({'sessions_frequency': [1, 2], 'total_data_volume': [3, 4]})
        mock_normalize_and_cluster.return_value = (pd.DataFrame({'sessions_frequency': [1, 2], 'total_data_volume': [3, 4], 'cluster': [0, 1]}), MagicMock())

        user_engagement_analysis()

        mock_aggregate_metrics.assert_called_once()
        mock_normalize_and_cluster.assert_called_once()
        mock_st_dataframe.assert_called_once()
        mock_st_pyplot.assert_called_once()

    @patch('scripts.dashboard.st.pyplot')
    @patch('scripts.dashboard.st.dataframe')
    @patch('scripts.dashboard.aggregate_per_customer')
    @patch('scripts.dashboard.kmeans_clustering')
    def test_experience_analysis(self, mock_kmeans_clustering, mock_aggregate_per_customer, mock_st_dataframe, mock_st_pyplot):
        # Mock the data
        mock_aggregate_per_customer.return_value = pd.DataFrame({'avg_rtt': [10, 20], 'avg_throughput': [30, 40]})
        mock_kmeans_clustering.return_value = (pd.DataFrame({'avg_rtt': [10, 20], 'avg_throughput': [30, 40], 'cluster': [0, 1]}), MagicMock())

        experience_analysis()

        mock_aggregate_per_customer.assert_called_once()
        mock_kmeans_clustering.assert_called_once()
        mock_st_dataframe.assert_called_once()
        mock_st_pyplot.assert_called_once()

    @patch('scripts.dashboard.st.pyplot')
    @patch('scripts.dashboard.st.dataframe')
    @patch('scripts.dashboard.aggregate_metrics')
    @patch('scripts.dashboard.aggregate_per_customer')
    def test_satisfaction_analysis(self, mock_aggregate_per_customer, mock_aggregate_metrics, mock_st_dataframe, mock_st_pyplot):
        # Mock the data
        mock_aggregate_metrics.return_value = pd.DataFrame({'MSISDN/Number': [1, 2], 'sessions_frequency': [3, 4]})
        mock_aggregate_per_customer.return_value = pd.DataFrame({'MSISDN/Number': [1, 2], 'avg_rtt': [5, 6]})

        satisfaction_analysis()

        mock_aggregate_metrics.assert_called_once()
        mock_aggregate_per_customer.assert_called_once()
        mock_st_dataframe.assert_called()
        mock_st_pyplot.assert_called()

if __name__ == '__main__':
    unittest.main()