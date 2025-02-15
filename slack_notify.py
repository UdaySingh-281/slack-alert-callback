from ansible.plugins.callback import CallbackBase
import requests
import json

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = "notification"
    CALLBACK_NAME = "slack_notify"
    CALLBACK_NEEDS_WHITELIST = False

    def send_slack_message(self, message):
        payload = {"text": message}
        headers = {"Content-Type": "application/json"}
        requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    def v2_playbook_on_start(self, playbook):
        self.send_slack_message(f"Playbook `{playbook._file_name}` started.")

    def v2_runner_on_ok(self, result):
        task_name = result.task_name or "Unnamed Task"
        self.send_slack_message(f"Task `{task_name}` succeeded on `{result._host.get_name()}`.")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        task_name = result.task_name or "Unnamed Task"
        self.send_slack_message(f"Task `{task_name}` failed on `{result._host.get_name()}`.")

    def v2_playbook_on_stats(self, stats):
        summary = {host: stats.summarize(host) for host in stats.processed}

        total_ok = sum(host_stats['ok'] for host_stats in summary.values())
        total_failures = sum(host_stats['failures'] for host_stats in summary.values())
        total_skipped = sum(host_stats['skipped'] for host_stats in summary.values())

        message = f"Playbook finished. Success: {total_ok}, Failed: {total_failures}, Skipped: {total_skipped}."
        print(f"Slack message: {message}")
        self.send_slack_message(message)

