
# 10 Academy: Artificial Intelligence Mastery - Week 2 Challenge
---

## Situational Overview

You are working for a wealthy investor that specialises in purchasing assets that are undervalued.  This investor’s due diligence on all purchases includes a detailed analysis of the data that underlies the business, to try to understand the fundamentals of the business and especially to identify opportunities to drive profitability by changing the focus of which products or services are being offered.

Your last role with this investor saw you do a rich analysis of a delivery company and you helped to identify that delivery to university students was the most profitable route to follow, and your analysis helped the investor purchase this delivery company and ramp up profits by 25% within 6 months through focussing on the most profitable aspect of the business.  This was driven by university students always being hungry, awake at all hours, willing to purchase from a limited food menu, and tending to live within a small geographical area.

The investor is interested in purchasing TellCo, an existing mobile service provider in the Republic of Pefkakia.  TellCo’s current owners have been willing to share their financial information but have never employed anyone to look at the data that is generated automatically by their systems.

Your employer wants you to provide a report to analyse opportunities for growth and make a recommendation on whether TellCo is worth buying or selling.  You will do this by analysing a telecommunication dataset that contains useful information about the customers & their activities on the network. You will deliver insights you managed to extract to your employer through an easy-to-use web-based dashboard and a written report. 

---

## Data

Data is sourced from a month's aggregation of xDR records:
- We have sourced the data from a month's aggregation of xDR records here
- The description for attributes can be found here
- This data should be extracted from a PostgreSQL database, and we've included both the database schema and the corresponding SQL file here.    

---


## Instructions

At the end of this week, you are expected to have a complete project that has
●	Reusable code for data preparation and cleaning.
●	Code connected using scikit pipeline or other form of chaining multiple EDA steps  
●	Beautiful and insightful Streamlit dashboard that shows your findings.
●	SQL database as feature store which can be used to store selected features for dashboard visualization and model training.
●	Your project folder structure:
○	Has unit tests with good test coverage
○	Has CI/CD setup - using Github Actions
○	Has Dockerfile to build it as a docker image
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
├── notebooks/
│   ├──overview_analysis.ipynb
│   ├──user_engagement_analysis.ipynb
│   ├──user_Expriance_analysis.ipynb
│   ├──user_satisfaction_analysis.ipynb
│   ├──__init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├──overview_analysis.py
    ├──user_engagement_analysis.py
    ├──user_Expriance_analysis.py
    ├──user_satisfaction_analysis.py
    ├── __init__.py
    └── README.md

The global objective is divided into 4 sub-objectives 
●	User Overview analysis
●	User Engagement analysis
●	User Experience analysis
●	User Satisfaction Analysis


---

## Tasks

### Task 1: User Overview Analysis

The lifeblood of any business is its customers. Businesses are always finding ways to better understand their customers so that they can provide more efficient and tailored solutions to them. 
Exploratory Data Analysis is a fundamental step in the data science process. It involves all the processes used to familiarise oneself with the data and explore initial insights that will inform further steps in the data science process.

It is always better to explore each data set using multiple exploratory techniques and compare the results. The goal of this step is to understand the dataset and identify the missing values & outliers if any using visual and quantitative methods to get a sense of the story it tells. It suggests the next logical steps, questions, or areas of research for your project.

For the actual telecom dataset, you‘re expected to conduct a full User Overview analysis & the following sub-tasks are your guidance: 
- Start by identifying the top 10 handsets used by the customers.
- Then, identify the top 3 handset manufacturers
- Next, identify the top 5 handsets per top 3 handset manufacturer
- Make a short interpretation and recommendation to marketing teams
In telecommunication, CDR or Call Detail Record is the voice channel and XDR is the data channel equivalent. So here, consider xDR as data sessions Detail Record. In xDR, user behavior can be tracked through the following applications:  Social Media, Google, Email, YouTube, Netflix, Gaming, and others. 
Task 1.1 - Your employer wants to have an overview of the users’ behavior on those applications.   
-	Aggregate per user the following information in the column  
-	number of xDR sessions
-	Session duration
-	the total download (DL) and upload (UL) data
-	the total data volume (in Bytes) during this session for each application

Task 1.2 - Conduct an exploratory data analysis on those data & communicate useful insights. Ensure that you identify and treat all missing values and outliers in the dataset by replacing them with the mean or any possible solution of the corresponding column.
You’re expected to report about the following using Python script and slide  :
-	Describe all relevant variables and associated data types (slide). findings. 
-	Variable transformations – segment the users into the top five decile classes based on the total duration for all sessions and compute the total data (DL+UL) per decile class. 
-	Analyze the basic metrics (mean, median, etc) in the Dataset (explain) & their importance for the global objective.
-	Conduct a Non-Graphical Univariate Analysis by computing dispersion parameters for each quantitative variable and provide useful interpretation. 
-	Conduct a Graphical Univariate Analysis by identifying the most suitable plotting options for each variable and interpret your findings.
-	Bivariate Analysis – explore the relationship between each application & the total DL+UL data using appropriate methods and interpret your result
-	Correlation Analysis – compute a correlation matrix for the following variables and interpret your findings: Social Media data, Google data, Email data, YouTube data, Netflix data, Gaming data, and Other data 
-	Dimensionality Reduction – perform a principal component analysis to reduce the dimensions of your data and provide a useful interpretation of the results (Provide your interpretation in four (4) bullet points maximum). 


