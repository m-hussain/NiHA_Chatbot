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
def isRule1(POS_Tagged_Sentence):
    description = "Rule1: Sentence Starts With Single_Word QuestionWords"
    if (POS_Tagged_Sentence[0][0].startswith(tuple(listOfSingleQuestionWords))):
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

# "Rule3: Sentence Starts with Helping_Verbs or Modal_Auxiliary words trailing by PRP(pronouns)"
def isRule3(POS_Tagged_Sentence):
    description = "Rule3: Sentence Starts with Helping_Verbs or Modal_Auxiliary words trailing by Personal_Pronouns"
    if  (str(POS_Tagged_Sentence[0][1]).startswith(tuple(helpingVerbs_modalAuxilary_tags))) \
            and \
        (str(POS_Tagged_Sentence[1][1]).startswith("PRP")):
        return True, description
    else:
        return False, "rule failed"

#"Rule4: sentence starts with how trailing by adjectives or adverbs"
def isRule4(POS_Tagged_Sentence):
    description = "Rule4: sentence starts with how trailing by adjectives or adverbs"
    if  (POS_Tagged_Sentence[0][0] == 'how') \
            and \
        (str(POS_Tagged_Sentence[1][1]).startswith(tuple(adjective_adverbs_tags))):
        return True, description
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

#For length = 1: Rule 1, Rule5
def checkRulesSet1(Sentence, POS_Tagged_Sentence):
    reason = []
    isQuestion = False

    passed, description = isRule1(POS_Tagged_Sentence)
    if passed:
        reason.append(description)
        isQuestion = True

    passed, description = isRule5(Sentence)
    if passed:
        reason.append(description)
        isQuestion = True
    return isQuestion, reason

# For length = 2: Rule_Set_1 along with Rule 2, Rule 3, Rule 4, and Rule 6.
def checkRulesSet2(Sentence, POS_Tagged_Sentence):
    reason = []
    isQuestion = False

    passed, description = checkRulesSet1(Sentence, POS_Tagged_Sentence)
    if passed:
        reason = description
        isQuestion = True

    passed, description = isRule2(Sentence)
    if passed:
        reason.append(description)
        isQuestion = True

    passed, description = isRule3(POS_Tagged_Sentence)
    if passed:
        reason.append(description)
        isQuestion = True

    passed, description = isRule4(POS_Tagged_Sentence)
    if passed:
        reason.append(description)
        isQuestion = True

    passed, description = isRule6(POS_Tagged_Sentence)
    if passed:
        reason.append(description)
        isQuestion = True

    return isQuestion, reason

# For length >= 3 : Rule_Set_1 along with Rule 7.
def checkRulesSet3(Sentence, POS_Tagged_Sentence):
    reason = []
    isQuestion = False

    passed, description = checkRulesSet2(Sentence, POS_Tagged_Sentence)
    if passed:
        reason = description
        isQuestion = True

    passed, description = isRule7(POS_Tagged_Sentence)
    if passed:
        reason.append(description)
        isQuestion = True
    return isQuestion, reason

# Checking all possible rules for questions
def isQuestion(Sentence, POS_Tagged_Sentence):
    isQuestion = False
    reason = []

    if (len(POS_Tagged_Sentence) == 1): # Rule1, Rule3 and Rule5
        isQuestion, reason = checkRulesSet1(Sentence, POS_Tagged_Sentence)

    if (len(POS_Tagged_Sentence) == 2): # Rule1, Rule3 and Rule5
        isQuestion, reason = checkRulesSet2(Sentence, POS_Tagged_Sentence)

    if (len(POS_Tagged_Sentence) >= 3):  # Rule1, Rule3 and Rule5
        isQuestion, reason = checkRulesSet3(Sentence, POS_Tagged_Sentence)

    return isQuestion, reason
