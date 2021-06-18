from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1xxxxxxxxxx", 
    from_="+1xxxxxxxxxx",
    body="Hello from Python! This is Joshua England!"
)

print(client.sid)