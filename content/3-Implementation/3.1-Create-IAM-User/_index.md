---
title : "Create IAM User"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.1. </b> "
---

**1.** In the AWS Management Console, search for `IAM` in the search bar and select the IAM service.
![choose_iam_service](/images/3.implementation/3.1.create-iam-user/choose_iam_service.png)

**2.** In the IAM Dashboard, click on ****Users** from the left-hand menu and then click **Create user** button
![choose_users_iam](/images/3.implementation/3.1.create-iam-user/choose_users_iam.png)

**3.** Enter the following details and click **Next**:
- **Username**: Enter `workshop_user`.
- **Access Type**: Select **Provide user access to the AWS Management Console optional**
- **Console Password**: Choose **Custom password** and set a secure password.
- **Password Reset**: Optionally, require the user to reset the password upon first login.
![fill_user_details](/images/3.implementation/3.1.create-iam-user/fill_user_details.png)

**4.** Assign Permissions
- On the **Set permissions** page, select **Attach policies directly**.
![guide_attach_policy](/images/3.implementation/3.1.create-iam-user/guide_attach_policy.png)

- Search for and select the following policies:
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

- Click **Next** to go to **Review and create** section and then click **Create user**
![review_create_user](/images/3.implementation/3.1.create-iam-user/review_create_user.png)

- In just a few seconds, user **workshop_user** is created successfully.
![create_user_success](/images/3.implementation/3.1.create-iam-user/create_user_success.png)

- And now, you can log in as new user with username and password.
![login_new_user](/images/3.implementation/3.1.create-iam-user/login_new_user.png)
![login_new_user_success](/images/3.implementation/3.1.create-iam-user/login_new_user_success.png)

> Nguyen Van Hao