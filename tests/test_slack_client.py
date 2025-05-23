# # # # tests/test_slack_client.py

# # # import pytest
# # # from app.slack_client import send_slack_message
# # # from unittest.mock import patch, MagicMock

# # # @pytest.fixture
# # # def fake_env(monkeypatch):
# # #     monkeypatch.setenv("SLACK_BOT_TOKEN", "xoxb-fake-token")
# # #     monkeypatch.setenv("SLACK_CHANNEL_ID", "C12345678")

# # # @patch("app.slack_client.WebClient")
# # # def test_send_slack_message_success(mock_web_client, fake_env):
# # #     # mock_instance = MagicMock()
# # #     mock_web_client.return_value = mock_instance
# # #     mock_instance.chat_postMessage.return_value = {"ts": "1234567890.123456"}

# # #     send_slack_message("xoxb-fake-token", "C12345678")

# # #     mock_instance.chat_postMessage.assert_called_once()
# # # tests/test_slack_client.py

# # # import pytest
# # # from app.slack_client import send_slack_message
# # # from unittest.mock import patch, MagicMock

# # # @pytest.fixture
# # # def fake_env(monkeypatch):
# # #     monkeypatch.setenv("SLACK_BOT_TOKEN", "xoxb-fake-token")
# # #     monkeypatch.setenv("SLACK_CHANNEL_ID", "C12345678")

# # # @patch("app.slack_client.WebClient")
# # # def test_send_slack_message_success(mock_web_client, fake_env):
# # #     # mock_instance = MagicMock()
# # #     mock_web_client.return_value = mock_instance
# # #     mock_instance.chat_postMessage.return_value = {"ts": "1234567890.123456"}

# # #     send_slack_message("xoxb-fake-token", "C12345678")

# # #     mock_instance.chat_postMessage.assert_called_once()
# # # tests/test_slack_client.py

# # # import pytest
# # # from app.slack_client import send_slack_message
# # # from unittest.mock import patch, MagicMock

# # # @pytest.fixture
# # # def fake_env(monkeypatch):
# # #     monkeypatch.setenv("SLACK_BOT_TOKEN", "xoxb-fake-token")
# # #     monkeypatch.setenv("SLACK_CHANNEL_ID", "C12345678")

# # # @patch("app.slack_client.WebClient")
# # # def test_send_slack_message_success(mock_web_client, fake_env):
# # #     # mock_instance = MagicMock()
# # #     mock_web_client.return_value = mock_instance
# # #     mock_instance.chat_postMessage.return_value = {"ts": "1234567890.123456"}

# # #     send_slack_message("xoxb-fake-token", "C12345678")

# # #     mock_instance.chat_postMessage.assert_called_once()
# # # tests/test_slack_client.py
# # import sys
# # import os
# # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # from unittest.mock import patch, MagicMock
# # # tests/test_slack_client.py
# # from app.slack_client import SlackFeedbackBot

# # @patch("app.slack_client.WebClient")
# # def test_SlackFeedbackBot_success(mock_web_client):
# #     mock_instance = MagicMock()
# #     mock_web_client.return_value = mock_instance
# #     mock_instance.chat_postMessage.return_value = {"ts": "1234567890.123456"}

# #     SlackFeedbackBot("fake-token", "C12345678")

# #     mock_instance.chat_postMessage.assert_called_once()



# import sys
# import os
# import pytest
# from unittest.mock import patch, MagicMock

# # Add the parent directory to sys.path so Python can find the `app` module
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from app.slack_client import SlackFeedbackBot

# @patch("app.slack_client.WebClient")
# def test_SlackFeedbackBot_success(mock_web_client):
#     # Setup mock
#     mock_instance = MagicMock()
#     mock_web_client.return_value = mock_instance
#     mock_instance.chat_postMessage.return_value = {"ts": "1234567890.123456"}

#     # Only pass the argument that the class expects
#     slack_token = "fake-token"
#     bot = SlackFeedbackBot(slack_token)  # ✅ Only one argument

#     # If needed, manually set channel_id for testing
#     bot.channel_id = "C12345678"

#     # Call the method
#     bot.send_feedback()

#     # Verify postMessage was called
#     mock_instance.chat_postMessage.assert_called_once_with(
#         channel="C12345678",
#         text="How was your experience today? Please reply with 👍 or 👎"
#     )








import pytest
from unittest.mock import patch, MagicMock
from app.slack_client import SlackFeedbackBot
@patch("app.slack_client.WebClient")
def test_SlackFeedbackBot_success(mock_web_client):
    mock_instance = MagicMock()
    mock_web_client.return_value = mock_instance
    mock_instance.chat_postMessage.return_value = {"ts": "1234567890.123456"}

    slack_token = "fake-token"
    bot = SlackFeedbackBot(slack_token)

    # Define test channel and blocks (can be minimal for test)
    test_channel = "C12345678"
    test_blocks = [
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Test message",
            }
        }
    ]

    # Now call with required arguments
    bot.send_feedback(test_channel, test_blocks)

    mock_instance.chat_postMessage.assert_called_once_with(
        channel=test_channel,
        text="How was your experience today? Please reply with 👍 or 👎",
        blocks=test_blocks
    )
