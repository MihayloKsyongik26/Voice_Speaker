from speechbrain.pretrained import SpeakerRecognition
import speech_recognition as sr
import os
import const
import time
from command_list import say


""""
def verification():
    dir_path = 'User_Voices'
    files = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            files.append(path)
    #print(files)

    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                                   savedir="pretrained_models/spkrec-ecapa-voxceleb")
    for file in files:
        file_path = dir_path + "/" + file
        print(file_path)
        score, prediction = verification.verify_files(file_path, const.WAVE_OUTPUT_FILENAME)
        status = bool(prediction)
        #print(score)
        if status == True:
            #say("hello" + str(file))
            return status
            break
    return False
"""


def transform():
    r = sr.Recognizer()
    harvard = sr.AudioFile(const.WAVE_OUTPUT_FILENAME)
    with harvard as source:
        try:
            audio = r.record(source)
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            pass