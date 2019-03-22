def getPersonFromWord(Words_Signal:dict):
    for word in Words_Signal:
        ne_tag = Words_Signal[word]['ne_Tag']
        if ne_tag == "PERSON":
            return ne_tag
        else:
            return "null"

def getPersonFromSentence(Chunked_Sentence_Signal:dict):
    for phrase in Chunked_Sentence_Signal:
        ne_tag = Chunked_Sentence_Signal[phrase]['ne_Tag']
        phrase_label = Chunked_Sentence_Signal[phrase]['phrase_label']
        if ne_tag == "PERSON":
            return phrase_label
        else:
            return "null"

