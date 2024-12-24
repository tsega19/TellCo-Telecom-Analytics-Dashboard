import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def display_data_info(data):
    print("Dataset Overview:")
    print(data.info())
    print("\nSample Data:")
    print(data.head())

def numerical_summary(data):
    print("\nNumerical Summary:")
    print(data.describe())


def catagorical_summary(data):
    print("\nCategorical Summary:")
    print(data.describe(include=['O']))

def plt_hist(data, column):
    plt.hist(data[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
# plot catagorical distrubution data for each catagorical datas
def plt_catagorical(data):
    categorical_columns = data.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        column_count = data[column].value_counts()
        column_count.plot(kind='bar')
        plt.title(f'Categorical distribution of {column}')
        plt.ylabel('Frequency')
        plt.show()
# plot the correlation matrix of the data
def plt_corr(data):
    corr = data.corr()
    sns.heatmap(corr, annot=True)
    plt.title('Correlation Matrix')
    plt.show()
   