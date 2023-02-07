from recording_voice import recording
from multiprocessing.pool import ThreadPool
from SpeakerIdentification import test_model
from user_verification import transform
from command_list import *
import warnings


warnings.filterwarnings("ignore")


def main():
    while True:
        recording()
        pool = ThreadPool(processes=2)
        thread1 = pool.apply_async(test_model, ())
        thread2 = pool.apply_async(transform, ())

        user_status = thread1.get()
        command_text = thread2.get()
        print(user_status[1])
        print(command_text)

        if "rob" in command_text:
            say("I am listening you")
            while True:
                pool = ThreadPool(processes=2)
                recording()
                thread1 = pool.apply_async(test_model, ())
                thread2 = pool.apply_async(transform, ())

                user_status = thread1.get()
                command_text = thread2.get()
                if user_status[0] == True:
                    print(command_text)
                    if "name" in command_text:
                        say("Your name is" + user_status[1])
                    elif "time" in command_text:
                        get_time()
                    elif "weather" in command_text:
                        get_weather()
                    elif command_text == "Error":
                        print("You don`t say")
                    elif "bye" or "buy" in command_text:
                        say("Goodbye")
                        break
        else:
            continue


if __name__ == '__main__':
    main()