# TellCo Telecom Analytics Dashboard

## Description
This project focuses on analyzing operational data from TellCo Telecom to identify growth opportunities and provide actionable insights. The analysis is structured around four main areas: User Overview, Engagement, Experience Analytics, and Satisfaction. 

### Key Highlights
- **Market Trends**: Samsung, Apple, and Huawei dominate handset usage, with Samsung leading the market. Social Media, YouTube, and Netflix are the most frequently used platforms.
- **Engagement**: High-engagement users contribute 40% of network traffic, driven by streaming services like YouTube and Netflix.
- **Network Performance**: High throughput (25.4 Mbps) and low latency (150 ms) correlate strongly with user satisfaction.
- **Customer Satisfaction**: Satisfaction metrics reveal key areas for improvement, closely tied to engagement and experience.

### Strategic Recommendations
1. **Targeted Marketing**: Launch premium data plans for high-end handset users.
2. **Network Optimization**: Invest in reducing latency in high RTT regions.
3. **Collaborations**: Partner with top app providers (e.g., YouTube, Netflix) for exclusive offers.
4. **Loyalty Programs**: Retain satisfied customers and address pain points for lower-satisfaction segments.

This project provides a comprehensive dashboard for exploring these insights, enabling stakeholders to make data-driven decisions for profitability and growth.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/TellCo-Telecom-Analytics-Dashboard.git
    cd TellCo-Telecom-Analytics-Dashboard
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the dashboard:
    ```sh
    streamlit run dashboard.py
    ```

2. Explore the Jupyter notebooks in the [notebooks](http://_vscodecontentref_/6) directory for detailed analysis:
    - `EDA.ipynb`: Exploratory Data Analysis
    - `expriance_analytics.ipynb`: Experience Analytics
    - `new_engagement.ipynb`: New Engagement Analysis
    - `overview_analysis.ipynb`: Overview Analysis
    - `postgres_load.ipynb`: Loading Data into PostgreSQL
    - `satisfaction_analysis.py.ipynb`: Satisfaction Analysis
    - `users_overview.ipynb`: Users Overview

## Data

- The [data](http://_vscodecontentref_/7) directory contains raw and processed data.
- The [Models](http://_vscodecontentref_/8) directory contains the `user_satisfaction.csv` file used for analysis.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
