from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class SlackFeedbackBot:
    def __init__(self, token: str):
        self.client = WebClient(token=token)

    def send_feedback(self, channel: str, blocks: List[Dict]) -> None:
        """
        Sends a formatted message to a Slack channel.

        :param channel: Slack channel ID (e.g., 'C12345678')
        :param blocks: List of message blocks
        """
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text="Customer Satisfaction Survey Feedback",
                blocks=blocks
            )
            logger.info(f"✅ Message sent successfully. Timestamp: {response['ts']}")
        except SlackApiError as e:
            error_code = e.response["error"]
            logger.error(f"❌ Slack API Error: {error_code}")

            if error_code == "channel_not_found":
                logger.error("Check the channel ID. Make sure the bot is invited to the channel.")
            elif error_code == "not_in_channel":
                logger.error("Bot is not a member of the channel. Invite the bot to the channel.")
            elif error_code == "missing_scope":
                logger.error("Missing required permission scope. Check your app's OAuth scopes.")
            elif error_code == "invalid_auth":
                logger.error("Invalid token. Double-check the bot token.")
            else:
                logger.error(f"Unhandled Slack API error: {error_code}")
        except Exception as ex:
            logger.exception(f"⚠️ Unexpected error: {ex}")
