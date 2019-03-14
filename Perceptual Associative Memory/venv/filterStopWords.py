from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
def filterStopWords(Sentence):
    sentence = str(Sentence)

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(sentence)

    #filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = ''

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + ' ' + str(w)

    return filtered_sentence


from nltk.corpus import words
def filterCommonWords(Sentence):

    sentence = str(Sentence)
    wordsList = words.words()
    word_tokens = word_tokenize(sentence)

    filtered_sentence = ''
    for w in word_tokens:
        if w not in wordsList:
            filtered_sentence = filtered_sentence + ' ' + str(w)

    return filtered_sentence


##Testing Interface
# while(True):
#     s = input("Sentence : ")
#     f = filterStopWords(s)
#     print("After Stop Word Filter: ", f)
#     f1 = filterCommonWords(s)
#     print("After Common Word Filter: ", f1)
#
