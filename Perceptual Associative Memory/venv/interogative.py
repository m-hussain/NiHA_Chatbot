# from posTagger import *
#
# def getType(Sentence):
#
#     sentenceType = ""
#
#     tagged_question = False
#
#     sentence = str(Sentence)
#
#     posTaggedSentence = tagPOS(sentence)
#
#     listOfQuestionWords = \
#         [
#             "how", "what", "when", "where", "which", "who", "whom", "whose", "why",
#             "how come", "how far", "how long", "how many", "how much", "how old"
#         ]
#
#     adjective_adverbs_tags = \
#         [
#             'JJ'  ,  # adjective
#             'JJR' ,  # adjective comparative
#             'JJS' ,  # adjective superlative
#             'RB'  ,  # adverb
#             'RBR' ,  # adverb comparative
#             'RBS'    # adverb superlative
#         ]
#
#     helpingVerbs_modalAuxilary_tags = \
#         [
#             'VB'  ,  # simple verb such as do does
#             'VBP' ,  # verb, present tense, not 3rd person singular examples: are, am
#             'VBZ' ,  # verb, present tense, 3rd person singular   example: is
#             'MD'  ,  # Modal example could, would..
#             'VBD'    # This might be ambiguous for 3rd last pattern but fine for 2nd last
#         ]
#
#
#     if posTaggedSentence[0][0] == 'how' \
#             and \
#             str(posTaggedSentence[1][1]).startswith(tuple(adjective_adverbs_tags)):
#
#         how_with_adjective_or_adverb = True
#
#     else:
#
#         how_with_adjective_or_adverb = False
#
#     if str(posTaggedSentence[0][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags)):
#         helping_verb_at_start = True
#     else:
#         helping_verb_at_start = False
#
#
#     if (len(sentence) > 2):
#
#
#         if  (#for positive ending tagged question
#                 str(posTaggedSentence[-2][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags))
#                 and
#                 str(posTaggedSentence[-1][1]).startswith('PRP')
#             ) \
#                 or \
#             (#for negative ending tagged question
#                 str(posTaggedSentence[-3][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags))
#                 and
#                 str(posTaggedSentence[-2][1])=='RB'
#                 and
#                 str(posTaggedSentence[-1][1])=='PRP'
#             ):
#
#                     tagged_question = True
#
#     if sentence.startswith(tuple(listOfQuestionWords)) \
#             or \
#             sentence.endswith('?') \
#             or \
#             how_with_adjective_or_adverb \
#             or \
#             helping_verb_at_start \
#             or \
#             tagged_question:
#
#             sentenceType = "interrogative"
#
#     else:
#             sentenceType =  "statement"
#
#
#     return sentenceType
#
#
# """
# Types of Questions:
#
# Yes/no (Polar Question)
# Direct
# Indirect                # e.g, "i was wondering if you could buy me food".
# Alternatives
# Tag                     # e.g., there is no food in your bag. is there?
# wh-questions
#
# """
#
# """
# POLAR QUESTION
#
# Polar question require the pattern that:
# it starts with Helping verb and follows the subject afterwards
#
# their answers can only ve Yes(affirmative) of No(Negation)
#
# for example:    Is he going to school?
# Full answer:    Yes, he is going to school
# short answer:   Yes
#
# """
#
# # e.g., there is no food in your bag. is there?
# # e.g, "i was wondering if you could buy me food".
#
#
# # Testing Interface
# while(True):
#     s = input("Sentence : ")
#     #s = s.lower()
#     type = getType(s)
#     print("type : ", type)



#Question1 = Enum('TypeOfQuestion', 'Polar Tagged Request Alternative Indirect Direct_Straight Direct_Inverted Direct_Prep')

#print(list(Question1))


from enum import Enum
class Question(Enum):
    POLAR = 1
    TAGGED = 2
    REQUEST = 3
    ALTERNATIVE = 4
    INDIRECT = 5
    DIRECT_STRAIGHT = 6
    DIRECT_INVERTED = 7
    DIRECT_PREP = 8
    UNKNOWN = 9


class InterrogativePattern:

    LIST_OF_QUESTION_WORDS = \
        [
            "how", "what", "when", "where", "which", "who", "whom", "whose", "why",
            "how come", "how far", "how long", "how many", "how much", "how old"
        ]

    LIST_OF_ADJECTIVE_TAGS = \
        [
            'JJ',  # adjective
            'JJR',  # adjective comparative
            'JJS',  # adjective superlative
        ]

    LIST_OF_ADVERB_TAGS = \
        [
            'RB',  # adverb
            'RBR',  # adverb comparative
            'RBS'  # adverb superlative
        ]

    LIST_OF_HELPINGVERBS_MODELAUXILARY_TAGS = \
        [
            'VB',  # simple verb such as do does
            'VBP',  # verb, present tense, not 3rd person singular examples: are, am
            'VBZ',  # verb, present tense, 3rd person singular   example: is
            'MD',  # Modal example could, would..
            'VBD'  # This might be ambiguous for 3rd last pattern but fine for 2nd last
        ]

    def identifyPattern(self, Sentence):
        from posTagger import tagPOS
        posTaggedSentence = tagPOS(str(Sentence))

        if(str(posTaggedSentence[-1][0]).startswith('?')):
            return Question.UNKNOWN

        if ((str(posTaggedSentence[0][1]).startswith(tuple(self.LIST_OF_HELPINGVERBS_MODELAUXILARY_TAGS))) \
                and
                (str(posTaggedSentence[1][1]).startswith())
        ):
            return Question.POLAR


sentence = input("Sentence : ")
InterrogativePattern = InterrogativePattern()

pattern = InterrogativePattern.identifyPattern(sentence)

print("pattern : ",pattern)
print("type : ",type(pattern))
