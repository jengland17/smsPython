from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1xxxxxxxxxx", # recieves message
    from_="+1xxxxxxxxxx", # number that sends message
    body="Hello from Python! This is Joshua England!" # message that will be sent
)

print(client.sid)