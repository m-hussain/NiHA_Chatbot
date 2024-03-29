import nltk
# with open('sample.txt', 'r') as f:
#     sample = f.read()

sample = "My Name is Mahmood Hussain. I live in Lahore, Punjab, Pakistan. I study in COMSATS University Islamabad."

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)

print(tagged_sentences)
print(chunked_sentences)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

entity_names = []
for tree in chunked_sentences:
    print(tree)
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print(entity_names)

