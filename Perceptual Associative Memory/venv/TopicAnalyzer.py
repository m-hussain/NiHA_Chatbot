from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

import gensim
from gensim import corpora

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


topic_dict = {}

def getTopic(Text:str):

    #doc1 = Text

    text_document = Text



    doc_clean = [clean(text_document).split()]


    # Importing Gensim

    # Creating the term dictionary of our courpus, where every unique term is assigned an index.
    dictionary = corpora.Dictionary(doc_clean)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel

    # Running and Training LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=1, id2word = dictionary, passes=1)

    topics = ldamodel.print_topics(num_topics=1, num_words=1)

    print("topics : ", topics, "type : ", type(topics))

    topic = topics[0][1]

    topic = str(topic).split("*")

    probability = topic[0]
    term = topic[1]

    print("probability : ", probability, "\tterm : ", term)

    topic_dict["term"]=term
    topic_dict["probablity"] = probability

#     #['0.168*health + 0.083*sugar + 0.072*bad,'0.061*consume + 0.050*drive + 0.050*sister,'0.049*pressur + 0.049*father + 0.049*sister]
#


    return topic_dict
#
#
if __name__ == '__main__':
    while True:
        text = input("Enter Text: ")

        # doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
        # doc2 = "My father spends a lot of time driving my sister around to dance practice."
        # doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
        # doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
        # doc5 = "Health experts say that Sugar is not good for your lifestyle."

        topics = getTopic(text)
        print("Topics: ", topics)

