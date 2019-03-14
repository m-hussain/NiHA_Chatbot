from neTagger import *

def getPersons(Sentence):

    person = []

    neTagged = tagNE(Sentence)

    for chunk in neTagged:
        if hasattr(chunk, 'label'):
            if chunk.label() == 'PERSON':
                person.append(' '.join(c[0] for c in chunk))
    return person

#Testing Interface
while(True):
    s = input("Sentence : ")
    p = getPersons(s)
    print("Person : ", p)

