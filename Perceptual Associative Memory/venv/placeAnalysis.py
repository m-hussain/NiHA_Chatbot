from urllib.request import urlopen
import json

## To get system IP
# import ipgetter
# IP = ipgetter.myip()
# print(IP)

# Module to check If internet is connected to get IPLocation
import socket
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is a DNS listening
    host = socket.gethostbyname(hostname)
    #print(host)
    # connect to the host -- tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    #print(s)
    return True
  except:
      #print("Sorry Couldn't connect")
     pass
  return False


def getGPSLocation():

    # Get IP Location
    if is_connected("ipinfo.io"):
        url = 'http://ipinfo.io/json'
        response = urlopen(url).read()
        #print(type(response))
        response = '{' + str(response)[7:-2].replace('\\n', '') + '}'
        #print(response)
        #print(type(response))
        parsed_json = json.loads(response)
        #print(type(parsed_json))
        # print("city : ", parsed_json['city'])
        city = parsed_json['region']
        location = parsed_json['loc']
        return city, location
    else:
        return "null"



## Getting Location From Sentence
from neTagger import *
def getLocation(Sentence):
        #ORGANIZATION
        #LOCATION
        #GEO-POLITICAL ENTITY
        place = []
        s = str(Sentence)
        #print(s)
        # s = "I live in Lahore and works at Google."
        t = tagNE(s)
        print("NE Tagged : ", t)
        for chunk in t:
            if hasattr(chunk, 'label'):
                if chunk.label() == 'GPE':
                    place.append(''.join(c[0] for c in chunk))
        return place



#Testing Interface
if __name__ == '__main__':
    p = getGPSLocation()
    print("Place : ", p)

    while(True):
        s = input("Sentence : ")
        p = getLocation(s)
        print("Place : ", p)


