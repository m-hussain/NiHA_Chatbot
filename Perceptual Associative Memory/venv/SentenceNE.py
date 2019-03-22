def setSentNE(chunked_sentences):
    tagged_text = {}

    sentence_count = 0
    for tree in chunked_sentences:
        phrases_tags = {}
        phrase_count = 0
        for child in tree:
            phrase_tags = {}
            if hasattr(child, 'label'):
                #print("labeled_child : ", child)
                phrase = []
                for count in range(len(child)):
                    phrase.append(child[count][0])
                #print(phrase)
                phrase = " ".join(phrase)
                #print(phrase)
                phrase_tags["phrase_label"] = phrase
                #word_tags["pos_tag"] = child[0][1]
                phrase_tags["ne_Tag"] = child.label()
                phrases_tags[phrase_count] = phrase_tags
                phrase_count += 1
            # else:
            #     word_tags["word_label"] = child[0]
            #     word_tags["pos_tag"] = child[1]
            #     word_tags["ne_Tag"] = "null"
            #     words_tags[word_count] = word_tags
            #     word_count += 1
        tagged_text[sentence_count] = phrases_tags
        sentence_count += 1

    return tagged_text



if __name__ == '__main__':
    from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk_sents
    from I_Fix import fix_i
    from utilities import print_word_signal
    # with open('sample.txt', 'r') as f:
    #     document = f.read()

    document = "My Name is Mahmood Hussain. i live in Lahore, Punjab, Pakistan. i study in COMSATS University Islamabad."
    # document = "hello there. me good."

    sentences = sent_tokenize(document)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(fix_i(sentence)) for sentence in tokenized_sentences]
    chunked_sentences = ne_chunk_sents(tagged_sentences)

    tagged_text = setSentNE(chunked_sentences)

    print("tagged text: \n", tagged_text)

    from utilities import print_phrase_signal

    print_phrase_signal(tagged_text)
