---
title: " THÊM TRIGGER CHO LAMBDA FUNCTION"
date: 2025-07-17
weight: 7
chapter: false
pre: "<b>7.</b>"
---

### Thêm Trigger cho Lambda Function 
- Sau khi tạo xong Lambda function, chúng ta cần thêm trigger để tự động kích hoạt function theo lịch định sẵn.

1. Vào chức năng **Lambda Function** thực hiện **Add trigger** trên `dc-common-lambda-auto-start`

<p align="center">
  <img src="/log/images/7/image7.1.png" width="70%">
</p>

2. Ở trang **Add trigger**
- Chọn **EventBridge (CloudWatch Events)** 
- Ở mục **Rule** chọn **Existing rules**
- Ở mục **Existing rules** chọn **dc-common-lambda-auto-start** 
- Nhấn **Add**

<p align="center">
  <img src="/log/images/7/image7.2.png" width="70%">
</p>

3. Đã thêm thành công

<p align="center">
  <img src="/log/images/7/image7.3.png" width="70%">
</p>

4. Tiếp tục vào chức năng **Lambda Function** thực hiện **Add trigger** trên `dc-common-lambda-auto-stop`

<p align="center">
  <img src="/log/images/7/image7.4.png" width="70%">
</p>

5. Ở trang **Add trigger**
- Chọn **EventBridge (CloudWatch Events)** 
- Ở mục **Rule** chọn **Existing rules**
- Ở mục **Existing rules** chọn **dc-common-lambda-auto-stop** 
- Nhấn **Add**

<p align="center">
  <img src="/log/images/7/image7.5.png" width="70%">
</p>

6. Đã thêm thành công

<p align="center">
  <img src="/log/images/7/image7.6.png" width="70%">
</p>

7. Kiểm tra lại kết quả trên **Slack**
- Đã bật lúc 7 giờ sáng

<p align="center">
  <img src="/log/images/7/image7.7.1png" width="70%">
</p>

- Đã tắt lúc 5 giờ chiều

<p align="center">
  <img src="/log/images/7/image7.7.2png" width="70%">
</p>