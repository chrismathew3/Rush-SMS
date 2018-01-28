# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC42ca1e203f4053ff6d2843565c97d6c1"
auth_token = "249ffe8e6750827b1de6ff2f35d61e73"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+18568737908",
    from_="+18623731378",
    body="Hello there!"
)