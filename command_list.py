import datetime
from gtts import gTTS
import os
import requests

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    say(current_time)

def say(text):
    tts = gTTS(text)
    tts.save('out.wav')
    os.system("mpg123"+"out.wav")

