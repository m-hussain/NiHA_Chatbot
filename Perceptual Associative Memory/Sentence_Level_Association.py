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
from Type_of_Sentence_Analyzer import getType
from SystemTime import getSystemTime
from I_Fix import fix_i
from ContractionExpander import expandContraction
from utilities import print_sentences_signal

## SENTENCE LEVEL PROPERTIES
sentence_label      = "sentence_label"
pos_tagged_sentence = "sentence_pos"
words_in_sentence   = "words"
sentiment           = "sentiment"
person              = "person"
location            = "location"
timeStamp           = "timeStamp"
timeOfConversation  = "tense"
typeOfSentence      = "type"

## WORD LEVEL PROPERTIES
word_label          = "word_label"
word_pos            = "word_pos"
word_ne             = "entity"


while (True):
    sentences_signal = {}
    text = input("Text : ")
    text = expandContraction(text)
    # text = "This is cat. Cat is cute."
    #sentences = sent_tokenize(text)

    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(fix_i(sentence)) for sentence in tokenized_sentences]
    chunked_sentences = ne_chunk_sents(tagged_sentences)
    #
    # for sentence in sentences:
    #     tagged_text["sentence_label"] = sentence
    #
    # for tagged_sentence in tagged_sentences:
    #     tagged_text["sentence_pos"] = tagged_sentence
    #


    sentences_count = 0
    # print(sentences)
    for sentence in sentences:
        sentence_signal = {}
        sentence_signal[sentence_label] = sentence
        sentence_signal[sentiment] = getSentiment(sentence)
        sentence_signal[pos_tagged_sentence] = tagged_sentences[sentences_count]
        sentence_signal[typeOfSentence] = getType(sentence, sentence_signal[pos_tagged_sentence])
        sentence_signal[timeStamp] = getSystemTime()
        words = word_tokenize(sentence)
        # print(words)
        word_count = 0
        words_signal = {}
        for word in words:
            word_signal = {}
            word_signal[word_label] = word
            words_signal[word_count] = word_signal
            word_count += 1
        # print("words_signal", words_signal)
        sentence_signal[words_in_sentence] = words_signal

        sentences_signal[sentences_count] = sentence_signal
        sentences_count += 1

    # print("sentence signal : ", sentences_signal)
    # for sentence_signal_count in sentences_signal:
    #     #     print(sentence_signal_count)
    #     #     print("sentence_signal_id : ", sentence_count, "\nsentence_signal : ", sentences_signal[sentence_count])
    #     #     print("___DETAILS___")
    #     print("sentence_signal_id : ", sentence_signal_count)
    #     for attribute in sentences_signal[sentence_signal_count]:
    #         print("\t\t", attribute, " : ", sentences_signal[sentence_signal_count][attribute])

    print_sentences_signal(sentences_signal)