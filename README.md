
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
    python dashboard.py
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

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Thanks to the contributors and the open-source community.