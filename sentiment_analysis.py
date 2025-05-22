
import pandas as pd
from textblob import TextBlob

# Load the feedback data
df = pd.read_csv('data/sample_feedback.csv')

# Define function to classify sentiment
def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return 'positive'
    elif polarity < -0.2:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment classification
df['sentiment'] = df['feedback'].apply(classify_sentiment)

# Save output
df.to_csv('data/feedback_with_sentiment.csv', index=False)

print("✅ Sentiment classification complete. Output saved to 'data/feedback_with_sentiment.csv'")
