import schedule
from twilio.rest import Client
from secrets import auth_token, account_sid, twilio_number, kang_number, tg_message, daily_tag
import time

def job():
    client = Client(account_sid, auth_token)
    message = tg_message
    client.messages.create(to=kang_number, from_=twilio_number, body=message)
    schedule.clear(daily_tag)


schedule.every().day.at("9:01").do(job).tag(daily_tag)

while True:
    schedule.run_pending()
    time.sleep(1)
    if not schedule.jobs:
        break