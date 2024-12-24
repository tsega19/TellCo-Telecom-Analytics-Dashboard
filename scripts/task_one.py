import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def display_data_info(data):
    print("Dataset Overview:")
    print(data.info())
    print("\nSample Data:")
    print(data.head())

def identify_top_10_handsets(data):
    top_10_handsets = data['Handset Type'].value_counts().head(10)
    print("\nTop 10 Handsets Used by Customers:")
    print(top_10_handsets)
    return top_10_handsets

def identify_top_3_manufacturers(data):
    top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    print("\nTop 3 Handset Manufacturers:")
    print(top_3_manufacturers)
    return top_3_manufacturers

# def top_5_handsets_per_manufacturer(data, top_3_manufacturers):
#     top_5_handsets_per_manufacturer = {}
#     for manufacturer in top_3_manufacturers.index:
#         top_5_handsets = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
#         top_5_handsets_per_manufacturer[manufacturer] = top_5_handsets

#     print("\nTop 5 Handsets per Top 3 Manufacturers:")
#     for manufacturer, handsets in top_5_handsets_per_manufacturer.items():
#         print(f"\n{manufacturer}:\n{handsets}")

#     return top_5_handsets_per_manufacturer

def aggregate_user_behavior(data):
    user_behavior = data.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum', 
        'Avg Bearer TP DL (kbps)': 'sum',
        'Avg Bearer TP UL (kbps)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum'
    })
    user_behavior['Total Data Volume'] = user_behavior['Total DL (Bytes)'] + user_behavior['Total UL (Bytes)']
    return user_behavior

def handle_missing_values(data):
    data.fillna(data.mean(numeric_only=True), inplace=True) 
    return data

def describe_data(data):
    print("\nDescriptive Statistics:")
    print(data.describe())

def create_deciles(user_behavior):
    user_behavior['Decile'] = pd.qcut(user_behavior['Dur. (ms)'], 10, labels=False)
    return user_behavior

def univariate_analysis(user_behavior):
    print("\nDispersion Parameters:")
    for col in user_behavior.select_dtypes(include=np.number).columns:
        variance = np.var(user_behavior[col])
        std_deviation = np.std(user_behavior[col])
        print(f"{col}:")
        print(f"  Variance: {variance}")
        print(f"  Standard Deviation: {std_deviation}")

def plot_session_duration_distribution(user_behavior):
    plt.figure(figsize=(10, 6))
    sns.histplot(user_behavior['Dur. (ms)'], bins=20, kde=True)
    plt.title("Distribution of Session Duration")
    plt.xlabel("Session Duration (ms)")
    plt.ylabel("Frequency")
    plt.show()

def bivariate_analysis(user_behavior):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Total Data Volume', y='Dur. (ms)', data=user_behavior)
    plt.title("Relationship Between Total Data Volume and Session Duration")
    plt.xlabel("Total Data Volume")
    plt.ylabel("Session Duration (ms)")
    plt.show()

def plot_correlation_matrix(user_behavior):
    correlation_matrix = user_behavior[['Total DL (Bytes)', 'Total UL (Bytes)', 'Total Data Volume']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def perform_pca(user_behavior):
    features = ['Total DL (Bytes)', 'Total UL (Bytes)', 'Dur. (ms)']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(user_behavior[features])

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_features)

    print("\nPCA Explained Variance Ratio:")
    print(pca.explained_variance_ratio_)

    pca_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df)
    plt.title("PCA of User Behavior Data")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()
