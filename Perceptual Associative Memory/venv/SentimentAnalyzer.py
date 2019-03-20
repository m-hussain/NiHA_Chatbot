from nltk.sentiment.vader import SentimentIntensityAnalyzer


def getSentimentsScores(Sentence):
    s = SentimentIntensityAnalyzer()
    scores = s.polarity_scores(Sentence)
    scores1 = scores.copy()
    for key in scores1:
        if key is 'compound':
            scores1.pop('compound')
            break
    return scores, scores1

def getSentiment(Sentence):
    sentiScore = getSentimentsScores(Sentence)[1]
    maxValue = max(sentiScore.values())
    for key, value in sentiScore.items():
        if value is maxValue:
            return key


#Testing Interface
if __name__ == '__main__':
    while(True):
        #sentiment   = Sentiment()
        sentence    = input("Sentence : ")
        senti_tags  = getSentimentsScores(sentence)
        print(senti_tags)

        maxSentiScore = getSentiment(sentence)
        print(maxSentiScore)

