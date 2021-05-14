from flask import Flask



from SETTINGS import *
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter
# from slack_sdk.errors import SlackApiError

client = WebClient(
    token = SLACK_TOKEN
)

class GodBot:
    channel = '#random'

    def __init__(self, channel = None) -> None:
        if channel:
            self.channel = channel

    def get_message_payload(self):
        return "God is watching you all"
    
    def postMessage(self, message: str):
        return client.chat_postMessage(
            channel = self.channel,
            text = message
        )
    

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(SLACK_TOKEN, "/slack/events", app)

@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})
    text = event.get("text")

    if "god" in text.lower():

        God = GodBot('#private-channel-w-god')
        God.postMessage(
            God.get_message_payload()
        )

# app.run(
#     host = 'localhost',
#     port = 3000
# )

God = GodBot('#private-channel-w-god')
God.postMessage(
    God.get_message_payload()
)
