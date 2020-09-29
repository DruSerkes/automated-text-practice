import schedule
from twilio.rest import Client
from secrets import auth_token, account_sid, twilio_number, daily_tag, weinberg_number, good_morning_messages
import time
from random import choice


def job():
    client = Client(account_sid, auth_token)
    message = choice(good_morning_messages)
    print(f"Message sent: {message}")
    client.messages.create(
        to=weinberg_number, from_=twilio_number, body=message)
    schedule.clear(daily_tag)


schedule.every().day.at("09:00").do(job).tag(daily_tag)

while True:
    schedule.run_pending()
    time.sleep(5)
    if not schedule.jobs:
        print("No more jobs - ending process")
        break
