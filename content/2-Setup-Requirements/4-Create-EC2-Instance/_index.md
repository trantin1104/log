---
title: " Create EC2 Instance"
date: 2025-07-17
weight: 4
chapter: false
pre: "<b>2.4</b>"
---

## Guide to Creating an EC2 Instance

1. Go to the [AWS Management Console](https://aws.amazon.com/console/)
- Search for **EC2**
- Then click on **EC2**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.1.png" | absURL }}" width="100%">
</p>

2. In the **EC2** interface:
- Select **Instances**
- Then click on **Launch Instance**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.2.png" | absURL }}" width="100%">
</p>

3. In the **Launch Instance** interface:
- In the **Name** field, enter `lambda-lab-instance`
- Choose **Amazon Linux**
- Select **Amazon Linux 2023 kernel-6.12 AMI**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.3.png" | absURL }}" width="100%">
</p>

4. Under **Instance type**:
- Choose **t2.micro**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.4.png" | absURL }}" width="100%">
</p>

5. Next, under **Key pair**:
- Select **Create new key pair**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.5.png" | absURL }}" width="100%">
</p>

6. In the **Create key pair** screen:
- Enter `lambda-lab-key` for **Key pair name**
- Click **Create key pair**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.6.png" | absURL }}" width="100%">
</p>

7. In the **Network settings** section:
- Click **Edit**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.7.png" | absURL }}" width="100%">
</p>

8. In the **Edit** section of **Network settings**:
- Select the VPC you created earlier
- Select the public subnet you created
- Under **Auto-assign public IP**, choose **Enable**
- Then choose **Select existing security group**
- Select the Security Group you created
- Once completed, click **Launch instance**

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.8.png" | absURL }}" width="100%">
</p>

9. The **EC2 instance** has been successfully created

<p align="center">
  <img src="{{ "/images/2/2.4/image2.4.9.png" | absURL }}" width="100%">
</p>

> **Note:** After creating the EC2 instance, wait a few minutes for the instance to enter the "running" state and for internal services to fully start. Only then should you SSH into it or access any hosted web server (if applicable).
