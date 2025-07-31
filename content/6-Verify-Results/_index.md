---
title: " CHECK RESULTS"
date: 2025-07-17
weight: 6
chapter: false
pre: "<b>6.</b>"
---

### Check Stop Results

1. Check the **EC2** interface and the **instance** status

<p align="center">
  <img src="/images/6/image6.1.png" width="100%">
</p>

2. Go to the **Lambda Function** and execute the **stop instance** function
- Click **Test**
- Select **Create new event**
- In the **Event name** field, enter `instance-stop`
- In the **Event JSON** section, enter:
```
{
  "action": "stop"
}
```

- Click **Save**
- Click **Test**

<p align="center">
  <img src="/images/6/image6.2.png" width="100%">
</p>

3. A successful result is returned

<p align="center">
  <img src="/images/6/image6.3.png" width="100%">
</p>

4. Check your **Slack** workspace to confirm that a **Stopped instance** notification has been received

<p align="center">
  <img src="/images/6/image6.4.png" width="100%">
</p>

5. Recheck the **instance** status in the **EC2** interface

<p align="center">
  <img src="/images/6/image6.5.png" width="100%">
</p>

### Check Start Results

6. Similarly, go to the **Lambda Function** and execute the **start instance** function
- Click **Test**
- Select **Create new event**
- In the **Event name** field, enter `instance-start`
- In the **Event JSON** section, enter:
```
{
  "action": "start"
}
```

- Click **Save**
- Click **Test**

<p align="center">
  <img src="/images/6/image6.6.png" width="100%">
</p>

7. A successful result is returned

<p align="center">
  <img src="/images/6/image6.7.png" width="100%">
</p>

8. Check your **Slack** workspace to confirm that a **Started instance** notification has been received

<p align="center">
  <img src="/images/6/image6.8.png" width="100%">
</p>

9. Recheck the **instance** status in the **EC2** interface

<p align="center">
  <img src="/images/6/image6.9.png" width="100%">
</p>
