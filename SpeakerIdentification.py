import os
import pickle
import warnings
import numpy as np
from sklearn import preprocessing
from scipy.io.wavfile import read
import python_speech_features as mfcc
import time

warnings.filterwarnings("ignore")


def calculate_delta(array):
    rows, cols = array.shape
    print(rows)
    print(cols)
    deltas = np.zeros((rows, 20))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i - j < 0:
                first = 0
            else:
                first = i - j
            if i + j > rows - 1:
                second = rows - 1
            else:
                second = i + j
            index.append((second, first))
            j += 1
        deltas[i] = (array[index[0][0]] - array[index[0][1]] + (2 * (array[index[1][0]] - array[index[1][1]]))) / 10
    return deltas


def extract_features(audio, rate):
    mfcc_feature = mfcc.mfcc(audio, rate, 0.025, 0.01, 20, nfft=1200, appendEnergy=True)
    mfcc_feature = preprocessing.scale(mfcc_feature)
    print(mfcc_feature)
    delta = calculate_delta(mfcc_feature)
    combined = np.hstack((mfcc_feature, delta))
    return combined


def test_model():
    source = "testing_set/"
    modelpath = "trained_models/"
    test_file = "testing_set_addition.txt"
    file_paths = open(test_file, 'r')

    gmm_files = [os.path.join(modelpath,fname) for fname in
                  os.listdir(modelpath) if fname.endswith('.gmm')]

    #Load the Gaussian gender Models
    models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
    speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname
                  in gmm_files]

    # Read the test directory and get the list of test audio files
    for path in file_paths:

        path = path.strip()
        print(path)
        sr,audio = read(source + path)
        vector   = extract_features(audio,sr)

        log_likelihood = np.zeros(len(models))

        for i in range(len(models)):
            gmm = models[i]  #checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()

        print(log_likelihood)
        winner = np.argmax(log_likelihood)
        result = []
        print(log_likelihood[winner])
        if log_likelihood[winner] > -25:
            name = get_name(speakers[winner])
            #print(name)
            result.append(True)
            result.append(name)
            return result
        else:
            result.append(False)
            result.append("You are not in the database")
            return result


def get_name(text):
    text = text[15:]
    text = text[:text.find('.')]
    text_end = ''
    for i in text:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            text_end = text_end + i
    return text_end


