import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_data_from_postgres
from new_engagement_analysis import aggregate_metrics, top_10_customers
from expriance_analytics import aggregate_per_customer, kmeans_clustering, treat_missing_and_outliers
from satisfaction_analysis import calculate_satisfaction_score

# Configure Streamlit
st.set_page_config(page_title="Telecom Insights Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Dashboard Navigation")
page = st.sidebar.radio("Go to", ["User Overview Analysis", 
                                  "User Engagement Analysis", 
                                  "Experience Analysis", 
                                  "Satisfaction Analysis"])

# Database query for loading data
query = "SELECT * FROM xdr_data"
df = load_data_from_postgres(query)
st.write(df)  # Display the dataframe to verify data loading

# Define the analysis functions
def user_engagement_analysis():
    st.title("User Engagement Analysis")
    st.subheader("Engagement Metrics")
    engagement_data = aggregate_metrics(df)
    st.dataframe(engagement_data.head())

    st.subheader("Top 10 Customers by Engagement Metrics")
    top_10_sessions, top_10_duration, top_10_data_volume = top_10_customers(engagement_data)

    fig, ax = plt.subplots()
    sns.barplot(x=top_10_sessions['sessions_frequency'], y=top_10_sessions['MSISDN/Number'], ax=ax)
    ax.set_title("Top 10 Customers by Sessions Frequency")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(x=top_10_duration['total_session_duration'], y=top_10_duration['MSISDN/Number'], ax=ax)
    ax.set_title("Top 10 Customers by Total Session Duration")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(x=top_10_data_volume['total_data_volume'], y=top_10_data_volume['MSISDN/Number'], ax=ax)
    ax.set_title("Top 10 Customers by Total Data Volume")
    st.pyplot(fig)

def experience_analysis():
    st.title("Experience Analysis")
    st.subheader("Experience Metrics")
    experience_data = aggregate_per_customer(df)
    st.dataframe(experience_data.head())

    # Clean the data to handle missing values
    experience_data = treat_missing_and_outliers(experience_data)

    st.subheader("Experience Clustering")
    experience_data, kmeans = kmeans_clustering(experience_data, n_clusters=3)
    fig, ax = plt.subplots()
    sns.scatterplot(data=experience_data, x='avg_rtt', y='avg_throughput', 
                    hue='cluster', palette='coolwarm', ax=ax)
    ax.set_title("Experience Clusters")
    st.pyplot(fig)

def satisfaction_analysis():
    st.title("Satisfaction Analysis")
    st.subheader("Satisfaction Scores")
    satisfaction_data = calculate_satisfaction_score(df)
    st.dataframe(satisfaction_data.head())

    fig, ax = plt.subplots()
    sns.histplot(satisfaction_data['satisfaction_score'], bins=20, kde=True, ax=ax)
    ax.set_title("Distribution of Satisfaction Scores")
    st.pyplot(fig)

# Call the appropriate analysis function based on the selected page
if page == "User Engagement Analysis":
    user_engagement_analysis()
elif page == "Experience Analysis":
    experience_analysis()
elif page == "Satisfaction Analysis":
    satisfaction_analysis()