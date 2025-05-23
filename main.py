import os
import logging
from dotenv import load_dotenv
from app.slack_client import SlackFeedbackBot

# Load environment variables from .env
load_dotenv()

token = os.getenv("SLACK_BOT_TOKEN")
channel = os.getenv("SLACK_CHANNEL_ID")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_feedback_blocks():
    """
    Returns Slack block kit structure for customer survey feedback.
    """
    return [
        {"type": "header", "text": {"type": "plain_text", "text": "📝 Customer Survey Feedback", "emoji": True}},
        {"type": "divider"},
        {"type": "section", "fields": [
            {"type": "mrkdwn", "text": "*Survey Question 1:*"},
            {"type": "plain_text", "text": "On a scale of 1 to 5, how satisfied were you with the resolution provided by LINDA today?", "emoji": True},
            {"type": "mrkdwn", "text": "*Response:*"},
            {"type": "plain_text", "text": "5", "emoji": True},
        ]},
        {"type": "divider"},
        {"type": "section", "fields": [
            {"type": "mrkdwn", "text": "*Survey Question 2:*"},
            {"type": "plain_text", "text": "On a scale of 1 to 5, how satisfied are you with the customer service you received from LINDA today?", "emoji": True},
            {"type": "mrkdwn", "text": "*Response:*"},
            {"type": "plain_text", "text": "5", "emoji": True},
        ]},
        {"type": "divider"},
        {"type": "section", "fields": [
            {"type": "mrkdwn", "text": "*Customer Feedback:*"},
            {"type": "plain_text", "text": "nothing", "emoji": True},
        ]},
        {"type": "divider"},
        {"type": "section", "fields": [
            {"type": "mrkdwn", "text": "*AI Response:*"},
            {"type": "plain_text", "text": "Thank you for your feedback. We're glad your experience met your expectations.", "emoji": True},
        ]}
    ]

if __name__ == "__main__":
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    slack_channel = os.getenv("SLACK_CHANNEL_ID")

    if not slack_token or not slack_channel:
        logger.error("Environment variables SLACK_BOT_TOKEN and SLACK_CHANNEL_ID must be set.")
        exit(1)

    bot = SlackFeedbackBot(token=slack_token)
    bot.send_feedback(channel=slack_channel, blocks=build_feedback_blocks())
