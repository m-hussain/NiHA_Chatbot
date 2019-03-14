from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Sentiment:

    def getSentimentsScores(self, Sentence):
        s = SentimentIntensityAnalyzer()
        scores = s.polarity_scores(Sentence)
        scores1 = scores.copy()
        for key in scores1:
            if key is 'compound':
                scores1.pop('compound')
                break
        return scores, scores1

    def getSentiment(self, Sentence):
        sentiScore = self.getSentimentsScores(Sentence)[1]
        maxValue = max(sentiScore.values())
        for key, value in sentiScore.items():
            if value is maxValue:
                return key


#Testing Interface
while(True):
    sentiment   = Sentiment()
    sentence    = input("Sentence : ")
    senti_tags  = sentiment.getSentimentsScores(sentence)
    print(senti_tags)

    maxSentiScore = sentiment.getSentiment(sentence)
    print(maxSentiScore)

