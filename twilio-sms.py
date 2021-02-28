# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('twilio_account_sid')
auth_token = os.environ.get('twilio_auth_token')
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)

participant = client.conversations \
  .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
    .participants \
    .create(
        messaging_binding_address='<+16106806107>',
        messaging_binding_proxy_address='<+17067409285>'
    )