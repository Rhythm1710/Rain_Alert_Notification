import requests
from twilio.rest import Client

api_key = "808bda379c3f358d866ed5fbc998ae10"

twilio_account_sid = "AC6a916389b78ca018a9adb995df46d0b1"
twilio_auth_token = "a1b991364599966ff76d02100421a9de"
verify_sid = "VAca0ddccc627c2790286225993d571109"
twilio_phone_number = "+15734961771"

twilio_client = Client(twilio_account_sid, twilio_auth_token)

parametres = {
    "lat": 30.733315,
    "lon": 76.779419,
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
        to="+919992394539"
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
