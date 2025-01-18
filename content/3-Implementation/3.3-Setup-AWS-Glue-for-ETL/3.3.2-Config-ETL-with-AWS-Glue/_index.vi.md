---
title : "Cấu hình ETL Job với AWS Glue"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 3.3.2. </b> "
---

Trong phần này, chúng ta sẽ cố gắng tạo một pipeline dữ liệu để chuyển dữ liệu từ lớp staging sang kho dữ liệu. Chúng ta sẽ sử dụng AWS Glue để tạo pipeline dữ liệu. AWS Glue là một dịch vụ được quản lý bởi AWS để tạo pipeline dữ liệu.

**1. Tạo một Glue Job mới**
- Trong AWS Management Console, tìm kiếm `Glue` trong thanh tìm kiếm và chọn dịch vụ AWS Glue.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_glue.png)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/glue_home.png)

- Trong bảng điều khiển AWS Glue, nhấp vào **Visual ETL** dưới phần **ETL jobs**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_visual_ETL.png)

- Nhấp vào **Visual ETL** dưới mục Create job, chúng ta sẽ vào trang chủ **Visual ETL**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/visual_ETL_home.png)

**2. Thiết lập nguồn dữ liệu**
- Trong bảng **Add nodes**, nhấp vào Amazon S3 trong phần Sources 3 lần để tạo 3 nguồn vì chúng ta có 3 tệp CSV.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/add_3_sources.png)

- Chọn bucket Amazon S3 đầu tiên và đổi tên thành `Artist`. Nhấp vào **Browse S3** và chọn tệp từ **`s3://my-workshop-bucket-spotify/staging/spotify_artist_data_2023.csv`**. Sau đó, chọn **Data format** là CSV.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_first_source_artist.png)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_artist_first_source.png)

- Lặp lại các bước tương tự cho 2 bucket S3 khác.
  - `Albums`
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_second_source_albums.png)
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_albums_second_source.png)
  - `Tracks`
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_third_source_tracks.png)
  ![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_tracks_third_source.png)

**3. Cấu hình chuyển đổi dữ liệu**
- Bây giờ để kết hợp **Albums** và **Artist**, nhấp vào biểu tượng ADD, chọn join từ **Transforms** và kết nối các nodes như hình dưới đây.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_join_artist_albums.png)

- Sau khi kết nối các nodes của cả hai bucket với Join Transform. Thêm điều kiện nơi Albums **artist_id =** Artist **id** và đổi tên join thành `Join Albums and Artist`.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_transform_join_albums_artist.png)

- Bây giờ thêm một Join Transform khác để kết hợp bucket **Tracks** và **Join Albums and Artist**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_join_tracks_with_albums_and_artist.png)

- Bây giờ chọn Join và thêm điều kiện Join Albums and Artist **track_id =** Tracks **id** và đổi tên join thành `Join with Tracks`.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_transform_join_with_tracks.png)

- Để loại bỏ các cột không cần thiết, chọn **Drop Fields** từ node Transforms.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_drop_fields.png)

- Chúng ta loại bỏ các cột trùng lặp và các cột giống nhau mà chúng ta không cần. Ở đây **id** (Tracks **id**) là inner join với Artist **id** nên chọn **id**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_drop_fields.png)

**4. Thiết lập đích dữ liệu**
- Bước tiếp theo là thêm đích đến. Nhấp vào bucket Amazon S3 trong phần Targets
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_target.png)

- Đổi tên node `Destination` và thêm vị trí đích S3 **`s3://my-workshop-bucket-spotify/datawarehouse/`** và đảm bảo loại nén là Snappy.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/done_config_target.png)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_s3_url_destination.png)

- Nhập tên như `My Workshop AWS Intern Spotify` vào Name trong tab Job details và chọn IAM Role **`glue_s3_access`** đã tạo trước đó.
- **Type**: Chọn Spark
- **Glue Version**: Chọn phiên bản Glue mới nhất có sẵn.
- **Language**: Chọn Python 3
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/job_details_rename_and_choose_role.png)

- **Requested number of workers**: 4 (có thể nhập số khác)
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_worker_numbers.png) 

- Để mặc định các mục khác và nhấp vào **Save**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/save_job_success.png)

**5. Chạy Glue Job**
-  Xem lại cài đặt job của bạn.
-  Nhấp vào **Run job** trong tab **Runs** để bắt đầu quá trình ETL, chuyển đổi và di chuyển dữ liệu từ lớp staging sang kho dữ liệu.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/choose_run_job.png)

![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/run_job_started.png)

- Chờ vài phút, job đã chạy thành công.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/run_job_success.png)

- Kiểm tra bucket S3 **datawarehouse** để xem các tệp đã được ghi chưa.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.2.config-etl-with-aws-glue/file_written_into_destination.png)

> Nguyễn Văn Hào