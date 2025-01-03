---
title : "Upload Pre-Processed CSV files"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.2.2. </b> "
---
{{% notice info %}}
In real-time data in a staging layer will be coming from through Dynamo DB or our database instance, but for this project, we are adding our data manually.
{{% /notice %}}

**1.** Choose **staging** folder, click **Upload** and then **Add files**. Select the pre-processed CSV files (`spotify_albums_data_2023.csv`, `spotify_artist_data_2023.csv`, `spotify_tracks_data_2023.csv`) from your local machine.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.2.upload-pre-processed-csv-files/choose_3_file_upload.png)

**2.** Click **Upload** to upload the files to the staging folder.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.2.upload-pre-processed-csv-files/upload_3_file_success.png)

> Nguyen Van Hao