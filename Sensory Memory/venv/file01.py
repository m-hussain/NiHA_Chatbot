import threading
import time

import SpeechToText
import Publisher

def publisher():
    Publisher.__main__()
    # print(threading.currentThread().getName(), 'Starting')
    # #time.sleep(1)
    # print(threading.currentThread().getName(), 'Exiting')

def mainThread():
    SpeechToText.__main__()
    # print(threading.currentThread().getName(), 'Starting')
    # #time.sleep()
    # print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=publisher)
w = threading.Thread(name='worker', target=mainThread)
#w2 = threading.Thread(target=worker) # use default name

w.start()
#w2.start()
t.start()