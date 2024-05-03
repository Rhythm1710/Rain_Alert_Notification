import requests
from twilio.rest import Client

api_key = ""

twilio_account_sid = ""
twilio_auth_token = ""
verify_sid = ""
twilio_phone_number = ""

twilio_client = Client(twilio_account_sid, twilio_auth_token)

parametres = {
    "lat": 0,
    "lon": 0,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "lang": "en"
}

response = requests.get(
    url="https://api.openweathermap.org/data/3.0/onecall", params=parametres)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]  # slice operator

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = twilio_client.messages.create(
        from_=twilio_phone_number,
        body="It's going to rain today.Remember to bring an ☔",
        to="your_number"
    )
    print(message.status)


# import requests
# api_key = "808bda379c3f358d866ed5fbc998ae10"

# parametres = {
#     "lat": 30.733315,
#     "lon": 76.779419,
#     "appid": api_key,
#     "exclude":"current,minutely,daily",
#     "lang":"en"
# }

# response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall",params=parametres)
# response.raise_for_status()
# weather_data = response.json()["hourly"]
# # print(weather_data[0]["weather"])

# for i in  range(12):
#     code = int(weather_data[i]["weather"][0])
#     if code<700:
#         print("Bring Umbrella")
