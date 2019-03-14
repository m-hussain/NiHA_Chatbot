def fix_i(tokenized_text):
    for count in range(len(tokenized_text)):
        if tokenized_text[count] == 'i':
            tokenized_text[count] = 'I'
    return tokenized_text

##TESTING INTERFACE##
if __name__ == '__main__':
    from nltk import word_tokenize
    from ContractionExpander import expandContraction

    while (True):
        text = input("Sentence : ")
        text = text.lower()

        print(text)
        text = expandContraction(text)

        print(text)

        tokenized = word_tokenize(text)

        tokenized = fix_i(tokenized)

        print(tokenized)

        #tagged = pos_tag(tokenized)
        #
        #ne_tagged = nltk.ne_chunk(tagged)

        #print(tagged)
        #print(tagged[-2][0])


        ##ne_tagged.draw()
        #
        #
        # if text.find("is your"):
        #     print()