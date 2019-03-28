import _pickle as pickle

sensorySignal = {}
text = "Text from sensory memory."
sensorySignal["text"] = text
print("text : ",text)
print("sensorySignal : ",sensorySignal)

# ByteArr = io.BytesIO()
##text.save(imgByteArr, format='PNG')
# imgByteArr = imgByteArr.getvalue()

binary = pickle.dumps(sensorySignal, -1)

print("binary : ",binary)

print("type : ", type(binary))
