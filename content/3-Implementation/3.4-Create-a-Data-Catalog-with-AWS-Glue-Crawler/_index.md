---
title : "Create a data catalog with AWS Glue Crawler"
date :  "`r Sys.Date()`" 
weight : 4 
chapter : false
pre : " <b> 3.4. </b> "
---
**1. Create a New Crawler**
- In the AWS Glue dashboard, click on **Crawlers** under the **Data Catalog** section. Then, click on **Create crawler** button.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/crawler_home.png)

- **Crawler name**: Enter `spotify_crawler` and click **Next**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_1_crawler_name.png)

- Choose **Add a data source**
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_home_click_add_datasource.png)

- **Data store**: Select S3, provide the path to the **datawarehouse** bucket in **S3 path** section and click **Add an S3 data source**. After this, click **Next**
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_click_add_datasource.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_choose_s3_datawarehouse_datasource.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_done.png)

- Select the IAM role we created earlier and before this please do add another policy **AWSGlueServiceRole** to this role. Then, click **Next**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_home.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_choose_iam_role.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_add_permission_role.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_policy_attach_role_success.png)

**2. Create a New Database**
- Open the duplicate tab. Go to the AWS Glue >> Data catalog >> Databases, and create a new database by selecting **Add database**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_database_home.png)

- **Database Name**: Enter `spotify_db`.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_database_name.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_create_database_success.png)

- Back to the Crawlers, select the created database, Click **Next** and **Create the Crawler**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_4_choose_target_db.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_4_create_crawler.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_4_create_crawler_success.png)

**3. Run the Crawler**
- After setting up the crawler, click **Run crawler**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/choose_run_crawler.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/crawler_run_success.png)

- The crawler will scan the data in the **datawarehouse** folder and create corresponding tables in the **spotify_db** database.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/check_spotify_db.png)

> Nguyen Van Hao