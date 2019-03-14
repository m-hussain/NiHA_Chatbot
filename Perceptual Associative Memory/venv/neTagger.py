#from nameparser.parser import HumanName
import nltk
from posTagger import *
from filterStopWords import *

def tagNE(Sentence):

    sentence    = str(Sentence)
    #sentence    = filterCommonWords(sentence)
    #sentence    = sentence.title()
    posTagged   = tagPOS(str(sentence))
    NE_tagged   = nltk.ne_chunk(posTagged)
    return NE_tagged

#Testing Interface
if __name__ == '__main__':
    while(True):
        s = input("Sentence : ")
        print(s)
        #s = "I live in Lahore and works at Google."
        tree = tagNE(s)
        print("NE Tagged : ", t)
        tagged = []
        for tupple in tree:
            print(tupple)
            if hasattr(tupple, 'label'):
                tagged = []
              #     if chunk.label() == 'GPE':
              #         print(chunk.label())
                  #print(chunk.label(), ' '.join(c[0] for c in chunk))
