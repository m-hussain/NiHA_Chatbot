from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize, pos_tag_sents, ne_chunk_sents

class PerceptualAssociativeMemory:

    def __init__(self):
        self.sensory_signal = self.getSensorySignal()
        self.opinosis_graph = self.getOpinosisGraph()
        self.sensory_text = self.getSensoryText()
        self.sentences = self.getSentences()
        self.words = self.getWords()
        self.pos_tagged_sentences = self.getPOSTaggedSentences()
        self.ne_taggedSentences = self.getNETaggedSentences()

        #self.

    def getSensorySignal(self):
        pass

    def getOpinosisGraph(self):
        pass

    def getSensoryText(self):
        pass

    def getSentences(self):
        sentences = sent_tokenize(self.sensory_text)
        return sentences

    def getWords(self):
        words = word_tokenize(self.sentences)
        return words

    def getPOSTaggedSentences(self):
        return pos_tag_sents(word_tokenize(sentence) for sentence in sent_tokenize(self.sensory_text))

    def getNETaggedSentences(self):
        pass

