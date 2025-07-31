---
title: "Function to Start Instances"
date: 2025-07-17
weight: 2
chapter: false
pre: "<b>5.2</b>"
---

## Create a Lambda Function to Start Instances

1. Go to [AWS Management Console](https://aws.amazon.com/console/)  
   - Search for **Lambda**  
   - Then click to select **Lambda**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.1.png" | relURL }}" width="100%">
</p>

2. In **Lambda**, under **Functions**  
   - Click **Create function**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.2.png" | relURL }}" width="100%">
</p>

3. In the **Create function** interface  
   - Select **Author from scratch**  
   - Set **Function name** to `dc-common-lambda-auto-start`  
   - In **Runtime**, choose **Python 3.13**  
   - For **Architecture**, select **x86_64**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.3.1.png" | relURL }}" width="100%">
</p>

4. Continue in the **Create function** interface  
   - Click **Change default execution role**  
   - In **Execution role**, select **Use an existing role**  
   - In **Existing role**, choose the **IAM role** you just created  
   - Complete by clicking **Create function**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.4.png" | relURL }}" width="100%">
</p>

5. After successfully creating the function  
   - Select **Configuration**  
   - In the left sidebar, choose **Environment variables**  
   - Click **Edit**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.5.png" | relURL }}" width="100%">
</p>

6. In the **Edit environment variables** interface  
   - Enter `environment_auto` for **Key**  
   - Enter `true` for **Value**  
   - Click **Save** to complete

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.6.png" | relURL }}" width="100%">
</p>

7. After successfully creating the function, proceed to the **code** section

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.7.png" | relURL }}" width="100%">
</p>

8. In the **Code source** interface  
- Import the source code: You need to change the **webhook_url** to receive notifications on Slack.

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

    environment_auto = os.environ.get('environment_auto')
    action = event.get("action", "").lower()

    print(f"[DEBUG] environment_auto = {environment_auto}")
    print(f"[DEBUG] action = {action}")

    if not environment_auto or action not in ["start", "stop"]:
        return {
            "statusCode": 400,
            "body": "Missing environment_auto or invalid action"
        }


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

- After adding the webhook URL, click **Deploy**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.8.png" | relURL }}" width="100%">
</p>

9. Go to **Amazon EventBridge**  
- Select **Rules**  
- Click **Create rule**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.9.png" | relURL }}" width="100%">
</p>

10. In the **Define rule detail** section of the **Create rule** interface  
- For **Name**, enter `dc-common-lambda-auto-start`  
- For **Description**, enter `dc-common-lambda-auto-start`  
- Choose **Schedule**  
- Click **Continue to create rule**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.10.png" | relURL }}" width="100%">
</p>

11. In the **Schedule pattern** section  
- For **Occurrence**, choose **Recurring schedule**  
- For **Time zone**, select **(UTC+07:00) Asia/Saigon**  
  *You want the **EventBridge Rule** to trigger at 9:00 AM every Monday to Friday (excluding Saturday and Sunday) in Vietnam Time (ICT, UTC+7). On **AWS EventBridge**, cron uses UTC, so subtract 7 hours.*  
- For **Schedule type**, select **Cron-based schedule**  
- In the **Cron expression**, configure as follows:

| Field        | Value  | Description                          |
| ------------ | ------ | ------------------------------------ |
| Minutes      | `0`    | At minute 00                         |
| Hours        | `2`    | 2:00 UTC (9:00 AM Vietnam time)      |
| Day of month | `?`    | Ignore the day of the month          |
| Month        | `*`    | Every month                          |
| Day of week  | `2-6`  | Monday through Friday                |
| Year         | `*`    | Every year                           |

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.11.png" | relURL }}" width="100%">
</p>

- Then click **Next**

12. In the **Select target(s)** section  
- Select **AWS service**  
- For **Select a target**, choose **Lambda function**  
- For **Function**, select **dc-common-lambda-auto-stop**  
- For **Execution role**, check **Use existing role** and select **dc-common-lambda-role**  
- Click **Next**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.12.png" | relURL }}" width="100%">
</p>

13. Review and complete by clicking **Create rule**

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.13.png" | relURL }}" width="100%">
</p>

14. The rule for starting instances has been successfully created

<p align="center">
  <img src="{{ "/images/5/5.2/image5.2.14.png" | relURL }}" width="100%">
</p>
