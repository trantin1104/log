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
  <img src="/images/5/5.2/image5.2.1.png" width="100%">
</p>

2. Tại **Functions** trong **Lambda**
- Chọn **Create function**

<p align="center">
  <img src="/images/5/5.2/image5.2.2.png" width="100%">
</p>

3. Trong giao diện **Create function**
- Chọn **Author from scratch**
- Ở **Function name** đặt `dc-common-lambda-auto-start`
- Trong phần **Runtime** chọn **Python 3.13**
- Còn lại **Architecture** hãy chọn **x86_64**

<p align="center">
  <img src="/images/5/5.2/image5.2.3.1.png" width="100%">
</p>

4. Tiếp tục ở giao diện **Create function**
- Chọn **Change default execution role**
- Ở **Execution role** chọn **Use an existing role**
- Ở **Existing role** chọn **IAM role** vừa tạo 
- Hoàn thành **Create function**

<p align="center">
  <img src="/images/5/5.2/image5.2.4.png" width="100%">
</p>

5. Sau khi tạo thành công function 
- Chọn **Configuration**
- Tại thanh bên trái, chọn **Environment variables**
- Chọn **Edit**

<p align="center">
  <img src="/images/5/5.2/image5.2.5.png" width="100%">
</p>

6. Tại giao diện **Edit environment variables**
- Ở **Key** nhập `environment_auto`
- Ở **Value** nhập `true`
- Chọn **Save** để hoàn tất

<p align="center">
  <img src="/images/5/5.2/image5.2.6.png" width="100%">
</p>

7. Sau khi tạo thành công ta đến với **code**

<p align="center">
  <img src="/images/5/5.2/image5.2.7.png" width="100%">
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
  <img src="/images/5/5.2/image5.2.8.png" width="100%">
</p>