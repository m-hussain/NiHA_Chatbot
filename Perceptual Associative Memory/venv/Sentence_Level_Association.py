# from    sentimentAnalysis       import *
# from    timeAnalysis            import *
# from    placeAnalysis           import *
# from    personAnalysis          import *
# from    topicAnalysis           import *
# from    TOS_Analyzer            import *
#
# def sentenceTagger(text_signal):
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
from LocationAnalyzer import getLocation_NE

## SENTENCE LEVEL PROPERTIES
sentence_label      = "sentence_label"  #done
pos_tagged_sentence = "sentence_pos"    #done
words_in_sentence   = "words"           #done
sentiment           = "sentiment"       #done
person              = "person"
place               = "location"
timeStamp           = "timeStamp"       #done
timeOfConversation  = "tense"           #done
typeOfSentence      = "type"            #done
topic               = "topic"

## WORD LEVEL PROPERTIES
word_label          = "word_label"
word_pos            = "word_pos"
word_ne             = "entity"


def AssociateSentenceLevelTags(text):
    sentences_signal = {}
    text = expandContraction(text)

    #TODO use sentence__level__pos_tagger and sentence__level__word_tokenizer
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(fix_i(sentence)) for sentence in tokenized_sentences]
    chunked_sentences = ne_chunk_sents(tagged_sentences)

    Word_Level_Tagged_Sentences = AssociateWordLevelTags(chunked_sentences)

    sentences_count = 0
    for sentence in sentences:
        sentence_signal = {}
        sentence_signal[sentence_label] = sentence
        sentence_signal[sentiment] = getSentiment(sentence)
        sentence_signal[pos_tagged_sentence] = tagged_sentences[sentences_count]
        sentence_signal[typeOfSentence] = getSentenceType(sentence, sentence_signal[pos_tagged_sentence])
        sentence_signal[timeStamp] = getSystemTime()

        words_signal = Word_Level_Tagged_Sentences[sentences_count]

        getLocation_NE(words_signal)


        sentence_signal[words_in_sentence] = words_signal

        sentences_signal[sentences_count] = sentence_signal
        sentences_count += 1

    return sentences_signal


if __name__ == '__main__':

    # text = input("Text : ")
    document = "The Washington Monument is the most prominent structure in Washington, D.C. and one of the city's early attractions. It was built in honor of George Washington, who led the country to independence and then became its first President."

    sentences_signal = AssociateSentenceLevelTags(document)

    print_sentences_signal(sentences_signal)

