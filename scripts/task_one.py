import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def display_data_info(data):
    # Display basic information about the dataset
    """
    Displays basic information about the dataset, including
    the number of rows and columns, the data types of each
    column, and the first few rows of the dataset.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset
    """
    print("Dataset Overview:")
    print(data.info())
    print("\nSample Data:")
    print(data.head())

def identify_top_10_handsets(data):
    # Task 1.0: Identify top 10 handsets and manufacturers
    """
    Identifies the top 10 handsets used by customers based on the provided data.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset

    Returns
    -------
    top_10_handsets : pandas.Series
        The top 10 handsets used by customers, sorted in descending order of their frequency

    """

    top_10_handsets = data['Handset Manufacturer'].value_counts().head(10)
    print("\nTop 10 Handsets Used by Customers:")
    print(top_10_handsets)
    return top_10_handsets

def identify_top_3_manufacturers(data):
    # Top 3 manufacturers based on 'Handset Manufacturer'
    """
    Identifies the top 3 manufacturers of handsets used by customers based on the provided data.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset

    Returns
    -------
    top_3_manufacturers : pandas.Series
        The top 3 manufacturers of handsets used by customers, sorted in descending order of their frequency
    """
    top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    print("\nTop 3 Handset Manufacturers:")
    print(top_3_manufacturers)
    return top_3_manufacturers

def top_5_handsets_per_manufacturer(data, top_3_manufacturers):
    # Initialize an empty dictionary to store the top 5 handsets for each top manufacturer
    """
    Finds the top 5 handsets for each of the top 3 manufacturers of handsets used by customers.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset
    top_3_manufacturers : pandas.Series
        The top 3 manufacturers of handsets used by customers, sorted in descending order of their frequency

    Returns
    -------
    top_5_handsets_per_manufacturer : dict
        A dictionary with the top 5 handsets for each of the top 3 manufacturers, sorted in descending order of their frequency
    """
    top_5_handsets_per_manufacturer = {}

    # Loop through each top manufacturer and find their top 5 handsets
    for manufacturer in top_3_manufacturers.index:
        top_5_handsets = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        top_5_handsets_per_manufacturer[manufacturer] = top_5_handsets

    print("\nTop 5 Handsets per Top 3 Manufacturers:")
    for manufacturer, handsets in top_5_handsets_per_manufacturer.items():
        print(f"\n{manufacturer}:\n{handsets}")

    return top_5_handsets_per_manufacturer

def aggregate_user_behavior(data):
    # Aggregating user behavior data
    """
    Aggregates user behavior data by MSISDN/Number and calculates total data volume.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset

    Returns
    -------
    user_behavior : pandas.DataFrame
        The aggregated user behavior data with total data volume
    """
    user_behavior = data.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum', 
        'Avg Bearer TP DL (kbps)': 'sum',
        'Avg Bearer TP UL (kbps)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum'
    })

    # Calculate total data volume
    user_behavior['Total Data Volume'] = user_behavior['Total DL (Bytes)'] + user_behavior['Total UL (Bytes)']
    return user_behavior

def handle_missing_values(data):
    # Handle missing values
    """
    Handles missing values in the input dataset by filling them with the mean of the respective columns.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset

    Returns
    -------
    data : pandas.DataFrame
        The input dataset with missing values filled
    """
    data.fillna(data.mean(numeric_only=True), inplace=True) 
    return data

def describe_data(data):
    # Variable descriptions and transformations
    """
    Provides descriptive statistics for the input dataset.

    Parameters
    ----------
    data : pandas.DataFrame
        The input dataset for which descriptive statistics are to be calculated

    Returns
    -------
    None
    """

    print("\nDescriptive Statistics:")
    print(data.describe())

def create_deciles(user_behavior):
    """
    Creates a new column 'Decile' in the input DataFrame based on the session duration in milliseconds.

    The deciles are calculated using the pandas.qcut function and are assigned labels from 0 to 9. The deciles are
    calculated based on the 'Dur. (ms)' column of the input DataFrame.

    Parameters
    ----------
    user_behavior : pandas.DataFrame
        The input DataFrame containing the 'Dur. (ms)' column.

    Returns
    -------
    user_behavior : pandas.DataFrame
        The input DataFrame with the additional 'Decile' column.
    """
    user_behavior['Decile'] = pd.qcut(user_behavior['Dur. (ms)'], 10, labels=False)
    return user_behavior

