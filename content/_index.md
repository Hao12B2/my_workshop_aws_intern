---
title : "BUILD A DATA ENGINEERING PIPELINE WITH AWS TO ANALYZE SPOTIFY DATA"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
---

# BUILD A DATA ENGINEERING PIPELINE WITH AWS TO ANALYZE SPOTIFY DATA
![aws services](/images/aws_services_01.png)
### Overview
In this workshop, we will build a comprehensive data engineering pipeline using AWS cloud services. While we demonstrate the pipeline with the Spotify dataset, the project architecture is flexible enough to handle any dataset. The focus is on processing and analyzing data using various AWS tools like S3, Glue and Athena.

### Project Architecture Overview
![workshop architecture](/images/arc_02.png)
- **Staging Layer**: Raw data is stored in an S3 bucket.
- **ETL Pipeline**: AWS Glue processes and transfers data from the staging layer to the data warehouse.
- **Data Warehouse**: Processed data is stored in another S3 bucket.
- **Data Catalog**: AWS Glue Crawler creates a database and tables for the data warehouse.
- **Data Analysis**: AWS Athena queries the processed data.

### Content
 1. [Introduction](1-introduction/)
 2. [Preparation](2-prerequiste/)
 3. [Implementation](3-implementation/)
 4. [Clean up resources](4-cleanupresources/)

> Nguyen Van Hao