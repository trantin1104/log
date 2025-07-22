---
title: " CREATE IAM ROLE FOR LAMBDA"
date: 2025-07-17
weight: 4
chapter: false
pre: "<b>4.</b>"
---

## Create IAM Role for Lambda

1. Go to the [AWS Management Console](https://aws.amazon.com/console/)
- Search for **IAM**
- Then click on **IAM**

<p align="center">
  <img src="/images/4/image4.1.png" width="100%">
</p>

2. In the **IAM** interface:
- Click on **Roles**
- Then click **Create role** in the **Roles** interface

<p align="center">
  <img src="/images/4/image4.2.png" width="100%">
</p>

3. In the **Select trusted entity** screen:
- Under **Trusted entity type**, select **AWS service**
- For **Use case**, select **Lambda**
- Then click **Next**

<p align="center">
  <img src="/images/4/image4.3.png" width="100%">
</p>

4. Next, in the **Add permissions** screen:
- Search for `CloudWatchFullAccess`
- Select **CloudWatchFullAccess**

<p align="center">
  <img src="/images/4/image4.4.png" width="100%">
</p>

5. Continue the same steps:
- Search for `CloudWatchFullAccess`
- Select **CloudWatchFullAccess**
- Then click **Next**

<p align="center">
  <img src="/images/4/image4.5.png" width="100%">
</p>

6. In the **Name, review, and create** screen:
- Enter `dc-common-lambda-role` for **Role name**

<p align="center">
  <img src="/images/4/image4.6.png" width="100%">
</p>

7. Scroll down to **Step 2: Add permissions**:
- Check the **Policy name** in the **Permissions policy summary**
- After verifying, click **Create role**

<p align="center">
  <img src="/images/4/image4.7.png" width="100%">
</p>

8. The role for the **Lambda Function** has been successfully created

<p align="center">
  <img src="/images/4/image4.8.png" width="100%">
</p>
