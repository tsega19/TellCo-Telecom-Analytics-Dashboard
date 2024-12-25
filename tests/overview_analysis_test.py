import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from scripts.overview_analysis import (
    load_and_prepare_data,
    clean_data,
    identify_top_10_handsets,
    identify_top_3_manufacturers,
    identify_top_5_handsets_per_manufacturer,
    plot_top_10_handsets,
    plot_top_5_handsets_per_manufacturer,
    provide_recommendation
)

class TestOverviewAnalysis(unittest.TestCase):

    @patch('scripts.overview_analysis.load_data_from_postgres')
    @patch('scripts.overview_analysis.clean_data')
    def test_load_and_prepare_data(self, mock_clean_data, mock_load_data_from_postgres):
        # Mock the data loading and cleaning
        mock_load_data_from_postgres.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_clean_data.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

        query = "SELECT * FROM xdr_data"
        df = load_and_prepare_data(query)
        self.assertIsInstance(df, pd.DataFrame)
        mock_load_data_from_postgres.assert_called_once_with(query)
        mock_clean_data.assert_called_once()

    def test_clean_data(self):
        # Sample data for testing
        data = {
            'Dur. (ms)': [100, None, 300],
            'Total DL (Bytes)': [1000, 2000, None],
            'Total UL (Bytes)': [None, 200, 300]
        }
        df = pd.DataFrame(data)
        cleaned_df = clean_data(df)
        self.assertIsInstance(cleaned_df, pd.DataFrame)
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_identify_top_10_handsets(self):
        # Sample data for testing
        data = {'Handset Type': ['Handset1', 'Handset2', 'Handset1', 'Handset3', 'Handset2']}
        df = pd.DataFrame(data)
        top_10_handsets = identify_top_10_handsets(df)
        self.assertIsInstance(top_10_handsets, pd.Series)
        self.assertEqual(len(top_10_handsets), 3)

    def test_identify_top_3_manufacturers(self):
        # Sample data for testing
        data = {'Handset Manufacturer': ['Manufacturer1', 'Manufacturer2', 'Manufacturer1', 'Manufacturer3', 'Manufacturer2']}
        df = pd.DataFrame(data)
        top_3_manufacturers = identify_top_3_manufacturers(df)
        self.assertIsInstance(top_3_manufacturers, pd.Series)
        self.assertEqual(len(top_3_manufacturers), 3)

    def test_identify_top_5_handsets_per_manufacturer(self):
        # Sample data for testing
        data = {
            'Handset Manufacturer': ['Manufacturer1', 'Manufacturer1', 'Manufacturer2', 'Manufacturer2', 'Manufacturer3'],
            'Handset Type': ['Handset1', 'Handset2', 'Handset3', 'Handset4', 'Handset5']
        }
        df = pd.DataFrame(data)
        top_3_manufacturers = identify_top_3_manufacturers(df)
        top_5_handsets_per_manufacturer = identify_top_5_handsets_per_manufacturer(df, top_3_manufacturers)
        self.assertIsInstance(top_5_handsets_per_manufacturer, dict)
        self.assertEqual(len(top_5_handsets_per_manufacturer), 3)

    @patch('scripts.overview_analysis.plt.show')
    def test_plot_top_10_handsets(self, mock_plt_show):
        # Sample data for testing
        top_10_handsets = pd.Series([10, 20, 30], index=['Handset1', 'Handset2', 'Handset3'])
        plot_top_10_handsets(top_10_handsets)
        mock_plt_show.assert_called_once()

    @patch('scripts.overview_analysis.plt.show')
    def test_plot_top_5_handsets_per_manufacturer(self, mock_plt_show):
        # Sample data for testing
        top_5_handsets_per_manufacturer = {
            'Manufacturer1': pd.Series([10, 20], index=['Handset1', 'Handset2']),
            'Manufacturer2': pd.Series([30, 40], index=['Handset3', 'Handset4']),
            'Manufacturer3': pd.Series([50, 60], index=['Handset5', 'Handset6'])
        }
        plot_top_5_handsets_per_manufacturer(top_5_handsets_per_manufacturer)
        self.assertEqual(mock_plt_show.call_count, 3)

    def test_provide_recommendation(self):
        # Sample data for testing
        top_10_handsets = pd.Series([10, 20, 30], index=['Handset1', 'Handset2', 'Handset3'])
        top_3_manufacturers = pd.Series([100, 200, 300], index=['Manufacturer1', 'Manufacturer2', 'Manufacturer3'])
        top_5_handsets_per_manufacturer = {
            'Manufacturer1': pd.Series([10, 20], index=['Handset1', 'Handset2']),
            'Manufacturer2': pd.Series([30, 40], index=['Handset3', 'Handset4']),
            'Manufacturer3': pd.Series([50, 60], index=['Handset5', 'Handset6'])
        }
        provide_recommendation(top_10_handsets, top_3_manufacturers, top_5_handsets_per_manufacturer)

if __name__ == '__main__':
    unittest.main()