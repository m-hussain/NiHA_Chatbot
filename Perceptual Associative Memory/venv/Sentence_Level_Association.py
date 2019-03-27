# from    sentimentAnalysis       import *
# from    timeAnalysis            import *
# from    placeAnalysis           import *
# from    personAnalysis          import *
# from    topicAnalysis           import *
# from    TOS_Analyzer            import *
#
## def sentenceTagger(text_signal):
#     topic           =   []
#     person          =   []
#     place           =   []
#     time            =   []
#     sentiment       =   []
#     typeOfSentence  =   []
#
#     topic.append(getTopic(Sentence))
#     person.append(getPersons(Sentence))
#     place.append(getGPSLocation())
#     place.append((getLocation(Sentence)))
#     time.append(getTime())
#     time.append(getTense(Sentence))
#     sentiment.append(getSentiments(Sentence))
#     typeOfSentence.append(getType(Sentence))
#
#     taggedSentence = {  Sentence:[topic, person, place, time, sentiment, typeOfSentence]   }
#
#     return taggedSentence
#
#
# ##Testing Interface
# if __name__ == '__main__':
#     while(True):
#         sentence = input("Sentence : ")
#         s = sentenceTagger(sentence)
#         print("Sentence After Tagging : ", s)
#
#         # print("Sentiment : ", s[sentence][4])
#         # print("Sentiment : ", s[sentence][4][0])
#         # print("Sentiment : ", s[sentence][4][0]['pos'])
#         #
#         # print("Time : ", s[sentence][3][0].split(" ")[4])


#from nltk import sent_tokenize, word_tokenize
from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk_sents
from SentimentAnalyzer import getSentiment
from Type_of_Sentence_Analyzer import getSentenceType
from SystemTime import getSystemTime
from I_Fix import fix_i
from ContractionExpander import expandContraction
from utilities import print_sentences_signal
from Word_Level_Association import AssociateWordLevelTags
from LocationAnalyzer import getLocation_Sent_NE
from SentenceNE import setSentNE
from PersonAnalyzer import getPersonFromSentence
from TopicAnalyzer import getTopic


## SENTENCE LEVEL PROPERTIES
sentence_label      = "sentence_label"  #done
pos_tagged_sentence = "sentence_pos"    #done
#ne_tagged_sentence  = "sentence_ne"
words_in_sentence   = "words"           #done
sentiment           = "sentiment"       #done
person              = "person"          #done
place               = "location"        #done
timeStamp           = "timeStamp"       #done
timeOfConversation  = "tense"           #done
typeOfSentence      = "type"            #done
topicOfSentence     = "topic"

## WORD LEVEL PROPERTIES
word_label          = "word_label"
word_pos            = "word_pos"
word_ne             = "entity"


def AssociateSentenceLevelTags(text):
    sentences_signal = {}
    text = expandContraction(text)

    ##TODO use sentence__level__pos_tagger and sentence__level__word_tokenizer
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(fix_i(sentence)) for sentence in tokenized_sentences]
    chunked_sentences = ne_chunk_sents(tagged_sentences)
    chunked_sentences1 = ne_chunk_sents(tagged_sentences)

    #chunked_sentences1 = copy.deepcopy(chunked_sentences)
    #print("chunked_sentences : ",chunked_sentences)

    Word_Level_Tagged_Sentences = AssociateWordLevelTags(chunked_sentences)
    #print("Word_Level_Tagged_Sentences : ", Word_Level_Tagged_Sentences)

    #print("chunked_sentences1 : ",chunked_sentences1)

    ne_tagged_sentences = setSentNE(chunked_sentences1)
    #print("ne_tagged_sentence : ", ne_tagged_sentences)

    #print("chunked_sentences : ",chunked_sentences)


    sentences_count = 0
    for sentence in sentences:
        sentence_signal = {}
        sentence_signal[sentence_label] = sentence
        sentence_signal[sentiment] = getSentiment(sentence)
        sentence_signal[pos_tagged_sentence] = tagged_sentences[sentences_count]
        #print("ne_tagged_sentences[sentences_count] : ", ne_tagged_sentences[sentences_count])
        #sentences_signal["sentence_ne"] = "sentence_ne" #ne_tagged_sentences[sentences_count]
        sentence_signal[typeOfSentence] = getSentenceType(sentence, sentence_signal[pos_tagged_sentence])
        sentence_signal[timeStamp] = getSystemTime()

        #print("Word_Level_Tagged_Sentences[sentences_count] : ", Word_Level_Tagged_Sentences[sentences_count])
        words_signal = Word_Level_Tagged_Sentences[sentences_count]


        sentence_signal[place] = getLocation_Sent_NE(ne_tagged_sentences[sentences_count])
        #print(ne_tagged_sentences[sentences_count])
        sentence_signal[person] = getPersonFromSentence(ne_tagged_sentences[sentences_count])

        sentence_signal[words_in_sentence] = words_signal
        print("sentence : ", sentence)

        sentence_signal[topicOfSentence] = getTopic(sentence)

        sentences_signal[sentences_count] = sentence_signal
        sentences_count += 1

    return sentences_signal


if __name__ == '__main__':

    # text = input("Text : ")
    document = "My Name is Mahmood Hussain. i live in Lahore, Punjab, Pakistan. i study in COMSATS University Islamabad."

    #document = "The Washington Monument is the most prominent structure in Washington, D.C. and one of the city's early attractions. It was built in honor of George Washington, who led the country to independence and then became its first President."

    sentences_signal = AssociateSentenceLevelTags(document)

    #print("sentences_signal : ", sentences_signal)

    print_sentences_signal(sentences_signal)

