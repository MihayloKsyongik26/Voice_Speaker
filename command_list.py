import datetime
from gtts import gTTS
import os
import requests
import wikipediaapi


def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    say(current_time)


def say(text):
    tts = gTTS(text)
    tts.save('out.wav')
    os.system("mpg123 " + "out.wav")


def get_weather():
    s_city = "Lviv, UA"
    city_id = 0
    appid = "d972ec87c4d3b913ea5d14a1a6a9ac34"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'uk', 'APPID': appid})
        data = res.json()
        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
    except Exception as e:
        print("Exception (weather):", e)
        pass

    if data['main']['temp'] < 0:
        say(data['weather'][0]['description'] + str(round(data['main']['temp'])) + str("degrees below zero"))

    else:
        say(data['weather'][0]['description'] + str(round(data['main']['temp'])) + str("degrees above zero"))


