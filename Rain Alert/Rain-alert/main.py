from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

MY_API_KEY = os.getenv("MY_API_KEY")
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
from_phone = os.getenv("TWILIO_FROM")
to_phone = os.getenv("TWILIO_TO")

rain = 0

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

for i in range(4):
    id_weather = weather_data["list"][i]["weather"][0]["id"]
    if id_weather < 700:
        rain += 1

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring the umbrella ☔",
        from_=from_phone,
        to=to_phone
    )
    print(message.status)
