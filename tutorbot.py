from time import sleep
from slackclient import SlackClient
import os

message = """
Hi there! Looks like you're trying to write a Slack bot. Want some help?

You can find an example echobot here: https://github.com/jackreichelt/slackbot-tutorial
You can also find some notes on how to write a Slack bot in that same repository.

You can also find an example of adding slash commands and notes here: https://github.com/rowena-s/easy-peasy-slash-command-app
There's also notes on that as well.

Finally, you can find my source code here: https://github.com/jackreichelt/tutorbot

🍕🍕🍕🍕🍕
"""

token = os.environ.get('TOKEN', None) # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
if sc.rtm_connect() == True:
  print('Connected.')
  while True:
    response = sc.rtm_read()
    for part in response:
      if part['type'] == 'message':
        if '<@U1C5S08F4>' in part['text']:
          sc.api_call("chat.postMessage", channel=part['channel'], text=message, username='tutorbot', icon_emoji=':mortar_board:')
    sleep(1)
else:
  print('Connection Failed, invalid token?')