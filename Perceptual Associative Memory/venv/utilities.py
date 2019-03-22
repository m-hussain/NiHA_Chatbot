sentences_signal = {}
def print_sentences_signal(sentences_signal):
    #print("sentence signal : ", sentences_signal)
    for sentence_signal_count in sentences_signal:
        #     print(sentence_signal_count)
        #     print("sentence_signal_id : ", sentence_count, "\nsentence_signal : ", sentences_signal[sentence_count])
        #     print("___DETAILS___")
        print("sentence_signal_id : ", sentence_signal_count)
        for attribute in sentences_signal[sentence_signal_count]:
            print("\t\t", attribute, " : ", sentences_signal[sentence_signal_count][attribute])

def print_word_signal(word_signal:dict):
    for sentence in word_signal:
        print("sentence ",sentence, " : ")
        words = word_signal[sentence]
        for word in words:
            print("\t\tword ",word," : ", words[word])
        print()

def print_phrase_signal(phrases_signal:dict):
    for sentence in phrases_signal:
        print("sentence ",sentence, " : ")
        phrases = phrases_signal[sentence]
        for phrase in phrases:
            print("\t\tphrase ",phrase," : ", phrases[phrase])
        print()
