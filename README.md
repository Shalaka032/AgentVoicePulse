## 📝 Slack Feedback Bot

A Python-based bot that sends automated, formatted customer feedback messages to a specified Slack channel using the Slack Web API and a daily scheduler (APScheduler).

---

### 📦 Features

* Sends daily customer satisfaction feedback messages to Slack
* Uses Slack [blocks](https://api.slack.com/block-kit) for rich message formatting
* Powered by [`slack-sdk`](https://pypi.org/project/slack-sdk/) and [`APScheduler`](https://pypi.org/project/APScheduler/)
* Environment variables are securely managed using `.env`
* Unit tested with `pytest`
* CI/CD ready with GitHub Actions

---

###  Project Structure

```
slack_feedback_bot/
├── app/
│   └── slack_client.py        # Slack messaging logic
├── tests/
│   └── test_slack_client.py   # Unit tests
├── .env                       # Environment secrets (not committed)
├── .gitignore                 # Ignore sensitive and build files
├── main.py                    # Entry point with scheduler
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
└── .github/
    └── workflows/
        └── ci.yml             # GitHub Actions for CI
```


#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/slack-feedback-bot.git
cd slack-feedback-bot
```

#### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On Mac/Linux
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set up environment variables

Create a `.env` file in the project root:

```env
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_CHANNEL_ID=C1234567890
```


###  Run the Bot

```bash
python main.py
```

It will send a Slack message once and then continue based on the scheduled interval (daily at a set time).

---

###  How It Works

* `main.py` loads your Slack token and channel ID from `.env`
* Schedules a task using APScheduler to send a message once per day
* `app/slack_client.py` constructs and sends a rich message to Slack

---

###  Running Tests

```bash
pytest
```

> Tests use monkeypatching to safely simulate API calls without actually hitting Slack.

---

### 🛠 GitHub Actions CI (Optional)

The included `.github/workflows/ci.yml` runs tests automatically on pushes and pull requests to `main`.

---

###  Example Slack Message

![Slack Message Screenshot](https://via.placeholder.com/600x250?text=Slack+Survey+Bot+Example)
*(Replace with actual screenshot if needed)*

---

###  Dependencies

* `slack-sdk`
* `apscheduler`
* `python-dotenv`
* `pytest` (for testing)

---

###  Security

* Keep your Slack token secret
* Add `.env` to `.gitignore`
* Use GitHub Secrets if deploying with GitHub Actions

---
