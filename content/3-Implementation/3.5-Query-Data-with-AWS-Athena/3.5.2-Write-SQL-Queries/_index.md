---
title : "Write SQL Queries"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.5.2. </b> "
---
-  In the Athena query editor, write SQL queries to analyze the data
-  Example query: `SELECT * FROM datawarehouse LIMIT 5;`. This query will fetch the first 5 records from the **datawarehouse** table.
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/write_query.png)

- Click **Run** to execute the SQL statement.
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/run_query_result.png)

- The results will be displayed in the query editor, and the output will be saved in the specified S3 bucket (athena-output-for-workshop).
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/output_saved_at_s3.png)

- Another example: This query will find the 10 artists with the most followers
```sql
SELECT name, followers
FROM (
    SELECT DISTINCT name, CAST(followers AS INTEGER) AS followers
    FROM datawarehouse
) AS subquery
ORDER BY followers DESC
LIMIT 10;
```

![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/query_top_10_artist.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/result_top_10_artist.png)

> Nguyen Van Hao