# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# conversation = client.conversations \
#                      .conversations \
#                      .create(friendly_name='My First Conversation')

# conversation.sid = CH2ceade900b8946e1892babf48e194d2d

conversation = client.conversations \
                     .conversations('CH2ceade900b8946e1892babf48e194d2d') \
                     .fetch()

print(conversation.chat_service_sid)

# chat service ID = IS3a14601e02ca48d581a251a5c5cb57ba

# twilio token:chat --identity testPineapple --chat-service-sid IS3a14601e02ca48d581a251a5c5cb57ba --profile project-danger
