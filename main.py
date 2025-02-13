import requests
from twilio.rest import Client

#https://console.twilio.com/ - GYZ59WKQKJ56MCRXJKM1VM3H
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f2079907240e3ba4c24c6bd44dbc762b"
account_sid = 'ACd883fec549e1e00d7aadfef2634703b0'
auth_token = '35b76fe9025b16eab47ca9afc90be5cc'

weather_params = {
    "lat": -27.563829,
    "lon": 151.953964,
    "appid": api_key,
    "cnt": 4,
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
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+12512764417',
        to='+614522711xx'
    )
    #put your number#

    print(message.status)
