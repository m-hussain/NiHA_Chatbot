## DOCUMENTATION ##

"""""
Takes input as Text and returns Tags associated Text including all information about
Sentences and Words along with their word level tags 

For example if the Text comes "There is cat. Cat is cute."
Final Output would be 

sentences = \
    {
        0 : {
                "label"     : "There is cat",
                "words"     : {
                                    0 : {
                                            "word_label":   "There",
                                            "pos_tag"   :   "ab",
                                            "ne_tag"    :   "xy"
                                        },
                                    1 : {
                                            "word_label":   "is",
                                            "pos_tag"   :   "bc",
                                            "ne_tag"    :   "xz"
                                        },
                                    2 : {
                                            "word_label":   "cat",
                                            "pos_tag"   :   "cd",
                                            "ne_tag"    :   "zy"
                                        }
                                },
                "sentiment" : "positive",
                "person"    : "self",
                "location"  : "unknown",
                "timeStamp" : "timeStamp",
                "time"      : "tense"
            },
        1 : {
                "label"      : "cat is cute",
                "words"     : {
                                    0 : {
                                            "word_label":   "cat",
                                            "pos_tag"   :   "ab",
                                            "ne_tag"    :   "xy"
                                        },
                                    1 : {
                                            "word_label":   "is",
                                            "pos_tag"   :   "bc",
                                            "ne_tag"    :   "xz"
                                        },
                                    2 : {
                                            "word_label":   "cute",
                                            "pos_tag"   :   "cd",
                                            "ne_tag"    :   "zy"
                                        }
                                },
                "sentiment" : "positive",
                "person"    : "self",
                "location"  : "unknown",
                "timeStamp" : "timeStamp",
                "time"      : "tense"
            }
    }
    
# Try
# print(sentences[0]["label"])

"""""

def AssociateWordLevelTags(chunked_sentences) -> dict:
    tagged_text = {}

    sentence_count = 0
    for tree in chunked_sentences:
        words_tags = {}
        word_count = 0
        for child in tree:
            word_tags = {}
            if hasattr(child, 'label'):
                word_tags["word_label"] = child[0][0]
                word_tags["pos_tag"] = child[0][1]
                word_tags["ne_Tag"] = child.label()
                words_tags[word_count] = word_tags
                word_count += 1
            else:
                word_tags["word_label"] = child[0]
                word_tags["pos_tag"] = child[1]
                word_tags["ne_Tag"] = "null"
                words_tags[word_count] = word_tags
                word_count += 1
        tagged_text[sentence_count] = words_tags
        sentence_count += 1

    return tagged_text

if __name__ == '__main__':
    from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk_sents
    from I_Fix import fix_i
    from utilities import print_word_signal
    # with open('sample.txt', 'r') as f:
    #     document = f.read()

    # document = "My Name is Mahmood Hussain. i live in Lahore, Punjab, Pakistan. i study in COMSATS University Islamabad."
    document = "hello there. me good."

    sentences = sent_tokenize(document)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(fix_i(sentence)) for sentence in tokenized_sentences]
    chunked_sentences = ne_chunk_sents(tagged_sentences)

    tagged_text = AssociateWordLevelTags(chunked_sentences)

    print("tagged text: \n", tagged_text)

    # print_word_signal(tagged_text)

