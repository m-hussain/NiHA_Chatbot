from nltk.corpus import stopwords
from string import punctuation

stop = set(stopwords.words('english'))
exclude = set(punctuation)
#lemma = WordNetLemmatizer()

def clean(doc:str):
    stop_free = ' '.join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    #normalized = " ".join(lemma.lemmatize(word) for word in doc.split())
    return punc_free #normalized

def removeStopWords(tokenized_text:list):
    stop_free = []
    for word in tokenized_text:
        word = str(word).lower()
        if word not in stop:
            stop_free.append(word)
        else:
            stop_free.append("null")
    return stop_free

def removePuncuation(TokenizedSentence:list):
    punc_free = []
    for word in TokenizedSentence:
        if word not in exclude:
            punc_free.append(word)
        else:
            punc_free.append("null")

    # punc_free = ''.join(ch for ch in Sentence if ch not in exclude)

    return punc_free


def cleanTokenizedText(TokenizedText:list):
    tokenizedText = removePuncuation(TokenizedText)
    tokenizedText = removeStopWords(tokenizedText)
    return tokenizedText


# #normalized = " ".join(lemma.lemmatize(word) for word in doc.split())
# return punc_free #normalized


if __name__ == '__main__':
    sentence = "My name is Mahmood Hussain."


    from nltk import word_tokenize

    tokenized = word_tokenize(sentence)

    print("tokenized : ", tokenized)

    punc_free = removePuncuation(tokenized)

    print("punctuation free : ", punc_free)

    stop_free = removeStopWords(punc_free)

    print("Stopfree : ", stop_free)