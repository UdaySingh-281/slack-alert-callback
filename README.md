# Slack Alert Callback for Ansible

## Description
This repository contains a custom **Ansible callback plugin** that sends real-time monitoring feedback to **Slack** during Ansible playbook execution. The callback plugin, `slack_notify.py`, captures key playbook events such as task success, failure, and completion and sends formatted messages to a designated **Slack channel** via a webhook.

## Features
- Sends notifications when a playbook starts and finishes.  
- Reports task successes and failures in real time.  
- Provides a summary of total successful, failed, and skipped tasks.  
- Uses a **Slack Webhook URL** for seamless integration.  

## Installation

Clone this repository:
   ```bash
   git clone https://github.com/your-username/slack-monitoring-callback.git
   cd slack-monitoring-callback
   ```
