# This is an extremely simple project that uses the twilio API
# to notify family members that dinner's ready

import os
from twilio.rest import Client

# The sid and token are removed for security
account_sid = os.environ['sid']
auth_token = os.environ['token']
client = Client(account_sid, auth_token)

# The numbers are removed for privacy
numbers_to_message = ['+9999999990', '+9999999991', '+9999999992']

for number in numbers_to_message:
    message = client.messages \
        .create(
        # Inspired by the automate workshop
         body='Come down, dinner''s ready!',
         
         # The number is removed for privacy
         from_='+9999999999',
         to=numbers
     )
     print(message.sid)
