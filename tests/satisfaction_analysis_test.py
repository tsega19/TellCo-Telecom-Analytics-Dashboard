import unittest
import pandas as pd
from satisfaction_analysis import (
    load_and_prepare_data,
    treat_missing_and_outliers,
    aggregate_per_customer,
    calculate_engagement_score,
    calculate_experience_score,
    calculate_satisfaction_score,
    build_regression_model,
    run_kmeans,
    aggregate_scores_per_cluster,
    save_to_csv
)

class TestSatisfactionAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'MSISDN/Number': [1, 2, 3, 4, 5],
            'sessions_frequency': [1, 2, 3, 4, 5],
            'total_session_duration': [100, 200, 300, 400, 500],
            'total_download_data': [1000, 2000, 3000, 4000, 5000],
            'total_upload_data': [100, 200, 300, 400, 500],
            'avg_tcp_retransmission': [10, 20, 30, 40, 50],
            'avg_rtt': [1, 2, 3, 4, 5],
            'avg_throughput': [10, 20, 30, 40, 50]
        }
        self.df = pd.DataFrame(data)

    def test_load_and_prepare_data(self):
        query = "SELECT * FROM xdr_data"
        df = load_and_prepare_data(query)
        self.assertIsInstance(df, pd.DataFrame)

    def test_treat_missing_and_outliers(self):
        df = treat_missing_and_outliers(self.df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_aggregate_per_customer(self):
        df = aggregate_per_customer(self.df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_calculate_engagement_score(self):
        kmeans = KMeans(n_clusters=3, random_state=42)
        df = calculate_engagement_score(self.df, kmeans)
        self.assertIsInstance(df, pd.DataFrame)

    def test_calculate_experience_score(self):
        kmeans = KMeans(n_clusters=3, random_state=42)
        df = calculate_experience_score(self.df, kmeans)
        self.assertIsInstance(df, pd.DataFrame)

    def test_calculate_satisfaction_score(self):
        df = calculate_satisfaction_score(self.df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_build_regression_model(self):
        model = build_regression_model(self.df)
        self.assertIsNotNone(model)

    def test_run_kmeans(self):
        df, kmeans = run_kmeans(self.df)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsNotNone(kmeans)

    def test_aggregate_scores_per_cluster(self):
        df = aggregate_scores_per_cluster(self.df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_save_to_csv(self):
        save_to_csv(self.df)
        self.assertTrue(os.path.exists('data/aggregated_data.csv'))

if __name__ == '__main__':
    unittest.main()