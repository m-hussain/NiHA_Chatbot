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
    sentence_label = "sentence_label"
    words_in_sentence = "words"
    sentiment = "sentiment"
    person = "person"
    location = "location"
    timeStamp = "timeStamp"
    timeOfConversation = "tense"

    sentences_signal = {}
    while(True):
        text = input("Text : ")
        sentences = sent_tokenize(text)
        sentences_count = 0
        print(sentences)
        for sentence in sentences:
            sentence_signal = {}
            sentence_signal[sentence_label] = sentence

            words = word_tokenize(sentence)
            word_count = 0
            words_signal = {}
            for word in words:
                word_signal = {}
                word_signal["label"] = word
                words_signal[word_count] = word_signal
                word_count += 1
            #print("words_signal", words_signal)
            sentence_signal[words_in_sentence]= words_signal

            sentences_signal[sentences_count] = sentence_signal
            sentences_count += 1

        #print("sentence signal : ", sentences_signal)
        for sentence_count in sentences_signal:
            print()
            print("SENTENCE_ID : ", sentence_count, "\nSENTENCE_SIGNAL : ", sentences_signal[sentence_count])
            for attribute in sentences_signal[sentence_count]:
                print("\tATTRIBUTE : ", attribute, ", \tVALUE : ", sentences_signal[sentence_count][attribute])

        # for token_sentence in tokenized_sentences:
        #     sentences[sentences_count][sentence_label]= token_sentence
        # print(sentences)
        # sentences_count += 1
