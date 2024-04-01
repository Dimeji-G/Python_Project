# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='ACfaf3f24f7d15a9657a4445b064b36b57'
auth_token = '6c4c52add0ecefa4578f40abf6251f4b'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello Dimzy!, Have a great day',
                              from_='+15076056324',
                              to='+2348078595543'
                          )

print(message.sid)
