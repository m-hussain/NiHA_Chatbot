
isFuture    = False

def isPastTense(posTaggedSentence):
    isPast = False
    index = 0
    for tuple in posTaggedSentence:
        if (tuple[1] == 'VBD' or tuple[1] == 'VBN'):
            isPast = True
            break
        index += 1
    return isPast, index

def isPresentTense(posTaggedSentence):
    isPresent = False
    index = 0
    for tuple in posTaggedSentence:
        if (tuple[1] == 'VB' or tuple[1] == 'VBG' or tuple[1] == 'VBP' or tuple[1] == 'VBZ'):
            isPresent = True
            break
        index += 1
    return isPresent, index

def isFutureTense(posTaggedSentence):

    isFuture = False
    index = 0
    for tuple in posTaggedSentence:
        if (tuple[1] == 'MD'):
            isFuture = True
            break
        index += 1
    return isFuture, index

def getTense(posTaggedSentence):
    if((isPastTense(posTaggedSentence))[0] and not(isFutureTense(posTaggedSentence)[0])):
        return "past"
    elif((isPresentTense(posTaggedSentence)[0]) and not(isFutureTense(posTaggedSentence)[0])):
        return "present"
    elif((isFutureTense(posTaggedSentence)[0]) and ( (isPresentTense(posTaggedSentence)[0]) or (isPastTense(posTaggedSentence)) )):
        return "future"
    else:
        return "unknown"

##TESTING INTERFACE##

if __name__ == '__main__':
    from posTagger import tagPOS
    from SystemTime import getSystemTime

    time = getSystemTime()

    while(True):

        sentence = input("Sentence : ")

        posTaggedSentence = tagPOS(sentence)

        #print("pos tagged sentence : ", posTaggedSentence)

        tense = getTense(posTaggedSentence)

        print("Tense : ", tense, " -- Time Stamp : ", time)
