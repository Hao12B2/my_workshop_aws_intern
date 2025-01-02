---
title : "Giới thiệu"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

### Tổng quan
Trong workshop này, chúng ta sẽ xây dựng một pipeline xử lý dữ liệu toàn diện sử dụng các dịch vụ đám mây AWS. Mặc dù chúng ta sẽ minh họa pipeline với bộ dữ liệu Spotify, tuy nhiên, kiến trúc dự án đủ linh hoạt để xử lý bất kỳ bộ dữ liệu nào. Trọng tâm là xử lý và phân tích dữ liệu bằng các công cụ AWS như S3, Glue, Athena và QuickSight.

### Tổng quan về kiến trúc workshop
![workshop architecture](/images/arc_02.png)
- **Lớp Staging**: Dữ liệu thô được lưu trữ trong một bucket S3.
- **Pipeline ETL**: AWS Glue xử lý và chuyển dữ liệu từ lớp staging sang kho dữ liệu.
- **Kho Dữ liệu**: Dữ liệu đã xử lý được lưu trữ trong một bucket S3 khác.
- **Danh mục Dữ liệu**: AWS Glue Crawler tạo cơ sở dữ liệu và các bảng cho kho dữ liệu.
- **Phân tích Dữ liệu**: AWS Athena truy vấn dữ liệu đã xử lý.
- **Trực quan hóa Dữ liệu**: AWS QuickSight trực quan hóa dữ liệu.

> Nguyễn Văn Hào