import sys
sys.path.append("../../../NiHA_Chatbot/")

from thrift_code.GenPy.SignalTransfer_NameSpace import SignalTransfer_Service

import _pickle as pickle

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import json
configurations = open("../../Configurations/config.json",'r').read()
configurations = json.loads(configurations)
SensorySocket = configurations["SensorySocket"]


class SignalTransferHandler:
    dataToPublish = "Text from sensory memory...."

    def PublishData(self, SensorySignal):
        print("Data Received : ", SensorySignal)
        SignalTransferHandler.dataToPublish = SensorySignal

    def getBinaryStream(self):
        sensorySignal = {}
        # text = "Text from sensory memory...."
        text = SignalTransferHandler.dataToPublish

        sensorySignal["text"] = text
        # print("text : ", text)
        # print("sensorySignal : ", sensorySignal)

        binary = pickle.dumps(sensorySignal, -1)

        # print("binary : ", binary)

        # print("type : ", type(binary))

        return binary

def __main__():
    handler = SignalTransferHandler()
    print("data by other object : ", handler.dataToPublish)
    processor = SignalTransfer_Service.Processor(handler)
    transport = TSocket.TServerSocket(host=SensorySocket["ip"], port=SensorySocket["port"])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Ready to Publish Data..")

    server.serve()


if __name__ == '__main__':
    __main__()