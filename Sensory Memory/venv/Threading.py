import threading
import time

import TextFromInput
import Publisher_Server

from SpeechToText import initializer, getAudio, adjustAmbient, getTextFromSpeech, standardizeText

textCounter = 0

def textFromSpeech():
    microphone, recognizer = initializer()
    adjustAmbient(microphone, recognizer)

    global textCounter

    textCounter += 1
    print("Say something!")
    audio = getAudio(microphone, recognizer)
    print("Got it! Now to recognize it...")
    recognizedText = getTextFromSpeech(audio, recognizer)
    recognizedText = standardizeText(recognizedText)
    #client.publishSensoryData(recognizedText)
    print("You said : ", recognizedText)
    #makeGraph(recognizedText, textCounter)
    return  recognizedText


def textFromInput():
    TextFromInput.getTextFromInput()
    # print(threading.currentThread().getName(), 'Starting')
    # #time.sleep()
    # print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='speech', target=textFromSpeech())
w = threading.Thread(name='input', target=textFromInput())
#w2 = threading.Thread(target=worker) # use default name

w.start()
#w2.start()
t.start()