# 📊 Log Utilities

A lightweight toolset for logging, monitoring, and analyzing events in a structured way.

---

## 🧾 Overview

This repository provides scripts and utilities that help developers:

- Record and manage log entries
- Filter and parse logs easily
- Generate structured reports
- Optionally notify Slack on specific events

It is ideal for tracking actions, debugging, and creating activity summaries.

---

## 🚀 Features

- ✅ Generate standardized logs (JSON or plain text)  
- ✅ Filter logs by **date**, **severity**, or **tags**  
- ✅ Aggregate and analyze logs for reporting  
- ✅ Optional Slack integration for live notifications  

---

## 🎬 Getting Started

### 1. Prerequisites

- Python **3.x** (or Node.js if using JavaScript utilities)
- `pip` installed for Python dependencies
- *(Optional)* Slack Incoming Webhook URL if you want live notifications

### 2. Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/trantin1104/log.git
cd log
```

Install Python dependencies if needed:

```bash
pip install -r requirements.txt
```

### 3. Usage Examples

#### **Parse Logs**

```bash
python log_parser.py logs/*.json
```

#### **Filter Logs**

```bash
python log_filter.py --from 2025-07-01 --to 2025-07-17 --severity ERROR
```

#### **Generate Report**

```bash
python log_parser.py --output report.txt
```

---

## 📥 Slack Notifications (Optional)

If you want to send log alerts to Slack:

1. Create a Slack Incoming Webhook ([Guide](https://api.slack.com/messaging/webhooks))  
2. Add your Webhook URL to the script  
3. Run the script and check Slack for notifications

Example notification:

```
✅ Started EC2 Instance(s):
• i-017582b100bbdee11
🕒 Time: 14:25:07 31-07-2025 (Asia/Ho_Chi_Minh)
```

---

## 🧠 Common Tasks

| Task                             | Command Example                                          |
|----------------------------------|----------------------------------------------------------|
| Filter logs by date range        | `python log_filter.py --from 2025-07-01 --to 2025-07-17` |
| Filter logs by severity          | `python log_filter.py --severity ERROR`                  |
| Output structured report         | `python log_parser.py --output report.txt`               |
| Send Slack notifications         | Configure `webhook_url` and run script                   |

---

## 🧭 Contributing

Contributions are welcome! 🎉  
Feel free to **fork** the repository and submit **pull requests** with enhancements.

---

## ⚖️ License

This project is **open-source** and distributed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
