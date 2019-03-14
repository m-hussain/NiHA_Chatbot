class Interogative:

    LIST_OF_QUESTION_WORDS = \
        [
            "how", "what", "when", "where", "which", "who", "whom", "whose", "why",
            "how come", "how far", "how long", "how many", "how much", "how old",
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
            #'VB',  # simple verb such as do does
            'VBP',  # verb, present tense, not 3rd person singular examples: are, am
            'VBZ',  # verb, present tense, 3rd person singular   example: is
            'MD',  # Modal example could, would..
            'VBD'  # This might be ambiguous for 3rd last pattern but fine for 2nd last
        ]


    def findTupleContainsWord(self, posTaggedSentence, word):
        tupleIndex = -1
        count = 0
        for tuple in posTaggedSentence:
            if str(tuple[0]).startswith(word):
                tupleIndex = count
                break
            count+=1
        return tupleIndex



    def pattern1(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 1
                )
                and
                (
                    str(posTaggedSentence[-1][0]).startswith('?')
                )
        ):
            return True

    def pattern2(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 1
                )
                and
                (
                    (
                        str(posTaggedSentence[0][0]).startswith(tuple(['do','does','did']))
                    )
                    and
                    (
                        str(posTaggedSentence[1][1]).startswith('PRP')
                    )

                )
        ):
            return True

    def pattern3(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 1
                )
                and
                (
                    (
                        str(posTaggedSentence[0][0]).startswith(tuple(["since","for"]))
                    )
                    and
                    (
                        str(posTaggedSentence[1][0]).startswith(tuple(self.LIST_OF_QUESTION_WORDS))
                    )

                )
        ):
            return True

    def pattern4(self, posTaggedSentence):
        if (
                str(posTaggedSentence[0][0]).startswith(tuple(self.LIST_OF_QUESTION_WORDS))
        ):
            return True

    def pattern5(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 1
                )
                and
                (
                    str(posTaggedSentence[0][1]).startswith(tuple(self.LIST_OF_HELPINGVERBS_MODELAUXILARY_TAGS))
                )
        ):
            return True

    def pattern6(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 3
                )
                and
                (
                    str(posTaggedSentence[-3][1]).startswith(",")
                    and
                    str(posTaggedSentence[-2][1]).startswith("VBZ")
                    and
                    str(posTaggedSentence[-1][1]).startswith("PRP")
                )
        ):
            return True

    def pattern7(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 4
                )
                and
                (
                    str(posTaggedSentence[-4][1]).startswith(",")
                    and
                    str(posTaggedSentence[-3][1]).startswith("VBZ")
                    and
                    str(posTaggedSentence[-2][1]).startswith("RB")
                    and
                    str(posTaggedSentence[-1][1]).startswith("PRP")
                )
        ):
            return True

    def pattern8(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 3
                )
                and
                (
                    str(posTaggedSentence[-3][1]).startswith(",")
                    and
                    str(posTaggedSentence[-2][1]).startswith("MD")
                    and
                    str(posTaggedSentence[-1][1]).startswith("PRP")
                )
        ):
            return True

    def pattern9(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 4
                )
                and
                (
                    str(posTaggedSentence[-4][1]).startswith(",")
                    and
                    str(posTaggedSentence[-3][1]).startswith("MD")
                    and
                    str(posTaggedSentence[-2][1]).startswith("RB")
                    and
                    str(posTaggedSentence[-1][1]).startswith("PRP")
                )
        ):
            return True

    def pattern10(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 3
                )
                and
                (
                    str(posTaggedSentence[-3][1]).startswith(",")
                    and
                    str(posTaggedSentence[-2][1]).startswith("VBZ")
                    and
                    str(posTaggedSentence[-1][1]).startswith("RB")
                )
        ):
            return True

    def pattern11(self, posTaggedSentence):
        if (
                (
                   len(posTaggedSentence) > 4
                )
                and
                (
                    str(posTaggedSentence[-4][1]).startswith(",")
                    and
                    str(posTaggedSentence[-3][1]).startswith("VBZ")
                    and
                    str(posTaggedSentence[-2][1]).startswith("RB")
                    and
                    str(posTaggedSentence[-1][1]).startswith("RB")
                )
        ):
            return True


    def pattern12(self, posTaggedSentence):
        if (
                (
                    len(posTaggedSentence) > 3
                )
                and
                (
                    str(posTaggedSentence[-3][1]).startswith(",")
                    and
                    str(posTaggedSentence[-2][1]).startswith("VBZ")
                    and
                    str(posTaggedSentence[-1][1]).startswith("IN")
                )
        ):
            return True

    def pattern13(self, posTaggedSentence):
        if (
                (
                   len(posTaggedSentence) > 4
                )
                and
                (
                    str(posTaggedSentence[-4][1]).startswith(",")
                    and
                    str(posTaggedSentence[-3][1]).startswith("VBZ")
                    and
                    str(posTaggedSentence[-2][1]).startswith("RB")
                    and
                    str(posTaggedSentence[-1][1]).startswith("IN")
                )
        ):
            return True

    # THIS PATTERN IS INCOMPLETE
    # WORD DOCUMENT FOR FALSE NEGATIVES AND PDF CONTAINING INFORMATION FOR INDIRECT QUESTIONS
    def pattern14(self, posTaggedSentence):
        if (len(posTaggedSentence) > 3):
            index = self.findTupleContainsWord(posTaggedSentence,"if")
            if (
                    (
                        index != -1
                    )
                    and
                    (
                        len(posTaggedSentence) > index+2
                    )
                    and
                    (
                        str(posTaggedSentence[index + 1][1]).startswith("PRP")
                    )
                    and
                    (
                        (
                            str(posTaggedSentence[index + 2][1]).startswith("VB")
                        )
                        or
                        (
                            str(posTaggedSentence[index + 2][1]).startswith("IN")
                        )
                        or
                        (
                            str(posTaggedSentence[index + 2][1]).startswith("MD")
                        )
                    )
            ):
                return True

    def isQuestion(self, Sentence):
        from posTagger import tagPOS
        posTaggedSentence = tagPOS(str(Sentence))

        if(self.pattern1(posTaggedSentence)):
            return True
        elif (self.pattern2(posTaggedSentence)):
            return True
        elif (self.pattern3(posTaggedSentence)):
            return True
        elif(self.pattern4(posTaggedSentence)):
            return True
        elif(self.pattern5(posTaggedSentence)):
            return True
        elif(self.pattern6(posTaggedSentence)):
            return True
        elif(self.pattern7(posTaggedSentence)):
            return True
        elif (self.pattern8(posTaggedSentence)):
            return True
        elif (self.pattern9(posTaggedSentence)):
            return True
        elif (self.pattern10(posTaggedSentence)):
            return True
        elif (self.pattern11(posTaggedSentence)):
            return True
        elif (self.pattern12(posTaggedSentence)):
            return True
        elif (self.pattern13(posTaggedSentence)):
            return True
        elif (self.pattern14(posTaggedSentence)):
            return True
        else:
            return False


### TESTING ####
q = Interogative()
while(True):
    sentence = input("Sentence : ")
    print("Is Question : ", q.isQuestion(sentence))
