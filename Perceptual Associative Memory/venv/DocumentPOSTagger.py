from nltk import word_tokenize
from nltk import pos_tag
from ContractionExpander import expandContraction
from I_Fix import fix_i
def tag_text_POS(document):

    text = expandContraction(document)

    text = fix_i(tokenized_text)

    sentences = nltk.sent_tokenize(text)



    text = Sentence
    #text = text.lower()
    #print(text)
    tokenized = word_tokenize(text)

    # print("before : ", tokenized)

    count = 0
    for count in range(len(tokenized)):
        if tokenized[count] == 'i':
            tokenized[count] = 'I'

    # print("after : ", tokenized)

    tagged = pos_tag(tokenized)

    return tagged
