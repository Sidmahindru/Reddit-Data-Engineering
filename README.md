# Reddit-Data-Engineering Project
# End to End Data Pipeline with Reddit Data, Apache Airflow, S3, AWS Glue, Athena, and Redshift

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Amazon Redshift data warehouse. The pipeline leverages a combination of tools and services including Python, Docker, Apache Airflow, Amazon S3, AWS Glue, Glue Crawler, Amazon Athena, and Amazon Redshift.


## Overview
The pipeline is designed to:

1. Extract data from Reddit API using PRAW python library.
2. Storing the Data in our local system.
3. Loading the raw data into an S3 bucket using Airflow. Airflow connects to an AWS S3 bucket using s3fs and stores the transformmed file in the bucket.
4. Transform the data using AWS Glue. Using Glue Crawler to infer schema and performing SQL querys using Amazon Athena.
5. Load the transformed data into Amazon Redshift for analytics and querying.

![reddit_airflow_dag](https://github.com/Sidmahindru/Reddit-Data-Engineering/assets/106438066/6e086e75-7233-41b5-930c-38a98736390a)

## Architecture
1. **Reddit API**: Source of the data.
2. **Apache Airflow**: Orchestrates the ETL process and manages task distribution.
4. **Amazon S3**: Raw data storage. Aamzon S3 is datalake on cloud.
5. **AWS Glue**: Data cataloging and ETL jobs.
6. **Glue Crawler**: Glue crawler was using to infer the schema of the transformed data.
7. **Amazon Athena**: SQL-based data transformation.
8. **Amazon Redshift**: Data warehousing and analytics. Amazon Redshift is datawarehouse on cloud.

   
![RedditDataEngineering](https://github.com/Sidmahindru/Reddit-Data-Engineering/assets/106438066/b31fccb9-dd35-44f1-8387-13926ececfe9)


