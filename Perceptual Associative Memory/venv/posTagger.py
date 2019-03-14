from nltk import word_tokenize
from nltk import pos_tag
#from ContractionExpander import expandContraction
#class POSTagger:

def tagPOS(Sentence):

    text = Sentence
    #text = text.lower()
    #print(text)
    tokenized = word_tokenize(text)

    # print("before : ", tokenized)

    count = 0
    for count in range(len(tokenized)):
        if tokenized[count] == 'i':
            tokenized[count] = 'I'

    # print("after : ", tokenized)

    tagged = pos_tag(tokenized)

    return tagged

#Testing Interface
if __name__ == '__main__':
    while(True):
        s = input("Sentence : ")
        t = tagPOS(s)
        print(t)
