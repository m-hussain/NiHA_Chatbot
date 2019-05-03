import threading
import time

import Subcriber_Server
#import PerceptualMemoryModule

def sensorySubscriber():
    Subcriber_Server.__main__()
    # print(threading.currentThread().getName(), 'Starting')
    # #time.sleep(1)
    # print(threading.currentThread().getName(), 'Exiting')

# def mainThread():
#     PerceptualMemoryModule.__main__()
#     # print(threading.currentThread().getName(), 'Starting')
#     # #time.sleep()
#     # print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=sensorySubscriber)
# w = threading.Thread(name='worker', target=mainThread)
#w2 = threading.Thread(target=worker) # use default name

# w.start()
#w2.start()
t.start()