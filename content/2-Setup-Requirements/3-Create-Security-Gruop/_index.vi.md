---
title: " Tạo Security Group"
date: 2025-07-17
weight: 3
chapter: false
pre: "<b>2.3</b>"
---

## Hướng dẫn tạo Security Gruop

1. Trong giao diện **VPC** 
- Chọn vào **Security Group**
- Sau đó chọn **Create security gruop**

<p align="center">
  <img src="{{ "/images/2/2.3/image2.3.1.png" | relURL }}" width="100%">
</p>

2. Trong **Create security group**
- Nhập `lambda-lab` vào Security gruop name
- Nhập `security group for lambda lab` vào Description
- Trong ô **VPC** chọn **VPC** vừa mới tạo

<p align="center">
  <img src="{{ "/images/2/2.3/image2.3.2.png" | relURL }}" width="100%">
</p>

3. Tiếp tục đến phần **Inbound rules**
- Chọn vào **Add rule**

<p align="center">
  <img src="{{ "/images/2/2.3/image2.3.3.png" | relURL }}" width="100%">
</p>

4. Cấu hình **Inbound rules** và **Outbound rules**

<p align="center">
  <img src="{{ "/images/2/2.3/image2.3.4.png" | relURL }}" width="100%">
</p>

5. Bấm vào **Create security group**

<p align="center">
  <img src="{{ "/images/2/2.3/image2.3.5.png" | relURL }}" width="100%">
</p>