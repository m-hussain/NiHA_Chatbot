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
