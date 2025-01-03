---
title : "Tạo các buckets và folders trong nó"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.2.1. </b> "
---
**1.** Trong AWS Management Console, tìm kiếm `S3` trong thanh tìm kiếm và chọn dịch vụ S3.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/choose_s3_service.png)

**2.** Nhấp vào **Create bucket**
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/choose_create_bucket.png)

**3.** Nhập tên bucket `my-workshop-bucket-spotify`, để tất cả các cài đặt khác mặc định và cuộn xuống để nhấp vào **Create bucket**
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/fill_bucket_name.png)
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/create_bucket.png)
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/create_bucket_success.png)

**4.** Sau đó, nhấp vào **bucket my-workshop-bucket-spotify** mà bạn vừa tạo và nhấp vào **Create folder**
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/choose_create_folder.png)

**5.** Tên thư mục: Nhập `staging` và nhấp vào **Create folder**.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/create_folder_staging.png)
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/create_folder_staging_success.png)

**6.** Lặp lại các bước trên để tạo một thư mục khác có tên `datawarehouse`.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/create_folder_datawarehouse.png)
![](/images/3.implementation/3.2.create-s3-buckets/3.2.1.create-buckets-and-folders/create_folder_datawarehouse_success.png)

> Nguyễn Văn Hào