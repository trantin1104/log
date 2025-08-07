---
title: " TỐI ƯU HÓA CHI PHÍ VỚI LAMBDA"
date: 2025-07-17
weight: 1
chapter: false
---

# TỐI ƯU HÓA CHI PHÍ VỚI LAMBDA

#### Tổng quan

Trong môi trường sử dụng AWS, Amazon EC2 là một trong những dịch vụ phổ biến và cũng là nguồn chi phí lớn nếu không được quản lý hiệu quả. Workshop **“Optimize EC2 Cost with Lambda”** được thiết kế nhằm giúp bạn tự động hóa việc quản lý chi phí EC2 bằng cách sử dụng AWS Lambda để tắt các EC2 instance khi không cần thiết – ví dụ ngoài giờ hành chính.


<p align="center">
  <img src="/log/images/index/image.png" width="70%">
</p>

Thông qua workshop này, bạn sẽ học được cách:

- Gắn thẻ (tag) cho các EC2 instance để phân biệt instance cần tối ưu.
- Tạo IAM Role để Lambda có thể kiểm soát EC2.
- Viết hàm Lambda bật/tắt EC2 tự động theo lịch trình.
- Kiểm tra kết quả và dọn dẹp tài nguyên.

#### Mục tiêu

Giúp người học:

- Nắm được cách tích hợp Lambda với EC2.
- Tối ưu hóa chi phí sử dụng EC2.
- Tăng tính tự động hóa trong vận hành hạ tầng cloud.

#### Điều kiện cần

Để thực hiện workshop này, bạn cần có:

- Tài khoản AWS có quyền quản trị (AdministratorAccess).
- Kiến thức cơ bản về EC2, IAM và Lambda.
- Trình duyệt web và kết nối Internet ổn định.

#### Nội dung chính
1. [Giới thiệu](1-introduction/)
1. [Các bước chuẩn bị](2-setup-requirements/)
2. [Tạo tag cho instance](3-tag-for-instances/)
3. [Tạo IAM role cho Lambda](4-create-iam-role-for-lambda/)
4. [Tạo Lambda Function](5-create-lambda-function/)
5. [Kiểm tra kết quả](6-verify-results/)
7. [Thêm Trigger cho Lambda Function](7-add-trigger-to-lambda-function/)
8. [Dọn dẹp tài nguyên](7-cleanup-resources/)
