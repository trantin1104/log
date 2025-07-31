---
title: " Function to Stop Instances"
date: 2025-07-17
weight: 1
chapter: false
pre: "<b>5.1</b>"
---

## Create a Lambda Function to Stop Instances

1. Go to [AWS Management Console](https://aws.amazon.com/console/)
- Search for **Lambda**
- Then click to select **Lambda**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.1.png" | relURL }}" width="100%">
</p>

2. In the **Functions** section of **Lambda**
- Select **Create function**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.2.png" | relURL }}" width="100%">
</p>

3. In the **Create function** interface
- Select **Author from scratch**
- In **Function name**, enter `dc-common-lambda-auto-stop`
- In **Runtime**, select **Python 3.13**
- For **Architecture**, select **x86_64**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.3.png" | relURL }}" width="100%">
</p>

4. Continue in the **Create function** interface
- Select **Change default execution role**
- In **Execution role**, choose **Use an existing role**
- In **Existing role**, select the **IAM role** you created earlier
- Finish by clicking **Create function**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.4.png" | relURL }}" width="100%">
</p>

5. After successfully creating the function 
- Go to **Configuration**
- On the left sidebar, select **Environment variables**
- Click **Edit**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.5.png" | relURL }}" width="100%">
</p>

6. In the **Edit environment variables** interface
- Click **Add environment variable**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.6.png" | relURL }}" width="100%">
</p>

7. In the **Edit environment variables** interface
- In **Key**, enter `environment_auto`
- In **Value**, enter `true`
- Click **Save** to complete

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.7.png" | relURL }}" width="100%">
</p>

8. After creating successfully, move to the **code** section

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.8.png" | relURL }}" width="100%">
</p>

9. In the **Code source** interface
- Import the source code: You must change **webhook_url** to receive notifications in Slack.

```python
import boto3
import os
import json
import urllib3
from datetime import datetime, timedelta, timezone

ec2_resource = boto3.resource('ec2')
http = urllib3.PoolManager()
webhook_url = "https://hooks.slack.com/services/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"

ACTION_VERB = {
    "start": "Started",
    "stop": "Stopped"
}

def lambda_handler(event, context):
    environment_auto = os.environ.get('environment_auto')
    action = event.get('action', '').lower()

    print(f"[DEBUG] environment_auto = {environment_auto}")
    print(f"[DEBUG] action = {action}")

    if not environment_auto:
        return {
            "statusCode": 400,
            "body": "Missing environment_auto"
        }

    if action not in ['start', 'stop']:
        return {
            "statusCode": 400,
            "body": "Invalid action. Must be 'start' or 'stop'."
        }

    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'tag:environment_auto', 'Values': [environment_auto]}]
    )

    instance_list = list(instances)
    print(f"[DEBUG] Instances found: {instance_list}")

    if not instance_list:
        print(f"[INFO] No EC2 instances found for action '{action}'")
        return {
            "statusCode": 404,
            "body": "No EC2 instances found"
        }

    action_results = []
    for instance in instance_list:
        if action == 'start':
            result = instance.start()
        else:
            result = instance.stop()
        action_results.append(result)

    sent_slack(action, action_results)

    return {
        "statusCode": 200,
        "body": f"{ACTION_VERB[action]} {len(instance_list)} EC2 instance(s)"
    }

def sent_slack(action, action_results):
    instance_ids = []
    key = "StartingInstances" if action == "start" else "StoppingInstances"

    for result in action_results:
        if key in result and len(result[key]) > 0:
            for i in result[key]:
                instance_ids.append(i["InstanceId"])

    if instance_ids:
        now = datetime.now(timezone.utc) + timedelta(hours=7)
        current_time = now.strftime("%H:%M:%S %d-%m-%Y")
        instance_list_str = "\n• " + "\n• ".join(instance_ids)
        msg = (
            f"{'✅ Started' if action == 'start' else '⛔ Stopped'} EC2 Instances:\n"
            f"{instance_list_str}\n"
            f"🕒 Time: {current_time} (Asia/Ho_Chi_Minh)"
        )
        data = {"text": msg}
        r = http.request("POST",
                         webhook_url,
                         body=json.dumps(data),
                         headers={"Content-Type": "application/json"})
        print(f"[DEBUG] Slack response status: {r.status}")
    else:
        print(f"[INFO] No instances {ACTION_VERB[action]}")

```

- After adding the webhook URL, click **Deploy**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.9.png" | relURL }}" width="100%">
</p>

10. Go to [AWS Management Console](https://aws.amazon.com/console/)  
- Search for **Amazon EventBridge**  
- Then click to select **Amazon EventBridge**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.10.png" | relURL }}" width="100%">
</p>

11. In the **Rules** interface  
- Select **Create rule**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.11.png" | relURL }}" width="100%">
</p>

12. In the **Define rule detail** section of the **Create rule** interface  
- In **Name**, enter `dc-common-lambda-auto-stop`  
- In **Description**, enter `dc-common-lambda-auto-stop`  
- Select **Schedule**  
- Click **Continue to create rule**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.12.png" | relURL }}" width="100%">
</p>

13. In the **Schedule pattern** section  
- In **Occurrence**, select **Recurring schedule**  
- In **Time zone**, select **(UTC+07:00) Asia/Saigon**  
  > You want the **EventBridge Rule** to stop instances at 17:00 every day from Monday to Friday (excluding Saturday and Sunday) in Vietnam time (ICT, UTC+7).  
  > On **AWS EventBridge**, cron uses UTC, so you must subtract 7 hours.  
- In **Schedule type**, select **Cron-based schedule**  
- Enter the following **Cron expression**:

| Field        | Value  | Meaning                          |
| ------------ | ------ | -------------------------------- |
| Minutes      | `0`    | At minute 00                     |
| Hours        | `10`   | 10:00 UTC (17:00 Vietnam)        |
| Day of month | `?`    | Ignore day of month              |
| Month        | `*`    | Every month                      |
| Day of week  | `2-6`  | Monday through Friday            |
| Year         | `*`    | Every year                       |

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.13.1.png" | relURL }}" width="100%">
</p>

- Then click **Next**

14. In the **Select target(s)** section  
- Select **AWS service**  
- In **Select a target**, choose **Lambda function**  
- In **Function**, select **dc-common-lambda-auto-stop**  
- In **Execution role**, check **Use existing role** and select **dc-common-lambda-role**  
- Click **Next**

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.14.png" | relURL }}" width="100%">
</p>

15. Review everything and click **Create rule** to complete

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.15.png" | relURL }}" width="100%">
</p>

16. The rule for stopping instances has been successfully created

<p align="center">
  <img src="{{ "/images/5/5.1/image5.1.16.png" | relURL }}" width="100%">
</p>
