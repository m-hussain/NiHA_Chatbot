"""""
words = \
    {
        0 : {"label":"There", "pos":"ab","ne":"xy"},
        1 : {"label":"is", "pos":"bc","ne":"xz"},
        2 : {"label":"cat", "pos":"cd","ne":"zy"}
    }

# print(words[1]["pos"])


sentences = \
    {
        0 : {
                "label"     : "There is cat",
                "words"     : {
                                0: {"label": "There", "pos": "ab", "ne": "xy"},
                                1: {"label": "is", "pos": "bc", "ne": "xz"},
                                2: {"label": "cat", "pos": "cd", "ne": "zy"}
                              },
                "sentiment" : "positive",
                "person"    : "self",
                "location"  : "unknown",
                "timeStamp" : "timeStamp",
                "time"      : "tense"
            },
        1 : {
                "label"      : "cat is cute",
                "words"      : {
                                0: {"label": "cat", "pos": "ab", "ne": "xy"},
                                1: {"label": "is", "pos": "bc", "ne": "xz"},
                                2: {"label": "cute", "pos": "cd", "ne": "zy"}
                               },
                "sentiment" : "positive",
                "person"    : "self",
                "location"  : "unknown",
                "timeStamp" : "timeStamp",
                "time"      : "tense"
            }

    }
# print(sentences[0]["label"])

"""""


if __name__ == '__main__':

    from nltk import sent_tokenize, word_tokenize
    sentence_label      = "sentence_label"
    words_in_sentence   = "words"
    sentiment           = "sentiment"
    person              = "person"
    location            = "location"
    timeStamp           = "timeStamp"
    timeOfConversation  = "tense"
    word_label          = "word_label"

    sentences_signal = {}
    while(True):
        text = input("Text : ")
        #text = "This is cat. Cat is cute."
        sentences = sent_tokenize(text)
        sentences_count = 0
        #print(sentences)
        for sentence in sentences:
            sentence_signal = {}
            sentence_signal[sentence_label] = sentence
            sentence_signal[sentiment] = "Call_Sentiment_Method_Here"


            words = word_tokenize(sentence)
            #print(words)
            word_count = 0
            words_signal = {}
            for word in words:
                word_signal = {}
                word_signal[word_label] = word
                words_signal[word_count] = word_signal
                word_count += 1
            #print("words_signal", words_signal)
            sentence_signal[words_in_sentence]= words_signal

            sentences_signal[sentences_count] = sentence_signal
            sentences_count += 1

        print("sentence signal : ", sentences_signal)
        for sentence_signal_count in sentences_signal:
        #     print(sentence_signal_count)
        #     print("sentence_signal_id : ", sentence_count, "\nsentence_signal : ", sentences_signal[sentence_count])
        #     print("___DETAILS___")
            print("sentence_signal_id : ", sentence_signal_count)
            for attribute in sentences_signal[sentence_signal_count]:
                print("\t\t", attribute, " : ", sentences_signal[sentence_signal_count][attribute])
