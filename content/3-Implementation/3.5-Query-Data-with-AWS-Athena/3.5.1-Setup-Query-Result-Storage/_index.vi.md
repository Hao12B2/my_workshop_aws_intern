---
title : "Thiết lập lưu trữ kết quả truy vấn"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.5.1. </b> "
---
- Điều hướng đến AWS `Athena` từ AWS Management Console
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/choose_athena.png)

- Nhấp vào **Launch query editor**
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/choose_launch_query_editor.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/query_editor_home.png)

- Trước khi chạy bất kỳ truy vấn nào, bạn phải chỉ định một vị trí cho kết quả truy vấn.
- Tạo một S3 bucket mới có tên là `athena-output-for-workshop`.
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/s3_output_name.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/create_s3_output_success.png)

- Trong cài đặt Athena, đặt vị trí kết quả truy vấn vào bucket mới này
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/choose_s3_output_dataset_for_athena.png)
![](/images/3.implementation/3.5.query-data-with-aws-athena/3.5.1.setup-query-result-storage/set_query_result_location_success.png)

> Nguyen Van Hao