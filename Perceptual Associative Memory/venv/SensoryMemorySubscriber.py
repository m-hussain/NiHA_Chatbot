import sys
sys.path.append("../../../NiHA_Chatbot/")

from thrift_code.GenPy.SignalTransfer_NameSpace import SignalTransfer_Service


# from ...thrift_code.GenPy.SignalTransfer_NameSpace import SignalTransfer_Service

import _pickle as pickle

# from PIL import Image
import io

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# from genpy.imageTransfer import ImageTransfer

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = SignalTransfer_Service.Client(protocol)
    transport.open()


    bytesData = client.getBinaryStream()

    print("bytesData : ", bytesData)

    # stream = io.BytesIO(bytesData)
    #
    # print("stream converted by BytesIO : ", stream)

    # img = Image.open(stream)
    # print(img)
    # img.show()
    # img.save("test.png")

    SensorySignal = pickle.loads(bytesData)

    print("SensorySignal : ", SensorySignal)

    transport.close()

except Thrift.TException as tx:
    print(tx.message)



def SubscribeSensoryMemory():
    print("hello")
    pass
