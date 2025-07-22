---
title: " Tạo EC2 Instace"
date: 2025-07-17
weight: 4
chapter: false
pre: "<b>2.3</b>"
---

## Hướng dẫn tạo EC2 Instace

1. Truy cập vào [AWS Management Consle](https://aws.amazon.com/vi/console/)
- Nhập vào tìm **EC2**
- Sau đó hãy bấm vào chọn **EC2**

<p align="center">
  <img src="/images/2/2.4/image2.4.1.png" width="70%">
</p>

2. Trong giao diện **EC2**
- Chọn **Instaces**
- Chọn tiếp **Launch Instance**

<p align="center">
  <img src="/images/2/2.4/image2.4.2.png" width="70%">
</p>

3. Trong giao diện của **Launch Instance**
- Trong mục **Name** nhập `lambda-lab-instance`
- Chọn **Amazon Linux**
- Chọn **Amazon Linux 2023 kernel-6.12 AMI**

<p align="center">
  <img src="/images/2/2.4/image2.4.3.png" width="70%">
</p>

4. Ở mục **Instance type**
- Chọn **t2.micro**

<p align="center">
  <img src="/images/2/2.4/image2.4.4.png" width="70%">
</p>

5. Tiếp theo ở **Key pair**
- Chọn **Create new key pair**

<p align="center">
  <img src="/images/2/2.4/image2.4.5.png" width="70%">
</p>

6. Trong giao diện **Create key pair**
- **Key pair name** nhập vào `lambda-lab-key`
- chọn **Create key pair**

<p align="center">
  <img src="/images/2/2.4/image2.4.6.png" width="70%">
</p>

7. Trong phần **Network settings**
- chọn **Edit**

<p align="center">
  <img src="/images/2/2.4/image2.4.7.png" width="70%">
</p>

8. Tại **Edit** của **Network settings**
- Chọn **VPC** vừa được tạo 
- Chọn **public-subnet** vừa tạo 
- Ở **Auto-assign public IP** chọn **Enable**
- Tiếp theo **Select existing security group**
- Chọn **Security group** vừa tạo
- Khi đã xong, chọn **Launch instance**

<p align="center">
  <img src="/images/2/2.4/image2.4.8.png" width="70%">
</p>

9. Đã tạo **EC2 instance** thành công

<p align="center">
  <img src="/images/2/2.4/image2.4.9.png" width="70%">
</p>
