---
title : "Chuẩn bị"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2. </b> "
---

### Yêu cầu
- Một tài khoản AWS (bắt buộc)
- Hiểu biết cơ bản về các dịch vụ AWS như S3, Glue và Athena

### Các dịch vụ AWS được sử dụng
- **Amazon S3**: Để lưu trữ dữ liệu thô và đã xử lý.
- **AWS Glue**: Để xây dựng và quản lý các pipeline ETL.
- **AWS Athena**: Để truy vấn dữ liệu bằng cú pháp giống SQL.

### Nguồn dữ liệu
Dữ liệu được sử dụng trong hội thảo này được lấy từ [Spotify Dataset 2023](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023) có sẵn trên Kaggle. Bộ dữ liệu, được tạo bởi Tony Gordon Jr., bao gồm thông tin chi tiết về các album, nghệ sĩ, bài hát của Spotify và các đặc điểm âm thanh khác nhau như khả năng nhảy, năng lượng, độ ồn và nhiều hơn nữa. Bộ dữ liệu có sẵn ở định dạng CSV và đã được tiền xử lý để sử dụng trong dự án này.

### Mô tả dữ liệu
- Albums: Chứa chi tiết về tất cả các album, bao gồm ID album, tên, độ phổ biến và ngày phát hành.
- Artists: Chứa thông tin về các nghệ sĩ, bao gồm tên của họ, số lượng người theo dõi và thể loại.
- Tracks: Chứa dữ liệu cấp bài hát, bao gồm ID bài hát, độ phổ biến và các đặc điểm khác như khả năng nhảy và năng lượng.
- Spotify Features: Chứa các đặc điểm âm thanh khác nhau như độ ồn, chế độ, độ nói và cảm xúc.

> Nguyễn Văn Hào