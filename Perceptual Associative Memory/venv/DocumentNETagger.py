import nltk
import string

def tagText(document):
    print(document)
    #document = document.translate(str.maketrans('','',string.punctuation))
    #print(document)
    sentences = nltk.sent_tokenize(document)
    print(sentences)
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
                #print("word : ",child[0][0],", pos_tag : ",child[0][1], ", NE_Tag : ", child.label())
                #print()
                word_tags["word_label"] = child[0][0]
                word_tags["pos_tag"] = child[0][1]
                word_tags["ne_Tag"] = child.label()
                words_tags[word_count] = word_tags
                word_count += 1
            else:
                #print("word : ",child[0],", pos_tag : ",child[1], ", NE_Tag : ", "null")
                #print()
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

    tagged_text = tagText(document)

    print(tagged_text)