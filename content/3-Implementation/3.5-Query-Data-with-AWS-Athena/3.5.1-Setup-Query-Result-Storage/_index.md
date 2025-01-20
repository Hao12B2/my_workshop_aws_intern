---
title : "Set up query result storage"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.5.1. </b> "
---
- Navigate to AWS `Athena` from the AWS Management Console
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/choose_athena.png)

- Click on **Launch query editor**
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/choose_launch_query_editor.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/query_editor_home.png)

- Before running any queries, you must specify a location for query results.
- Create a new S3 bucket named `athena-output-for-workshop`.
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/s3_output_name.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/create_s3_output_success.png)

- In the Athena settings, set the query result location to this new bucket
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/choose_s3_output_dataset_for_athena.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/set_query_result_location_success.png)

> Nguyen Van Hao