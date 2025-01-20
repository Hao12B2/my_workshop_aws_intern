---
title : "Viết các truy vấn SQL"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.5.2. </b> "
---
- Trong trình soạn thảo truy vấn Athena, viết các truy vấn SQL để phân tích dữ liệu
- Ví dụ truy vấn: `SELECT * FROM datawarehouse LIMIT 5;`. Truy vấn này sẽ lấy 5 bản ghi đầu tiên từ bảng **datawarehouse**.
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/write_query.png)

- Nhấn **Run** để thực thi câu lệnh SQL.
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/run_query_result.png)

- Kết quả sẽ được hiển thị trong trình soạn thảo truy vấn, và đầu ra sẽ được lưu trong bucket S3 đã chỉ định (athena-output-for-workshop).
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.2.write-sql-queries/output_saved_at_s3.png)

- Một ví dụ khác: Câu truy vấn này sẽ tìm ra 10 nghệ sĩ có nhiều người theo dõi nhất
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