def univariate_analysis(user_behavior):
    # Univariate Analysis (Non-Graphical) - Variance and Standard Deviation for numerical columns
    """
    Provides dispersion parameters (variance and standard deviation) for numerical columns in the input DataFrame.

    Parameters
    ----------
    user_behavior : pandas.DataFrame
        The input DataFrame containing the columns for which dispersion parameters are to be calculated.

    Returns
    -------
    None
    """
    print("\nDispersion Parameters:")
    for col in user_behavior.select_dtypes(include=np.number).columns:
        variance = np.var(user_behavior[col])
        std_deviation = np.std(user_behavior[col])
        print(f"{col}:")
        print(f"  Variance: {variance}")
        print(f"  Standard Deviation: {std_deviation}")

def plot_session_duration_distribution(user_behavior):
    # Visualize the distribution of session duration
    """
    Plots a histogram of the session duration to visualize its distribution.

    This function takes a DataFrame containing session duration data and
    generates a histogram with a kernel density estimate to show the
    distribution of session durations in milliseconds.

    Parameters
    ----------
    user_behavior : pandas.DataFrame
        The input DataFrame containing the 'Dur. (ms)' column representing
        session durations.

    Returns
    -------
    None
    """

    plt.figure(figsize=(10, 6))
    sns.histplot(user_behavior['Dur. (ms)'], bins=20, kde=True)
    plt.title("Distribution of Session Duration")
    plt.xlabel("Session Duration (ms)")
    plt.ylabel("Frequency")
    plt.show()

def bivariate_analysis(user_behavior):
    # Bivariate Analysis
    """
    Performs bivariate analysis on the input DataFrame to explore the relationship between session duration and total data volume.

    Parameters
    ----------
    user_behavior : pandas.DataFrame
        The input DataFrame containing the 'Dur. (ms)' and 'Total Data Volume' columns.

    Returns
    -------
    None
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Total Data Volume', y='Dur. (ms)', data=user_behavior)  # Use 'Dur. (ms)' for session duration
    plt.title("Relationship Between Total Data Volume and Session Duration")
    plt.xlabel("Total Data Volume")
    plt.ylabel("Session Duration (ms)")
    plt.show()

def plot_correlation_matrix(user_behavior):
    # Correlation Matrix
    """
    Plots a heatmap of the correlation matrix for selected features in the user_behavior DataFrame.

    This function calculates the correlation matrix for the columns 'Total DL (Bytes)', 
    'Total UL (Bytes)', and 'Total Data Volume' and visualizes it using a heatmap with annotations.

    Parameters
    ----------
    user_behavior : pandas.DataFrame
        The input DataFrame containing the columns for which the correlation matrix is to be plotted.

    Returns
    -------
    None
    """

    
    correlation_matrix = user_behavior[['Total DL (Bytes)', 'Total UL (Bytes)', 'Total Data Volume']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def perform_pca(user_behavior):
    # Dimensionality Reduction (PCA)
    """
    Applies Principal Component Analysis (PCA) to the user behavior data to reduce dimensionality.

    This function takes the user_behavior DataFrame as input and performs PCA on the columns 'Total DL (Bytes)', 'Total UL (Bytes)', and 'Dur. (ms)'.
    The results are then visualized using a scatter plot of the principal components.

    Parameters
    ----------
    user_behavior : pandas.DataFrame
        The input DataFrame containing the columns to be used for PCA.

    Returns
    -------
    None
    """
    
    features = ['Total DL (Bytes)', 'Total UL (Bytes)', 'Dur. (ms)']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(user_behavior[features])

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_features)

    print("\nPCA Explained Variance Ratio:")
    print(pca.explained_variance_ratio_)

    # Visualize PCA results
    pca_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df)
    plt.title("PCA of User Behavior Data")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()

