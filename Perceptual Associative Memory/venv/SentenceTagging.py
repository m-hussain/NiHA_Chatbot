from    SentimentAnalyzer       import *
from    TimeAnalyzer            import *
from    placeAnalysis           import *
from    personAnalysis          import *
from    topicAnalysis           import *
from    Type_of_Sentence_Analyzer  import *

def sentenceTagger(Sentence):

    topic           =   []
    person          =   []
    place           =   []
    time            =   []
    sentiment       =   []
    typeOfSentence  =   []

    topic.append(getTopic(Sentence))
    person.append(getPersons(Sentence))
    place.append(getGPSLocation())
    place.append((getLocation(Sentence)))
    time.append(getTime())
    time.append(getTense(Sentence))
    sentiment.append(getSentiments(Sentence))
    typeOfSentence.append(getType(Sentence))

    taggedSentence = {  Sentence:[topic, person, place, time, sentiment, typeOfSentence]   }

    return taggedSentence


#Testing Interface
while(True):
    sentence = input("Sentence : ")
    s = sentenceTagger(sentence)
    print("Sentence After Tagging : ", s)

    # print("Sentiment : ", s[sentence][4])
    # print("Sentiment : ", s[sentence][4][0])
    # print("Sentiment : ", s[sentence][4][0]['pos'])
    #
    # print("Time : ", s[sentence][3][0].split(" ")[4])
