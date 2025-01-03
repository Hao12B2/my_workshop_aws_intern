---
title : "Tải các tệp CSV đã được tiền xử lý"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.2.2. </b> "
---
{{% notice info %}}
Trong thời gian thực, dữ liệu trong lớp staging sẽ đến từ Dynamo DB hoặc instance cơ sở dữ liệu của chúng ta, nhưng đối với dự án này, chúng ta sẽ thêm dữ liệu thủ công.
{{% /notice %}}

**1.** Chọn thư mục **staging**, nhấp vào **Upload** và sau đó nhấp vào **Add files**. Chọn các tệp CSV đã được tiền xử lý (`spotify_albums_data_2023.csv`, `spotify_artist_data_2023.csv`, `spotify_tracks_data_2023.csv`) từ máy tính của bạn.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.2.upload-pre-processed-csv-files/choose_3_file_upload.png)


**2.** Nhấp vào **Upload** để tải các tệp lên thư mục staging.
![](/images/3.implementation/3.2.create-s3-buckets/3.2.2.upload-pre-processed-csv-files/upload_3_file_success.png)

> Nguyễn Văn Hào