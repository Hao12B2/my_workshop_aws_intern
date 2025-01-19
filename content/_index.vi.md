---
title : "XÂY DỰNG QUY TRÌNH KỸ THUẬT DỮ LIỆU PHÂN TÍCH DỮ LIỆU SPOTIFY VỚI AWS"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
---

# XÂY DỰNG QUY TRÌNH KỸ THUẬT DỮ LIỆU PHÂN TÍCH DỮ LIỆU SPOTIFY VỚI AWS
![aws services](/images/aws_services_01.png)
### Tổng quan
Trong workshop này, chúng ta sẽ xây dựng một quy trình kỹ thuật dữ liệu toàn diện sử dụng các dịch vụ đám mây AWS. Mặc dù chúng ta sẽ minh họa quy trình với bộ dữ liệu Spotify, kiến trúc dự án đủ linh hoạt để xử lý bất kỳ bộ dữ liệu nào. Trọng tâm là xử lý và phân tích dữ liệu bằng các công cụ AWS như S3, Glue và Athena.

### Tổng quan về Kiến trúc Dự án
![workshop architecture](/images/architecture_02.png)
- **Lớp Staging**: Dữ liệu thô được lưu trữ trong một bucket S3.
- **ETL Pipeline**: AWS Glue xử lý và chuyển dữ liệu từ lớp staging sang kho dữ liệu.
- **Kho Dữ Liệu**: Dữ liệu đã xử lý được lưu trữ trong một bucket S3 khác.
- **Danh Mục Dữ Liệu**: AWS Glue Crawler tạo cơ sở dữ liệu và các bảng cho kho dữ liệu.
- **Phân Tích Dữ Liệu**: AWS Athena truy vấn dữ liệu đã xử lý.

### Nội dung
 1. [Giới thiệu](1-introduction/)
 2. [Chuẩn bị](2-prerequiste/)
 3. [Triển khai](3-implementation/)
 4. [Dọn dẹp tài nguyên](4-cleanupresources/)

> Nguyễn Văn Hào