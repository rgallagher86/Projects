from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.environ['API_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['API_SLACK_TOKEN']

print(SLACK_APP_TOKEN)
print(SLACK_BOT_TOKEN)

app = App(token=SLACK_BOT_TOKEN)

# print(str(token))

#Slackbottoken = ()