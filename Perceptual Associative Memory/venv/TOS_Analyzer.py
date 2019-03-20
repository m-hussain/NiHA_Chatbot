helpingVerbs_modalAuxilary_tags = \
    [
        'VB'  ,  # simple verb such as do does
        'VBP' ,  # verb, present tense, not 3rd person singular examples: are, am
        'VBZ' ,  # verb, present tense, 3rd person singular   example: is
        'MD'  ,  # Modal example could, would..
        'VBD'    # This might be ambiguous for 3rd last pattern but fine for 2nd last
    ]
adjective_adverbs_tags = \
    [
        'JJ',  # adjective
        'JJR',  # adjective comparative
        'JJS',  # adjective superlative
        'RB',  # adverb
        'RBR',  # adverb comparative
        'RBS'  # adverb superlative
    ]
listOfSingleQuestionWords = ["how", "what", "when", "where", "which", "who", "whom", "whose", "why"]
listOfDoubleQuestionWords = ["how come", "how far", "how long", "how many", "how much", "how old"]

# "Rule1: Sentence Starts With Single_Word QuestionWords"
def isRule1(Sentence):
    description = "Rule1: Sentence Starts With Single_Word QuestionWords"
    if (Sentence.startswith(tuple(listOfSingleQuestionWords))):
        return True, description
    else:
        return False, "rule failed"
# "Rule2: Sentence Starts With Double_Word QuestionWords"
def isRule2(Sentence):
    description = "Rule2: Sentence Starts With Double_Word QuestionWords"
    if (Sentence.startswith(tuple(listOfDoubleQuestionWords))):
        return True , description
    else:
        return False, "rule failed"
# "Rule3: Sentence Starts with Helping_Verbs or Modal_Auxiliary words"
def isRule3(POS_Tagged_Sentence):
    description = "Rule3: Sentence Starts with Helping_Verbs or Modal_Auxiliary words"
    if str(POS_Tagged_Sentence[0][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags)):
        return True, description
    else:
        return False, "rule failed"
# "Rule4: sentence starts with how trailing by adjectives or adverbs"
def isRule4(POS_Tagged_Sentence):
    description = "Rule4: sentence starts with how trailing by adjectives or adverbs"
    if  (POS_Tagged_Sentence[0][0] == 'how') \
        and \
        (str(POS_Tagged_Sentence[1][1]).startswith(tuple(adjective_adverbs_tags)))\
        :   return True, description
    else:   return False, "rule failed"
# "Rule5: sentence ends with Interrogative Mark"
def isRule5(Sentence):
    description = "Rule5: sentence ends with Interrogative Mark"
    Sentence = str(Sentence)
    if Sentence.endswith("?"):
        return True, description
    else:
        return False, "rule failed"
# "Rule6: sentence ends with Helping_Verb or Modal_Auxiliary Trailing by Personal_Pronouns"
def isRule6(POS_Tagged_Sentence):
    print()
    description = "Rule6: sentence ends with Helping_Verb or Modal_Auxiliary Trailing by Personal_Pronouns"
    if (str(POS_Tagged_Sentence[-2][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags)) and str(
            POS_Tagged_Sentence[-1][1]).startswith('PRP')):
        return True, description
    else:
        return False, "rule failed"
# "Rule7: sentence ends with Helping_Verb or Modal_Auxiliary Trailing by Adjectives and Personal_Pronouns"
def isRule7(POS_Tagged_Sentence):
    description = "Rule7: sentence ends with Helping_Verb or Modal_Auxiliary Trailing by Adjectives and Personal_Pronouns"
    if(
            str(POS_Tagged_Sentence[-3][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags))
            and
            str(POS_Tagged_Sentence[-2][1]) == 'RB'
            and
            str(POS_Tagged_Sentence[-1][1]) == 'PRP'
    ): return True, description
    else: return False, "rule failed"

def isQuestion(Sentence, POS_Tagged_Sentence):
    reason = []
    isQuestion = False
    if (len(Sentence) == 1): # Rule1, Rule3 and Rule5
        passed, description = isRule1(Sentence)
        if passed:
            reason.append(description)
            isQuestion = True

        passed, description = isRule3(POS_Tagged_Sentence)
        if passed:
            reason.append(description)
            isQuestion = True

        passed, description = isRule5(Sentence)
        if passed:
            reason.append(description)
            isQuestion = True
    #
    # if (len(sentence) == 2):
    #
    #     pass
    #
    # if (len(sentence) >= 3):
    #     pass




def getType(Sentence, POS_Tagged_Sentence):

    sentenceType = "statement"
    sentence = str(Sentence)
    posTaggedSentence = POS_Tagged_Sentence



    if 1:

    else:
        sentenceType =


    return sentenceType


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
        type = getType(s, p_s)
        print("type : ", type)
