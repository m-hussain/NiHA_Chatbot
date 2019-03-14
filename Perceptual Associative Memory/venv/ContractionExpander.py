import contractions as c

def expandContraction(sentence):
    fixedSentence = c.fix(sentence)
    return fixedSentence


##TESTING INTERFACE##
if __name__ == '__main__':
    while(True):
        sentence = input("Sentence : ")

        refinedSentence = expandContraction(sentence)

        print(refinedSentence)
