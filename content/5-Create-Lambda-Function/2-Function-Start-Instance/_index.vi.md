---
title: " Function to Start Instances"
date: 2025-07-17
weight: 2
chapter: false
pre: "<b>5.2</b>"
---

## Tạo Lambda Function thực hiện chức năng Start instances

1. Truy cập vào [AWS Management Consle](https://aws.amazon.com/vi/console/)
- Nhập vào tìm **Lambda**
- Sau đó hãy bấm vào chọn **Lambda**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.1.png" | relURL }}" width="100%">
</p>

2. Tại **Functions** trong **Lambda**
- Chọn **Create function**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.2.png" | relURL }}" width="100%">
</p>

3. Trong giao diện **Create function**
- Chọn **Author from scratch**
- Ở **Function name** đặt `dc-common-lambda-auto-start`
- Trong phần **Runtime** chọn **Python 3.13**
- Còn lại **Architecture** hãy chọn **x86_64**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.3.1.png" | relURL }}" width="100%">
</p>

4. Tiếp tục ở giao diện **Create function**
- Chọn **Change default execution role**
- Ở **Execution role** chọn **Use an existing role**
- Ở **Existing role** chọn **IAM role** vừa tạo 
- Hoàn thành **Create function**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.4.png" | relURL }}" width="100%">
</p>

5. Sau khi tạo thành công function 
- Chọn **Configuration**
- Tại thanh bên trái, chọn **Environment variables**
- Chọn **Edit**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.5.png" | relURL }}" width="100%">
</p>

6. Tại giao diện **Edit environment variables**
- Ở **Key** nhập `environment_auto`
- Ở **Value** nhập `true`
- Chọn **Save** để hoàn tất

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.6.png" | relURL }}" width="100%">
</p>

7. Sau khi tạo thành công ta đến với **code**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.7.png" | relURL }}" width="100%">
</p>

8. Trong giao diện **Code source**
- Import source code: Cần phải thay đổi **webhook_url** để nhận thông báo đến Slack.

```python
import boto3
import os
import json
import urllib3
from datetime import datetime, timedelta, timezone

ec2_resource = boto3.resource('ec2')
http = urllib3.PoolManager()
webhook_url = "https://hooks.slack.com/services/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"

def lambda_handler(event, context):
    # Lấy biến môi trường và action từ input
    environment_auto = os.environ.get('environment_auto')
    action = event.get("action", "").lower()

    print(f"[DEBUG] environment_auto = {environment_auto}")
    print(f"[DEBUG] action = {action}")

    if not environment_auto or action not in ["start", "stop"]:
        return {
            "statusCode": 400,
            "body": "Missing environment_auto or invalid action"
        }

    # Lọc EC2 theo tag
    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'tag:environment_auto', 'Values': [environment_auto]}]
    )

    instance_list = list(instances)
    print(f"[DEBUG] Instances found: {instance_list}")

    if not instance_list:
        return {
            "statusCode": 404,
            "body": "No EC2 instances found"
        }

    action_result = []
    for instance in instance_list:
        if action == "start":
            result = instance.start()
        else:
            result = instance.stop()
        action_result.append(result)

    sent_slack(action_result, action)

    return {
        "statusCode": 200,
        "body": f"{action.capitalize()}ed {len(instance_list)} EC2 instance(s)"
    }

def sent_slack(action_result, action):
    instance_ids = []
    key = "StartingInstances" if action == "start" else "StoppingInstances"

    for result in action_result:
        if key in result and len(result[key]) > 0:
            for i in result[key]:
                instance_ids.append(i["InstanceId"])

    if instance_ids:
        # Lấy thời gian hiện tại theo UTC+7 (giờ VN)
        now = datetime.now(timezone.utc) + timedelta(hours=7)
        current_time = now.strftime("%H:%M:%S %d-%m-%Y")

        msg = f"{'✅ Starting' if action == 'start' else '⛔ Stopping'} Instances ID:\n{instance_ids}\n🕒 Time: {current_time} (Asia/Ho_Chi_Minh)"
        data = {"text": msg}
        r = http.request("POST",
                         webhook_url,
                         body=json.dumps(data),
                         headers={"Content-Type": "application/json"})
        print(f"[DEBUG] Slack response status: {r.status}")
    else:
        print(f"[INFO] No instances {action}ed")
```

- Sau khi đã thêm đường dẫn ta nhấn **Deploy**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.8.png" | relURL }}" width="100%">
</p>

9. Truy cập vào **Amazon EventBridge**
- Chọn **Rules**
- Chọn vào **Create rule**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.9.png" | relURL }}" width="100%">
</p>

10. Ở phần **Define rule detail** trong giao diện **create rule**
- Ở **Name** nhập `dc-common-lambda-auto-start`
- Ở **Description** nhập `dc-common-lambda-auto-start`
- Chọn **Schedule**
- Chọn **Countinue to create rule**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.10.png" | relURL }}" width="100%">
</p>

11. Ở phần **Schedule pattern**
- Ở **Occurrence** chọn **Recurring schedule**
- Ở **Time zone** chọn **(UTC+07:00) Asia/Saigon** "Bạn muốn **EventBridge Rule** bật lúc 9 giờ mỗi ngày từ thứ Hai đến thứ Sáu (trừ thứ 7 và Chủ nhật) theo giờ Việt Nam (ICT, UTC+7). Trên **AWS EventBridge**, cron dùng UTC, nên phải trừ 7 tiếng"
- Ở **Schedule type** chọn **Cron-based schedule**
- Trong phần **Cron expression**
    | Trường       | Giá trị | Ý nghĩa                        |
    | ------------ | ------- | ------------------------------ |
    | Minutes      | `0`     | Vào phút 00                    |
    | Hours        | `2`     | 2 giờ UTC (tức 9 giờ VN)       |
    | Day of month | `?`     | Bỏ qua ngày trong tháng        |
    | Month        | `*`     | Mỗi tháng                      |
    | Day of week  | `2-6`   | Từ thứ 2 đến thứ 6             |
    | Year         | `*`     | Mỗi năm                        |

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.11.png" | relURL }}" width="100%">
</p>

- Sau đó hãy bấm **Next**

12. Ở phần **Select target(s)**
- Chọn **AWS service**
- Ở **Select a target** chọn **Lambda function**
- Ở **Function** chọn **dc-common-lamda-auto-stop**
- Ở **Execution role** tích vào **Use existing role** rồi chọn **dc-common-lamda-role**
- Bấm **Next**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.12.png" | relURL }}" width="100%">
</p>

13. Kiểm tra lại và hoàn thành, chọn **Create rule**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.13.png" | relURL }}" width="100%">
</p>

14. Đã tạo thành công rule cho start insatance

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.14.png" | relURL }}" width="100%">
</p>