import datetime as dt
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv()

now = dt.datetime.now()
day_of_week = now.weekday()

MY_MAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

with open("quotes.txt", "r") as quotes:
    lines = quotes.readlines()
    array = [line.strip() for line in lines]
    today_quote = random.choice(array)

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{today_quote}"
        )
