from Sentence_Level_Association import AssociateSentenceLevelTags
from utilities import print_sentences_signal

class PerceptualAssociativeMemory:
    sensorySignal = {}
    PAM_Signal = {}

    # def __init__(self):
        # self.sensory_signal = self.getSensorySignal(sensorySignal)
        # self.opinosis_graph = self.getOpinosisGraph()
        # self.sensory_text = self.getSensoryText()
        # self.sentences = self.getSentences()
        # self.words = self.getWords()
        # self.pos_tagged_sentences = self.getPOSTaggedSentences()
        # self.ne_taggedSentences = self.getNETaggedSentences()

    # def getSensorySignal(self):
    #     pass
    # def getOpinosisGraph(self):
    #     pass
    # def getSensoryText(self):
    #     pass
    # def getSentences(self):
    #     pass
    # def getWords(self):
    #     pass
    # def getPOSTaggedSentences(self):
    #     pass
    # def getNETaggedSentences(self):
    #     pass

    def getSensorySignal(self):
        return PerceptualAssociativeMemory.sensorySignal

    def setSensorySignal(self, sensorySignal:dict):
        PerceptualAssociativeMemory.sensorySignal = sensorySignal

    def getTextFromSensorySignal(self):
        sensorySignal = self.getSensorySignal()
        text = sensorySignal["text"]
        return text

    def processAssociations(self):
        text = self.getTextFromSensorySignal()
        PerceptualAssociativeMemory.PAM_Signal = AssociateSentenceLevelTags(text)

    def printSignal(self, signal:dict):
        print_sentences_signal(signal)

    def getPAM_Signal(self):
        return PerceptualAssociativeMemory.PAM_Signal



def __main__():
    # sensoryData = {"text":"This is sample text. My name is Mahmood Hussain"}
    sensoryData = {"text":"John saw Bob talk to Alice yesterday. Alice met Susan twice."}

    PAM = PerceptualAssociativeMemory()
    PAM.setSensorySignal(sensoryData)
    PAM.processAssociations()
    pamSignal = PAM.getPAM_Signal()
    PAM.printSignal(pamSignal)

if __name__ == '__main__':
    __main__()