from posTagger import tagPOS
sentence = input("Sentence : ")
posTaggedSentence = tagPOS(sentence)

print(posTaggedSentence)


def fingTupleContainsWord(word):
    tupleIndex = -1
    count = 0
    for tuple in posTaggedSentence:
        if str(tuple[0]).startswith(word):
            tupleIndex = count
            break
        count+=1
    return tupleIndex

# if sentence.find("if")!=-1:
#     print("yes")
#     print(sentence.find("if"))



#print(str(posTaggedSentence))

#print(index)

