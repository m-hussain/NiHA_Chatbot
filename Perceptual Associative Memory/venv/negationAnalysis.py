#from contractions import fix  # DIRECT
# from posTagger import tagPOS
# posTaggedSentence = tagPOS(sentence)

class NegationAnalysis:

    LIST_OF_NEGATION_WORDS = ["no", "not", "none", "no one", "nobody", "nothing", "neither", "nowhere", "never"]

    def isNegation(self, sentence):
        if any(word in sentence.split() for word in self.LIST_OF_NEGATION_WORDS):
            return True
        else:
            return False

# ##TESTING INTERFACE

# from contraction_expander import ContractionExpander #INDIRECT
#
# c = ContractionExpander()
# n = NegationAnalysis()
#
# while(True):
#     sentence = input("Sentence : ")
#
#     sentence = c.expandContraction(sentence)
#
#     print("After Expanding Contractions : ", sentence)
#
#     sentence = sentence.lower()
#
#     print("After Lower : ", sentence)
#
#     print("is negation : ", n.isNegation(sentence))

