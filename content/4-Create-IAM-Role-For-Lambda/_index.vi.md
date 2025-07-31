---
title: " TẠO IAM ROLE CHO LAMBDA"
date: 2025-07-17
weight: 4
chapter: false
pre: "<b>4.</b>"
---
## Tạo IAM Role cho Lambda

1. Truy cập vào [AWS Management Consle](https://aws.amazon.com/vi/console/)
- Nhập vào tìm **IAM**
- Sau đó hãy bấm vào chọn **IAM**

<p align="center">
  <img src="{{ "/images/4/image4.1.png" | relURL }}" width="100%">
</p>

2. Tại giao diện **IAM**
- Nhấn vào **Roles**
- Ở tại giao diện **Roles** nhấn vào **Create role**

<p align="center">
  <img src="{{ "/images/4/image4.2.png" | relURL }}" width="100%">
</p>

3. Ở giao diện **Select trusted entity** 
- Tại **Trusted entity type** chọn **AWS service**
- Tại **Use case** chọn **Lambda**
- Chọn **Next**

<p align="center">
  <img src="{{ "/images/4/image4.3.png" | relURL }}" width="100%">
</p>

4. Tiếp theo, ở giao diện **Add permissions**
- Tìm `CloudWatchFullAccess`
- Chọn **CloudWatchFullAccess**

<p align="center">
  <img src="{{ "/images/4/image4.4.png" | relURL }}" width="100%">
</p>

5. Tiếp tục thực hiện theo bước 4 
- Tìm `CloudWatchFullAccess`
- Chọn **CloudWatchFullAccess**
- - Cuối cùng, hãy chọn **Next**

<p align="center">
  <img src="{{ "/images/4/image4.5.png" | relURL }}" width="100%">
</p>

6. Tại giao diện tiếp theo **Name, review, and create**
- Nhập `dc-common-lambda-role` cho **Role name**

<p align="center">
  <img src="{{ "/images/4/image4.6.png" | relURL }}" width="100%">
</p>

7. Nhìn phía dưới sẽ thấy **Step 2: Add permissions**
- Kiểm tra **Policy name** tại **Permissions policy summary**
- Sau khi đã kiểm tra xong thì chọn **Create role**

<p align="center">
  <img src="{{ "/images/4/image4.7.png" | relURL }}" width="100%">
</p>

8. Role cho **Lamda Function** đã được tạo thành công 

<p align="center">
  <img src="{{ "/images/4/image4.8.png" | relURL }}" width="100%">
</p>