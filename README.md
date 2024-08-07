DBT-RETAIL-PIPELINE

Overview
========

The DBT-RETAIL-PIPELINE project implements a comprehensive data pipeline for retail data using Apache Airflow, DBT (Data Build Tool), and Google Cloud Platform (GCP) services. This pipeline is designed to automate the ETL (Extract, Transform, Load) process, ensuring efficient data processing, quality checks, and reporting.Key components include Astro CLI for Airflow management, Astro SDK for data ingestion, and Cosmos for DBT integration.

Project Architecture

The project leverages a modular architecture to streamline data processing and analysis:
================

Data Flow
1. Data Ingestion:
    * Raw retail data is uploaded to Google Cloud Storage (GCS).
2. Data Loading:
    * The data is loaded from GCS into BigQuery.
3. Data Transformation:
    * DBT models transform the data, creating structured tables and reports.
4. Data Quality Checks:
    * Soda checks ensure the integrity and accuracy of the data.
5. Reporting:
    * Final reports are generated using DBT models, providing insights into retail operations.

Components
1. Apache Airflow DAG
    * Purpose: Orchestrates the ETL process, managing dependencies between tasks and scheduling.
    * Key Tasks:
        * Upload CSV to GCS: Transfers raw data from local storage to Google Cloud Storage.
        * Create BigQuery Dataset: Sets up the dataset in BigQuery.
        * Load Data from GCS to BigQuery: Imports the data from GCS into BigQuery.
        * Data Quality Checks: Executes data quality checks using Soda.
        * DBT Transformations: Performs data transformation and reporting using DBT.
2. DBT Models
    * Purpose: Defines data transformations and reporting queries.
    * Location: Located in the models and transform folders.
    * Key Files:
        * report: Contains SQL queries for generating reports on country invoices, product sales, and monthly revenue.
        * transform: Includes SQL transformations for cleaning and structuring data.
3. Soda Checks
    * Purpose: Validates data quality by checking for missing values and other anomalies.
    * Location: Located in the checks folder.
    * Key Files:
        * report_customer_invoices.yml: Checks for missing country values and total invoice counts.
        * report_product_invoices.yml: Validates product stock codes and quantities sold.
        * report_year_invoices.yml: Ensures non-negative invoice counts.
4. Dockerfile
    * Purpose: Creates a Docker image with the necessary environment for running Airflow and DBT.
    * Includes:
        * Virtual environments for Soda and DBT.
        * Installation of required packages.
5. Encoding Script
    * Purpose: Handles CSV file encoding issues to ensure data integrity.
    * Key Functions:
        * Reads CSV files with different encodings.
        * Saves the corrected file in UTF-8 encoding.

Potential Issues and Solutions
===========================

1. Encoding Errors:
    * Issue: CSV files may have encoding issues.
    * Solution: Use encoding.py to handle different encodings and save the file in UTF-8.
2. Dependency Issues:
    * Issue: Conflicts or missing dependencies may arise.
    * Solution: Ensure all dependencies are listed in the Dockerfile and install them in isolated environments.
3. GCP Connections:
    * Issue: Issues with GCP connections can occur.
    * Solution: Verify GCP credentials and ensure service roles for service accounts have the necessary permissions.
4. Service Roles and Permissions:
    * Issue: Insufficient permissions for GCP resources.
    * Solution: Assign appropriate IAM roles to the service accounts used by Airflow and other services.

Future Add-Ons
=================================

1. Real-Time Data Processing:
    * Integrate Apache Kafka or AWS Kinesis for streaming data.
2. Advanced Analytics:
    * Implement machine learning models using AWS SageMaker or Google AI Platform for advanced analytics.
3. Enhanced Dashboarding:
    * Use visualization tools like Tableau or Power BI for advanced reporting and dashboards.
4. Automated Reporting:
    * Set up automated reporting using tools like IBM Cognos Analytics or Google Data Studio.

<img width="1470" alt="Screenshot 2024-08-05 at 4 28 27 AM" src="https://github.com/user-attachments/assets/b3ba914f-45e2-4eaa-946e-2ea5d3f73451">


<img width="1470" alt="Screenshot 2024-08-05 at 4 37 39 AM" src="https://github.com/user-attachments/assets/619b7e91-dbf9-40b2-8cae-65be8b922763">


<img width="1470" alt="Screenshot 2024-08-05 at 4 43 52 AM" src="https://github.com/user-attachments/assets/9460e9bc-2ce4-4eaf-9317-eee8a42ed66b">
