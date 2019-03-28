import sys
sys.path.append("../../../NiHA_Chatbot/")

from thrift_code.GenPy.SignalTransfer_NameSpace import SignalTransfer_Service

import io
import _pickle as pickle

#from genpy.imageTransfer import ImageTransfer

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class SignalTransferHandler:

# print("")


    def getBinaryStream(self):
        sensorySignal = {}
        text = "Text from sensory memory."
        sensorySignal["text"] = text
        print("text : ", text)
        print("sensorySignal : ", sensorySignal)

        # ByteArr = io.BytesIO()
        ##text.save(imgByteArr, format='PNG')
        # imgByteArr = imgByteArr.getvalue()

        binary = pickle.dumps(sensorySignal, -1)

        print("binary : ", binary)

        print("type : ", type(binary))

        return binary

if __name__ == '__main__':
    handler = SignalTransferHandler()
    processor = SignalTransfer_Service.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting python server...")

    server.serve()

















def PublishData(SensorySignal):
    pass
