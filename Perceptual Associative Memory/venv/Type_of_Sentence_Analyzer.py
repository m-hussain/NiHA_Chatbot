from QuestionRecognizer import isQuestion

# Getting Type by analyzing all possible types of sentences
def getSentenceType(Sentence, POS_Tagged_Sentence):

    sentenceType = "statement"
    reason = ["Reason : No other rule matched."]

    isQ, reason = isQuestion(Sentence, POS_Tagged_Sentence)
    if isQ:
        sentenceType = "interrogative"

    # isN, reason = isNegation(Sentence, POS_Tagged_Sentence)
    # if isN:
    #     sentenceType = "Negation"
    #
    # isE, reason = isExclamation(Sentence, POS_Tagged_Sentence)
    # if isE:
    #     sentenceType = "Exclamation"
    #
    # isO, reason = isOrder(Sentence, POS_Tagged_Sentence)
    # if isO:
    #     sentenceType = "Order"

    return sentenceType, reason


"""
Types of Questions:

Yes/no (Polar Question) 
Direct
Indirect                # e.g, "i was wondering if you could buy me food".
Alternatives
Tag                     # e.g., there is no food in your bag. is there?

"""

"""
POLAR QUESTION

Polar question require the pattern that: 
it starts with Helping verb and follows the subject afterwards 

their answers can only ve Yes(affirmative) of No(Negation) 

for example:    Is he going to school?
Full answer:    Yes, he is going to school
short answer:   Yes 

"""

# e.g., there is no food in your bag. is there?
# e.g, "i was wondering if you could buy me food".


# Testing Interface
if __name__ == '__main__':
    from posTagger import *
    while(True):
        s = input("Sentence : ")
        p_s = tagPOS(s)

        #s = s.lower()
        type, reason = getSentenceType(s, p_s)
        print("type : ", type, ", reason : ", reason)
