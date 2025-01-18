---
title : "Tạo IAM Role cho ETL Job"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.3.1. </b> "
---
- Truy cập vào AWS Management Console và mở IAM console, sau đó chọn **Roles** bên thanh điều hướng và chọn **Create role**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/choose_roles.png)

- Chọn **AWS service** tại mục trusted entity type, chọn **Glue** từ danh sách các dịch vụ và nhấn **Next**
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_1.png)

- Trên trang **Add permissions**, chọn chính sách `AmazonS3FullAccess` và nhấn **Next**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_2.png)

- Đặt tên cho role là `glue_s3_access` , kiểm tra lại chính sách và chọn **Create role**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_3_name.png)

![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_3_click_create_role.png)

- Role được tạo thành công.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_success.png)
> Nguyễn Văn Hào