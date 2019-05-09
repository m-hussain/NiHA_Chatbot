import hashlib
def getHash(text):
    # mystring = input('Enter String to hash: ')
    # Assumes the default UTF-8
    mystring = text
    encoded_string = mystring.encode()
    print("encoded string : ",encoded_string)
    hash_object = hashlib.md5()
    print("hash_object : ", hash_object )
    hash_digest = hash_object.hexdigest()
    print("hash_digest : ", hash_digest)

    #d41d8cd98f00b204e9800998ecf8427e

    return hash_digest

import glob
path = glob.glob("aiml_to_qa/*.txt")
print(path)
source = open(path[1])
lines = source.readlines()
print(lines)

from vis import draw
from py2neo import Graph, Node, Relationship
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

graph.delete_all()

sentence = "hello there, how are you ?"
sentence_hash = getHash(sentence)
question_pattern = Node("Sentence", signalType="Working_Memory", nodeID=sentence_hash, label=sentence, sentenceTag1="None", sentenceTag2 = "None", response_id = "None")

sentence = "I am fine, thank you."
sentence_hash = getHash(sentence)
response = Node("Sentence", singalType="Working_Memory", nodeID=sentence_hash, label=sentence, sentenceTag1="None", sentenceTag2 = "None", response_id = "None")

graph.create(question_pattern | response)

options = {"Sentence": "label", "Word": "label"}

# graph.create(Relationship(nicole, "LIKES", cokezero))
# graph.create(Relationship(nicole, "LIKES", mtdew))
# graph.create(Relationship(drew, "LIKES", mtdew))
# graph.create(Relationship(coke, "MAKES", cokezero))
# graph.create(Relationship(pepsi, "MAKES", mtdew))

# draw(graph, options)


