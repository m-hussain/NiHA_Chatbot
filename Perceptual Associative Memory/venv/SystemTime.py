import time as t

def getSystemTime():
    timeNow = t.asctime(t.localtime(t.time()))
    return timeNow

