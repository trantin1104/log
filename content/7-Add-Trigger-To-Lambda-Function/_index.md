---
title: " ADD TRIGGER TO LAMBDA FUNCTION"
date: 2025-07-17
weight: 7
chapter: false
pre: "<b>7.</b>"
---

### Add Trigger to Lambda Function

After creating the Lambda function, we need to add triggers so it can run automatically on a scheduled basis.

1. Go to the **Lambda Function** section and click **Add trigger** for `dc-common-lambda-auto-start`.

<p align="center">
  <img src="/log/images/7/image7.1.png" width="70%">
</p>

2. In the **Add trigger** screen:
- Choose **EventBridge (CloudWatch Events)**  
- In the **Rule** section, select **Existing rules**  
- Under **Existing rules**, choose `dc-common-lambda-auto-start`  
- Click **Add**

<p align="center">
  <img src="/log/images/7/image7.2.png" width="70%">
</p>

3. The trigger has been successfully added.

<p align="center">
  <img src="/log/images/7/image7.3.png" width="70%">
</p>

4. Repeat the steps for `dc-common-lambda-auto-stop`:
- Go to the **Lambda Function** section and click **Add trigger** for `dc-common-lambda-auto-stop`.

<p align="center">
  <img src="/log/images/7/image7.4.png" width="70%">
</p>

5. In the **Add trigger** screen:
- Choose **EventBridge (CloudWatch Events)**  
- In the **Rule** section, select **Existing rules**  
- Under **Existing rules**, choose `dc-common-lambda-auto-stop`  
- Click **Add**

<p align="center">
  <img src="/log/images/7/image7.5.png" width="70%">
</p>

6. The trigger has been successfully added.

<p align="center">
  <img src="/log/images/7/image7.6.png" width="70%">
</p>

7. Finally, verify the result on **Slack**:
- Auto-start executed at 7:00 AM:

<p align="center">
  <img src="/log/images/7/image7.7.png" width="70%">
</p>

- Auto-stop executed at 5:00 PM:

<p align="center">
  <img src="/log/images/7/image7.8.png" width="70%">
</p>
