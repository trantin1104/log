---
title: " KIỂM TRA KẾT QUẢ"
date: 2025-07-17
weight: 6
chapter: false
pre: "<b>6.</b>"
---
### Kiểm tra kết quả Stop

1. Kiểm tra giao diện **EC2** và trạng thái **instance**

<p align="center">
  <img src="/images/6/image6.1.png" width="100%">
</p>

2. Vào chức năng **Lambda Function** và thực hiện chức năng **stop instance**
- Chọn **Test**
- Chọn **Create new event**
- Ở dòng **Event name** nhập `instance-stop`
- Ở phần **Event JSON** nhập vào 
```
{
  "action": "stop"
}
```

- Chọn **Save**
- Chọn **Test**

<p align="center">
  <img src="/images/6/image6.2.png" width="100%">
</p>

3. Trả về kết quả thành công

<p align="center">
  <img src="/images/6/image6.3.png" width="100%">
</p>

4. Kiểm tra trong workspace của **Slack** đã nhận được thông báo **Stopped instance**

<p align="center">
  <img src="/images/6/image6.4.png" width="100%">
</p>

5. Kiểm tra lại trang thái **instance** ở giao diện **EC2**

<p align="center">
  <img src="/images/6/image6.5.png" width="100%">
</p>

### Kiểm tra kết quả Start

6. Tương tự, truy cập vào **Lambda Function** và thực hiện chức năng **start instance**
- Chọn **Test**
- Chọn **Create new event**
- Ở dòng **Event name** nhập `instance-start`
- Ở phần **Event JSON** nhập vào 
```
{
  "action": "start"
}
```

- Chọn **Save**
- Chọn **Test**

<p align="center">
  <img src="/images/6/image6.6.png" width="100%">
</p>

7. Trả về kết quả thành công

<p align="center">
  <img src="/images/6/image6.7.png" width="100%">
</p>

8. Kiểm tra trong workspace của **Slack** đã nhận được thông báo **Started instance**

<p align="center">
  <img src="/images/6/image6.8.png" width="100%">
</p>

9. Kiểm tra lại trang thái **instance** ở giao diện **EC2**

<p align="center">
  <img src="/images/6/image6.9.png" width="100%">
</p>