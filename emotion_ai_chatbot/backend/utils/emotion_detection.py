from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def detect_emotion(text):
    # TextBlob analysis
    tb_analysis = TextBlob(text)
    
    # NLTK VADER analysis
    vader_scores = sia.polarity_scores(text)
    
    # Combine both analyses
    compound_score = (vader_scores['compound'] + tb_analysis.sentiment.polarity) / 2
    
    if compound_score > 0.3:
        return 'happy'
    elif compound_score < -0.3:
        if vader_scores['neg'] > 0.5:
            return 'angry'
        return 'sad'
    else:
        return 'neutral'