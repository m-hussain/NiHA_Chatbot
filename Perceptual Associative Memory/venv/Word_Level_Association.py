import nltk

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

def AssociateWordLevelTags(text):
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)

    tagged_text = {}
    sentence_count = 0
    for tree in chunked_sentences:
        #tagged_text[sentence_count] = tree
        print("tree : ", tree)
        words_tags = {}
        word_count = 0
        for child in tree:
            print("child : ",child)
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
    # with open('sample.txt', 'r') as f:
    #     document = f.read()

    document = "My Name is Mahmood Hussain. I live in Lahore, Punjab, Pakistan. I study in COMSATS University Islamabad."

    tagged_text = AssociateWordLevelTags(document)

    print(tagged_text)