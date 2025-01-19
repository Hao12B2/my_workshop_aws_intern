---
title : "Tạo danh mục dữ liệu với AWS Glue Crawler"
date :  "`r Sys.Date()`" 
weight : 4 
chapter : false
pre : " <b> 3.4. </b> "
---

**1. Tạo một Crawler mới**
- Trong bảng điều khiển AWS Glue, nhấp vào **Crawlers** dưới phần **Data Catalog**. Sau đó, nhấp vào nút **Create crawler**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/crawler_home.png)

- **Crawler name**: Nhập `spotify_crawler` và nhấp **Next**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_1_crawler_name.png)

- Chọn **Add a data source**
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_home_click_add_datasource.png)

- **Data store**: Chọn S3, cung cấp đường dẫn đến bucket **datawarehouse** trong phần **S3 path** và nhấp **Add an S3 data source**. Sau đó, nhấp **Next**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_click_add_datasource.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_choose_s3_datawarehouse_datasource.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_2_done.png)

- Chọn IAM role mà chúng ta đã tạo trước đó và trước khi làm điều này, hãy thêm chính sách **AWSGlueServiceRole** vào role này. Sau đó, nhấp **Next**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_home.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_choose_iam_role.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_add_permission_role.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_policy_attach_role_success.png)

**2. Tạo một cơ sở dữ liệu mới**
- Mở tab trùng lặp. Đi đến AWS Glue >> Data catalog >> Databases, và tạo một cơ sở dữ liệu mới bằng cách chọn **Add database**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_database_home.png)

- **Database Name**: Nhập `spotify_db`.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_database_name.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_3_create_database_success.png)

- Quay lại Crawlers, chọn cơ sở dữ liệu đã tạo, nhấp **Next** và **Create the Crawler**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_4_choose_target_db.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_4_create_crawler.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/step_4_create_crawler_success.png)

**3. Chạy Crawler**
- Sau khi thiết lập crawler, nhấp **Run crawler**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/choose_run_crawler.png)
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/crawler_run_success.png)

- Crawler sẽ quét dữ liệu trong thư mục **datawarehouse** và tạo các bảng tương ứng trong cơ sở dữ liệu **spotify_db**.
![](/images/3.implementation/3.4.create-a-data-catalog-with-aws-glue-crawler/check_spotify_db.png)

> Nguyễn Văn Hào
