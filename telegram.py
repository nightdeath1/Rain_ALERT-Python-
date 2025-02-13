import requests
# import time
# import schedule

def get_weather_data():
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "f2079907240e3ba4c24c6bd44dbc762b"
    weather_params = {
        "lat": -33.8688,
        "lon": 151.2093,
        "appid": api_key,
        "cnt": 4,
    }

    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    print(response.json())
    return response.json()

def check_rain(weather_data):
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
            break
    return will_rain

def telegram_bot_sendtext(bot_message):
    bot_token = '7091986185:AAFv41HRw5xNgIR2NMozOhVly30KOfSjpCI'
    bot_chatID = '132561972'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


# if __name__ == "__main__":
#     weather_data = get_weather_data()
#     will_rain = check_rain(weather_data)



def report():
    weather_data = get_weather_data()
    will_rain = check_rain(weather_data)

    if will_rain:
        telegram_bot_sendtext("It's going to rain today. Remember to bring an ☔️")
    else:
        telegram_bot_sendtext("It's not going to rain today. Enjoy your day! ☀️")


report()

# schedule.every().seconds.do(report)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
