from user_verification import *
from recording_voice import recording
from command_list import *


def main():
    recording()
    text = transform()
    if verification() == True:
        if "time" in text:
            get_time()
        elif "weather" in text:
            get_weather()

    else:
        say("You aren't in database")


if __name__ == '__main__':
    main()