### Task 2: User Engagement Analysis

As telecom brands are the data providers of all online activities, meeting user requirements, and creating an engaging user experience is a prerequisite for them. Building & improving the QoS (Quality of Service) to leverage the mobile platforms and to get more users for the business is good but the success of the business would be determined by the user engagement and activity of the customers on available apps. 

In telecommunication, tracking the user activities on the database sessions is a good starting point to appreciate the user engagement for the overall applications and per application as well. If we can determine the level of engagement of a random user for any application, then it could help the technical teams of the business to know where to concentrate network resources for different clusters of customers based on the engagement scores.

In the current dataset you’re expected to track the user’s engagement using the following engagement metrics: 
●	sessions frequency 
●	the duration of the session 
●	the session total traffic (download and upload (bytes))

Task 2.1 - Following the above, perform the following tasks:
●	Aggregate the above metrics per customer id (MSISDN) and report the top 10 customers per engagement metric 
●	Normalize each engagement metric and run a k-means (k=3) to classify customers in three groups of engagement. 
●	Compute the minimum, maximum, average & total non-normalized metrics for each cluster. Interpret your results visually with accompanying text explaining your findings.
●	Aggregate user total traffic per application and derive the top 10 most engaged users per application
●	Plot the top 3 most used applications using appropriate charts.  
●	Using k-means clustering algorithm, group users in k engagement clusters based on the engagement metrics: 
○	What is the optimized value of k (use elbow method for this)?  
○	Interpret your findings. 

### Task 3: Experience Analytics
The Telecommunication industry has experienced a great revolution in the last decade. Mobile devices have become the new fashion trend and play a vital role in everyone's life. The success of the mobile industry is largely dependent on its consumers. Therefore, it is necessary for the vendors to focus on their target audience i.e. what are the needs and requirements of their consumers and how they feel and perceive their products. Tracking & evaluating customers’ experience can help organizations to optimize their products and services so that it meet the evolving user expectations, needs, and acceptance.

In the telecommunication industry, the user experience is related, most of the time, to network parameter performances or the customers’ device characteristics.  

In this section, you’re expected to focus on network parameters like TCP retransmission, Round Trip Time (RTT), Throughput, and the customers’ device characteristics like the handset type to conduct a deep user experience analysis. The network parameters are all columns in the dataset. The following questions are your guidance to complete the task. For this task, you need a Python script that includes all solutions to tasks.

Task 3. 1 - Aggregate, per customer, the following information (treat missing & outliers by replacing with the mean or the mode of the corresponding variable):
●	Average TCP retransmission
●	Average RTT
●	Handset type
●	Average throughput
Task 3.2 - Compute & list 10 of the top, bottom, and most frequent:
a.	TCP values in the dataset. 
b.	RTT values in the dataset.
c.	Throughput values in the dataset.
Task 3.3 - Compute & report:
d.	The distribution of the average throughput per handset type and provide interpretation for your findings.
e.	The average TCP retransmission view per handset type and provide interpretation for your findings.
Task 3.4 - Using the experience metrics above, perform a k-means clustering (where k = 3) to segment users into groups of experiences and provide a brief description of each cluster. (The description must define each group based on your understanding of the data)

### Task 4: Satisfaction Analysis

Assuming that the satisfaction of a user is dependent on user engagement and experience, you’re expected in this section to analyze customer satisfaction in depth. The following tasks will guide you: 

Based on the engagement analysis + the experience analysis you conducted above,
Task 4.1  - Write a Python program to assign:
a.	engagement score to each user. Consider the engagement score as the Euclidean distance between the user data point & the less engaged cluster (use the first clustering for this) (Euclidean Distance)
b.	experience score for each user. Consider the experience score as the Euclidean distance between the user data point & the worst experience cluster. 
Task 4.2 - Consider the average of both engagement & experience scores as  the satisfaction score & report the top 10 satisfied customer 
Task 4.3 - Build a regression model of your choice to predict the satisfaction score of a customer. 
Task 4.4 - Run a k-means (k=2) on the engagement & the experience score. 
Task 4.5  - Aggregate the average satisfaction & experience score per cluster. 
Task 4.6 - Export your final table containing all user ID + engagement, experience & satisfaction scores in your local MySQL database. Report a screenshot of a select query output on the exported table. 

### Task 5: Dashboard Development

●	Tasks:
○	Designing and developing a dashboard using Visualization tools  to visualize data insights.
○	Separate each page by task title for example User overview analysis, User engagement analysis, Experience anysis, Satisfaction analysis. Add a plot for each page. 
●	KPIs
○	Dashboard Usability: Ease of use, with intuitive navigation and clear labels.
○	Interactive Elements: Effective use of widgets to enhance user engagement.
○	Visual Appeal: Clean and professional design that effectively communicates data insights.
○	Deployment Success: Fully functional deployment, accessible via a public URL.
