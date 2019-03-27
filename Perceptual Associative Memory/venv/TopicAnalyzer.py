from nltk.corpus import stopwords
#from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
from gensim.models.ldamodel import LdaModel
from gensim.corpora import Dictionary

stop = set(stopwords.words('english'))
exclude = set(punctuation)
#lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = ' '.join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    #normalized = " ".join(lemma.lemmatize(word) for word in doc.split())
    return punc_free #normalized



def getTopic(Text:str):
    topic_dict = {}
    print("text received : ", Text)

    doc_clean = [clean(Text).split()]
    # print("doc_clean : ", doc_clean)
    dictionary = Dictionary(doc_clean)
    # print("dictionary : ", dictionary)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # print("doc_term_matrix : ", doc_term_matrix)
    ldamodel = LdaModel(doc_term_matrix, num_topics=1, id2word = dictionary, passes=1)
    topics = ldamodel.print_topics(num_topics=1, num_words=1)
    topic = topics[0][1]
    topic = str(topic).split("*")
    probability = topic[0]
    term = topic[1]
    topic_dict["term"] = term
    topic_dict["probablity"] = probability

    print("Returning : ", topic_dict)

    return topic_dict

if __name__ == '__main__':
    # while True:
        # text = input("Enter Text: ")

        text = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
        # doc2 = "My father spends a lot of time driving my sister around to dance practice."
        # doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
        # doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
        # doc5 = "Health experts say that Sugar is not good for your lifestyle."

        topics = getTopic(text)
        print("Topic: ", topics)
