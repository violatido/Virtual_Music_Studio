import os
from twilio.rest import Client


account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
                    body="You have unread messages in VMS. Log on to read and reply!",
                    to=os.environ["MY_PHONE"],
                    from_=os.environ["TWILIO_PHONE"]
                )