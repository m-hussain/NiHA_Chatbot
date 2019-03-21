def isRule1(Sentence: str):
    description = "Found Exclamation Mark at the end"
    if (Sentence.endswith("!")):
        return True, description
    else:
        return False, "rule failed"


def isExclamation(Sentence: str):
    isExclamation = False

    reason = []

    passed, description = isRule1(Sentence)
    if passed:
        reason.append(description)
        isExclamation = True

    return isExclamation, reason
