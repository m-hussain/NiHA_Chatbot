#@ TODO Implement Each of following and shift in releative files
# def isExclamation(Sentence, POS_Tagged_Sentence):
#     isExclamation = False
#     reason = []
#
#     return isExclamation, reason
#
# def isNegation(Sentence, POS_Tagged_Sentence):
#     isNegation = False
#     reason = []
#
#     return isNegation, reason
#
# def isOrder(Sentence, POS_Tagged_Sentence):
#     isOrder = False
#     reason = []
#
#     return isOrder, reason


from QuestionRecognizer import isQuestion

# Getting Type by analyzing all possible types of sentences
def getType(Sentence, POS_Tagged_Sentence):

    sentenceType = "statement"

    isQ, reason = isQuestion(Sentence, POS_Tagged_Sentence)
    if isQ:
        sentenceType = "Interrogative"

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
        type, reason = getType(s, p_s)
        print("type : ", type, ", reason : ", reason)
