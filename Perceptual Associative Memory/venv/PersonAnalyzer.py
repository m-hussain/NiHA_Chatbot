from NameFinder import isName



def getPersonFromWordSignal(Words_Signal:dict):
    for word in Words_Signal:
        ne_tag = Words_Signal[word]['ne_Tag']
        if ne_tag == "PERSON":
            return ne_tag
        else:
            return "null"


def identifyPersonFromPickle(TokenizedSentence:list):

    #@TODO Need to write patternes before searching list:
    #@TODO Like: "__My name is__ mahmood", "__He is__ mahmood", "__I am__", "__me__ mahmood,
    #@TODO WORD POS Tag is "NNP" if not then above patterns


    from TextCleaner import cleanTokenizedText

    tokenizedSentence = cleanTokenizedText(TokenizedSentence)


    name = []
    for token in tokenizedSentence:
        token = str(token)
        token = token.capitalize()
        #print("token : ", token)
        if isName(token):
            name.append(token)
        else:
            name.append("null")

    count = 0
    N = []

    while count < len(name):
        list = []
        if name[count] != "null":
            while  name[count] != "null":
                list.append(name[count])
                count += 1
            string = ' '.join(list)
            N.append(string)
        count += 1

    # print("List : ", N)
    if len(N) == 1:
         return N[0]

    else: return N


def getPersonFromSentenceSignal(Chunked_Sentence_Signal: dict):
    for phrase in Chunked_Sentence_Signal:
        ne_tag = Chunked_Sentence_Signal[phrase]['ne_Tag']
        phrase_label = Chunked_Sentence_Signal[phrase]['phrase_label']
        if ne_tag == "PERSON":
            return phrase_label
        else:
            return "null"

def getPerson(Chunked_Sentence_Signal, sentence_tokens):
    response = getPersonFromSentenceSignal(Chunked_Sentence_Signal)

    if response == "null" or Chunked_Sentence_Signal=={}:
        response = identifyPersonFromPickle(sentence_tokens)
        if response == []:
            response = "null"
    return response



if __name__ == '__main__':

    from nltk import word_tokenize

    # sentence = "My name is Mahmood Hussain and his name is Ali. His father name is Wajahat Mehmood Qazi."

    sentence = "My name is mahmood hussain."

    print("sentence : ", sentence)

    tokenized_sentence = word_tokenize(sentence)

    print("tokenized_sentence : ", tokenized_sentence)
    # print("tokenized_sentences[0] : ", tokenized_sentence)

    name = identifyPersonFromPickle(tokenized_sentence)

    print("\nnames : ", name)

