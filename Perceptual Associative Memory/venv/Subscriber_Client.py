import sys
sys.path.append("../../../NiHA_Chatbot/")

from thrift_code.GenPy.SignalTransfer_NameSpace import SignalTransfer_Service
# from ...thrift_code.GenPy.SignalTransfer_NameSpace import SignalTransfer_Service

import _pickle as pickle

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import json
configurations = open("../../Configurations/config.json",'r').read()
configurations = json.loads(configurations)
SensorySocket = configurations["SensorySocket"]

try:
    transport = TSocket.TSocket(SensorySocket["ip"], SensorySocket["port"])
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = SignalTransfer_Service.Client(protocol)
    transport.open()

    lastText = ''
    while True:
        bytesData = client.getBinaryStream()

        SensorySignal = pickle.loads(bytesData)

        text = SensorySignal['text']

        if text == '' or lastText:
            continue

        print("SensorySignal : ", SensorySignal)

        if text == "quit":
            break

        lastText = text

    transport.close()

except Thrift.TException as tx:
    print(tx.message)



def SubscribeSensoryMemory():
    print("hello")
    pass
