import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
location = "Columbia,Maryland,USA"
lat = 39.217522
lon = -76.868729

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18448956019',
        body="It's going to rain today. Bring an umbrela",
        to='+13478153081'
    )
    print(message.status)