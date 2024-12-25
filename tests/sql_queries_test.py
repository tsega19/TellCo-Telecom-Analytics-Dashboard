import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from scripts.sql_queries import execute_telecom_queries

class TestSQLQueries(unittest.TestCase):

    @patch('scripts.sql_queries.create_engine')
    @patch('scripts.sql_queries.pd.read_sql_query')
    def test_execute_telecom_queries(self, mock_read_sql_query, mock_create_engine):
        # Mock the database engine
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        # Mock the SQL query results
        mock_read_sql_query.side_effect = [
            pd.DataFrame({'unique_imsi_count': [100]}),
            pd.DataFrame({'average_duration': [2000]}),
            pd.DataFrame({
                'IMSI': [1, 2, 3],
                'total_ul_bytes': [1000, 2000, 3000],
                'total_dl_bytes': [4000, 5000, 6000]
            }),
            pd.DataFrame({
                'Last Location Name': ['Location1', 'Location2'],
                'avg_rtt_dl': [50, 60],
                'avg_rtt_ul': [70, 80]
            }),
            pd.DataFrame({
                'Handset Type': ['Handset1', 'Handset2'],
                'count': [10, 20]
            })
        ]

        # Execute the function
        execute_telecom_queries('mock_db_url')

        # Verify the SQL queries were executed
        self.assertEqual(mock_read_sql_query.call_count, 5)

        # Verify the SQL queries
        mock_read_sql_query.assert_any_call("""
            SELECT COUNT(DISTINCT "IMSI") AS unique_imsi_count
            FROM xdr_data;
        """, mock_engine)

        mock_read_sql_query.assert_any_call("""
            SELECT AVG("Dur. (ms)") AS average_duration
            FROM xdr_data
            WHERE "Dur. (ms)" IS NOT NULL;
        """, mock_engine)

        mock_read_sql_query.assert_any_call("""
            SELECT "IMSI", 
                   SUM("Total UL (Bytes)") AS total_ul_bytes, 
                   SUM("Total DL (Bytes)") AS total_dl_bytes
            FROM xdr_data
            GROUP BY "IMSI"
            ORDER BY total_dl_bytes DESC
            LIMIT 10;
        """, mock_engine)

        mock_read_sql_query.assert_any_call("""
            SELECT "Last Location Name", 
                   AVG("Avg RTT DL (ms)") AS avg_rtt_dl, 
                   AVG("Avg RTT UL (ms)") AS avg_rtt_ul
            FROM xdr_data
            GROUP BY "Last Location Name"
            HAVING COUNT(*) > 10
            ORDER BY avg_rtt_dl DESC;
        """, mock_engine)

        mock_read_sql_query.assert_any_call("""
            SELECT "Handset Type", COUNT(*) AS count
            FROM xdr_data
            GROUP BY "Handset Type"
            ORDER BY count DESC
            LIMIT 10;
        """, mock_engine)

if __name__ == '__main__':
    unittest.main()