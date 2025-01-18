---
title : "Config ETL Job with AWS Glue"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.3.2. </b> "
---
In this section, we'll try to create a data pipeline that will transfer our data from the staging layer to the data warehouse. we'll be making use of AWS Glue to create a data pipeline. AWS glue is a managed service provided by AWS to create a data pipeline.

**1. Create a New Glue Job**
- In the AWS Management Console, search for `Glue` in the search bar and select the AWS Glue service.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_glue.png)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/glue_home.png)

- In the AWS Glue dashboard, click on **Visual ETL** under the **ETL jobs** section.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_visual_ETL.png)

- Click **Visual ETL** under Create job, we go to **Visual ETL** home.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/visual_ETL_home.png)

**2. Set Up Data Sources**
- In **Add nodes** panel, click on Amazon S3 in Sources section 3 times to create 3 sources because we have 3 CSV files.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/add_3_sources.png)

- Select the first Amazon S3 bucket and rename it with `Artist`. Click on **Browse S3** and select the file from the **`s3://my-workshop-bucket-spotify/staging/spotify_artist_data_2023.csv`**. After that, select the **Data format** as CSV.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_first_source_artist.png)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_artist_first_source.png)

- Repeat the same steps for the other 2 S3 Buckets.
  - `Albums`
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_second_source_albums.png)
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_albums_second_source.png)
  - `Tracks`
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_third_source_tracks.png)
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_tracks_third_source.png)

**3. Configure Data Transformations**
- Now to join **Albums** and **Artist**, click on the ADD symbol, select join from **Transforms** and connect nodes as per the image below.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_join_artist_albums.png)

- After joining the nodes of both the buckets to the Join Transform. Add a condition where Albums **artist_id =** Artist **id** and rename the join `Join Albums and Artist`.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_transform_join_albums_artist.png)

- Now add another Join Transfrom to join **Tracks** s3 bucket and **Join Albums and Artist**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_join_tracks_with_albums_and_artist.png)

- Now select the Join and add the condition Join Albums and Artist **track_id =** Tracks **id** and rename the join as `Join with Tracks`.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_transform_join_with_tracks.png)

- To drop unnecessary columns, select **Drop Fields** from Transforms node.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_drop_fields.png)

- We remove duplicate columns and Identical columns we don't need. Here **id** (Tracks **id**) is inner join to Artist **id** so select **id**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_drop_fields.png)

**4. Set Up Data Target**
- Next step is to add the destination. Click Amazon S3 bucket in the Targets section
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_target.png)

- Rename the `Destination` node and add the S3 Target location **`s3://my-workshop-bucket-spotify/datawarehouse/`** and make sure the compression type is Snappy.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_target.png)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_destination.png)

- Enter a name like `My Workshop AWS Intern Spotify` into Name in Job details tab and choose IAM Role **`glue_s3_access`** created earlier.
- **Type**: Choose Spark
- **Glue Version**: Choose the latest Glue version available.
- **Language**: Select Python 3
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/job_details_rename_and_choose_role.png)

- **Requested number of workers**: 4 (can enter other)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_worker_numbers.png) 

- Leave the rest default and click **Save**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/save_job_success.png)

**5. Run the Glue Job**
-  Review your job settings.
-  Click **Run job** in **Runs** tab to start the ETL process, transforming and moving data from the staging layer to the data warehouse.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_run_job.png)

![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/run_job_started.png)

- Wait a few minutes, the job ran successfully.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/run_job_success.png)

- Check the **datawarehouse** S3 bucket to see if the files have been written.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/file_written_into_destination.png)

> Nguyen Van Hao