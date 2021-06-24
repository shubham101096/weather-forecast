import requests
import pprint
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

KEY = os.environ.get("OWM_API_KEY")

parameters = {"lat": 8.3,
              "lon": 76.57,
              "exclude": "current,minutely,daily",
              "appid": KEY}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
pprint.pprint(response.json())

next_48 = response.json()["hourly"]

weather_id = []

for i in range(12):
    weather_id.append(next_48[i]["weather"][0]["id"])


print(weather_id)

for i in weather_id:
    if i < 700:
        print("bring an umbrella")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Take an umbrella!!",
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('MY_NUMBER')
        )
        print(message.sid)
        print(message.status)
        break