from recording_voice import recording
from multiprocessing.pool import ThreadPool
import time
from SpeakerIdentification import test_model
from user_verification import transform
from command_list import *


def main():
    while True:
        recording()
        t1 = time.time()
        pool = ThreadPool(processes=2)
        thread1 = pool.apply_async(test_model, ())
        thread2 = pool.apply_async(transform, ())

        user_status = thread1.get()
        command_text = thread2.get()
        print(user_status)
        print(command_text)
        if user_status[0] == True:
            if "hello" in command_text or "hi" in command_text:
                say("Hello" + user_status[1])
            elif "time" in command_text:
                get_time()
            elif "weather" in command_text:
                get_weather()
        else:
            say(user_status[1])
        t2 = time.time()
        print(t2-t1)


if __name__ == '__main__':
    main()
