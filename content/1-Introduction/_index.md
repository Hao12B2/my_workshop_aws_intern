---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

### Overview
In this workshop, we will build a comprehensive data engineering pipeline using AWS cloud services. While we demonstrate the pipeline with the Spotify dataset, the project architecture is flexible enough to handle any dataset. The focus is on processing and analyzing data using various AWS tools like S3, Glue and Athena.

### Workshop Architecture Overview
![workshop architecture](/images/architecture_02.png)
- **Staging Layer**: Raw data is stored in an S3 bucket.
- **ETL Pipeline**: AWS Glue processes and transfers data from the staging layer to the data warehouse.
- **Data Warehouse**: Processed data is stored in another S3 bucket.
- **Data Catalog**: AWS Glue Crawler creates a database and tables for the data warehouse.
- **Data Analysis**: AWS Athena queries the processed data.

> Nguyen Van Hao