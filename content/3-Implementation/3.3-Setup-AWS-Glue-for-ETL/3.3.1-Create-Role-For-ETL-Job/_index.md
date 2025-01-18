---
title : "Create IAM Role for ETL Job"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3.3.1. </b> "
---
- Access the AWS Management Console and open the IAM console, then select **Roles** from the navigation pane and choose **Create role**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/choose_roles.png)

- Select **AWS service** as the trusted entity type, choose **Glue** from the list of services, and click **Next**
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_1.png)

- On the **Add permissions** page, select the `AmazonS3FullAccess` policy and click **Next**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_2.png)

- Name the role `glue_s3_access`, review the policy, and choose **Create role**.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_3_name.png)

![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_step_3_click_create_role.png)

- The role is created successfully.
![](/images/3.implementation/3.3.setup-aws-glue-for-etl/3.3.1.create-role-for-etl-job/create_role_success.png)

> Nguyen Van Hao