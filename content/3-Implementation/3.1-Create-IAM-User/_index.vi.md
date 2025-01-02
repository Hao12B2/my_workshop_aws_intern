---
title : "Tạo người dùng IAM"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.1. </b> "
---
**1.** Trong AWS Management Console, tìm kiếm `IAM` trong thanh tìm kiếm và chọn dịch vụ IAM.
![choose_iam_service](/images/3.implementation/3.1.create-iam-user/choose_iam_service.png)

**2.** Trong IAM Dashboard, nhấp vào **Users** từ menu bên trái và sau đó nhấp vào nút **Create user**.
![choose_users_iam](/images/3.implementation/3.1.create-iam-user/choose_users_iam.png)

**3.** Nhập các chi tiết sau và nhấp **Next**:
- **Username**: Nhập `workshop_user`.
- **Access Type**: Chọn **Provide user access to the AWS Management Console optional**
- **Console Password**: Chọn **Custom password** và đặt mật khẩu an toàn.
- **Password Reset**: Tùy chọn, yêu cầu người dùng đặt lại mật khẩu khi đăng nhập lần đầu.
![fill_user_details](/images/3.implementation/3.1.create-iam-user/fill_user_details.png)

**4.** Gán các quyền
- Trong trang **Set permissions**, Chọn **Attach policies directly**.
![guide_attach_policy](/images/3.implementation/3.1.create-iam-user/guide_attach_policy.png)

- Tìm và chọn các chính sách sau:
    - **AmazonS3FullAccess**
    - **AWSGlueConsoleFullAccess**
    - **AmazonAthenaFullAccess**
    - **AmazonQuickSightAccess**
    - **AWSQuickSightDescribeRDS**
    - **IAMFullAccess**

![choose_attach_policy_s3](/images/3.implementation/3.1.create-iam-user/choose_attach_policy_s3.png)
![choose_attach_policy_glue](/images/3.implementation/3.1.create-iam-user/choose_attach_policy_glue.png)
![choose_attach_policy_athena](/images/3.implementation/3.1.create-iam-user/choose_attach_policy_athena.png)
![choose_attach_policy_quicksight_athena](/images/3.implementation/3.1.create-iam-user/choose_attach_policy_quicksight_athena.png)
![choose_attach_policy_quicksight_rds](/images/3.implementation/3.1.create-iam-user/choose_attach_policy_quicksight_rds.png)
![choose_iam_fullaccess](/images/3.implementation/3.1.create-iam-user/choose_iam_fullaccess.png)

- Nhấn **Next** để di chuyển đến phần **Review and create** và sau đó chọn **Create user**
![review_create_user](/images/3.implementation/3.1.create-iam-user/review_create_user.png)

- Chỉ trong vài giây, người dùng **workshop_user** đã được tạo thành công.
![create_user_success](/images/3.implementation/3.1.create-iam-user/create_user_success.png)

- Và bây giờ, bạn có thể đăng nhập với tư cách người dùng mới bằng tên người dùng và mật khẩu.
![login_new_user](/images/3.implementation/3.1.create-iam-user/login_new_user.png)
![login_new_user_success](/images/3.implementation/3.1.create-iam-user/login_new_user_success.png)

> Nguyễn Văn Hào

