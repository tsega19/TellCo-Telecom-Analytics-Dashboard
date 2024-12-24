import pandas as pd
from sqlalchemy import create_engine

def execute_telecom_queries(db_url):
    engine = create_engine(db_url)

    # 1. Count of Unique IMSIs
    unique_imsi_count = pd.read_sql_query("""
        SELECT COUNT(DISTINCT "IMSI") AS unique_imsi_count
        FROM xdr_data;
    """, engine)

    # 2. Average Duration of Calls
    average_duration = pd.read_sql_query("""
        SELECT AVG("Dur. (ms)") AS average_duration
        FROM xdr_data
        WHERE "Dur. (ms)" IS NOT NULL;
    """, engine)

    # 3. Total Data Usage per User
    total_data_usage = pd.read_sql_query("""
        SELECT "IMSI", 
               SUM("Total UL (Bytes)") AS total_ul_bytes, 
               SUM("Total DL (Bytes)") AS total_dl_bytes
        FROM xdr_data
        GROUP BY "IMSI"
        ORDER BY total_dl_bytes DESC
        LIMIT 10;
    """, engine)

    # 4. Average RTT by Last Location Name
    avg_rtt_by_location = pd.read_sql_query("""
        SELECT "Last Location Name", 
               AVG("Avg RTT DL (ms)") AS avg_rtt_dl, 
               AVG("Avg RTT UL (ms)") AS avg_rtt_ul
        FROM xdr_data
        GROUP BY "Last Location Name"
        HAVING COUNT(*) > 10
        ORDER BY avg_rtt_dl DESC;
    """, engine)

    # 5. Top 10 Handsets Used by Customers
    top_10_handsets = pd.read_sql_query("""
        SELECT "Handset Type", COUNT(*) AS count
        FROM xdr_data
        GROUP BY "Handset Type"
        ORDER BY count DESC
        LIMIT 10;
    """, engine)

    # 6. Top 3 Handset Manufacturers
    top_3_manufacturers = pd.read_sql_query("""
        SELECT "Handset Manufacturer", COUNT(*) AS count
        FROM xdr_data
        GROUP BY "Handset Manufacturer"
        ORDER BY count DESC
        LIMIT 3;
    """, engine)

    # 7. Top 5 Handsets per Top 3 Handset Manufacturers
    top_5_handsets_per_manufacturer = pd.read_sql_query("""
        SELECT "Handset Manufacturer", "Handset Type", COUNT(*) AS count
        FROM xdr_data
        WHERE "Handset Manufacturer" IN (
            SELECT "Handset Manufacturer"
            FROM xdr_data
            GROUP BY "Handset Manufacturer"
            ORDER BY COUNT(*) DESC
            LIMIT 3
        )
        GROUP BY "Handset Manufacturer", "Handset Type"
        ORDER BY "Handset Manufacturer", count DESC
        LIMIT 5;
    """, engine)

    # 8. User Behavior Overview
    user_behavior = pd.read_sql_query("""
        SELECT "MSISDN/Number",
               COUNT(*) AS xdr_sessions,
               SUM("Dur. (ms)") AS session_duration,
               SUM("Total DL (Bytes)") AS total_dl,
               SUM("Total UL (Bytes)") AS total_ul,
               SUM("Total DL (Bytes)") + SUM("Total UL (Bytes)") AS total_data_volume
        FROM xdr_data
        GROUP BY "MSISDN/Number";
    """, engine)

    # Return results as a dictionary
    return {
        "unique_imsi_count": unique_imsi_count,
        "average_duration": average_duration,
        "total_data_usage": total_data_usage,
        "avg_rtt_by_location": avg_rtt_by_location,
        "top_10_handsets": top_10_handsets,
        "top_3_manufacturers": top_3_manufacturers,
        "top_5_handsets_per_manufacturer": top_5_handsets_per_manufacturer,
        "user_behavior": user_behavior,
    }