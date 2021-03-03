# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
# messaging_sid = os.environ.get('messaging_service_sid') ????
client = Client(account_sid, auth_token)

message = client.messages.create(
                    body="You have unread messages in VMS. Log on to read and reply!",
                    to=os.environ["MY_PHONE"],
                    from_=os.environ["TWILIO_PHONE"]
                )

# export TWILIO_ACCOUNT_SID=AC7de31e0e824bcdab8af440bd1a54effb
# TWILIO_AUTH_TOKEN=aadd9e6fe1b0a00767bd20793b229cab