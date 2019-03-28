#from googleTranslate import translateThis
#from TTS_pyttsx3 import speakThis

from Publisher import SignalTransferHandler

import speech_recognition as sr


Signal = SignalTransferHandler()

def initializer():
    #print("in init")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    return microphone, recognizer

def adjustAmbient(microphone, recognizer):
    #print("in adjustAmbient module")
    with microphone as source: recognizer.adjust_for_ambient_noise(source)

def getAudio(microphone, recognizer):
    #print("in getAudio module")
    with microphone as source: audio = recognizer.listen(source)
    return audio

def standardizeText(text):
    #print("in standardizeText module")
    standardText = ""
    # we need some special handling here to correctly print unicode characters to standard output
    if str is bytes:  # this version of Python uses bytes for strings (Python 2)
        #print("Interpreter is Python2")
        standardText = text.encode("utf-8")
        return standardText
    else:  # this version of Python uses unicode for strings (Python 3+)
        #print("Interpreter is Python3")
        standardText = text
        return standardText

def getTextFromSpeech(audio = None, recognizer = None):
    #print("in getTextFromSpeech module")
    recognizedText = ""
    try:
        if audio is None and recognizer is None:
            microphone, recognizer1 = initializer()
            adjustAmbient(microphone, recognizer1)
            audio1 = getAudio(microphone, recognizer1)
            recognizedText = recognizer1.recognize_google(audio1)  # Online #configured
            recognizedText = standardizeText(recognizedText)

        elif audio is not None and recognizer is not None:
            # recognize speech using Google Speech Recognition
            recognizedText = recognizer.recognize_google(audio)  # Online #configured
            # recognizedText = recognizer.recognize_sphinx(audio) #Offline #configured

            ## unconfigured engines
            # recognizedText = recognizer.recognize_google_cloud(audio, credentials_json="?")
            # recognizedText = recognizer.recognize_bing(audio, key="?")
            # recognizedText = recognizer.recognize_houndify(audio, client_id="?", client_key="?")
            # recognizedText = recognizer.recognize_ibm(audio, username="?", password="?")
            # recognizedText = recognizer.recognize_wit(audio, key="?")
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

    return recognizedText



def __main__():
    try:
        microphone, recognizer = initializer()

        print("A moment of silence, please...")
        adjustAmbient(microphone, recognizer)

        print("Set minimum energy threshold to {}".format(recognizer.energy_threshold))

        while True:
            print("Say something!")
            audio = getAudio(microphone, recognizer)
            print("Got it! Now to recognize it...")
            recognizedText = getTextFromSpeech(audio, recognizer)
            recognizedText = standardizeText(recognizedText)
            Signal.PublishData(recognizedText)
            print("You said : ", recognizedText)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    __main__()