from twilio.rest import Client
from secrets import twilio_number, auth_token, account_sid, joey_lavarco_number, paul_sabala_number, rocket_reminder_message

client = Client(account_sid, auth_token)
message = rocket_reminder_message

client.messages.create(to=paul_sabala_number, from_=twilio_number, body=message)
print(f"Message sent to {paul_sabala_number}")

client.messages.create(to=joey_lavarco_number, from_=twilio_number, body=message)
print(f"Message sent to {joey_lavarco_number}")
 