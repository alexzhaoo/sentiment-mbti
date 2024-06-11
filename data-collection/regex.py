import pandas as pd
import re


df = pd.read_csv("datasets/englishdataset.csv")

def cleandf(df):
    cleanedTweets = []

    for tweet in df['tweet']:
        if isinstance(tweet, bytes):
            tweet = tweet.decode('utf-8', errors='ignore')

        # Remove URLs
        tweet = re.sub(r'http\S+', '', tweet)

        # Remove hexadecimal representations
        tweet = re.sub(r'\\x[a-fA-F0-9]{2}', '', tweet)

        # Remove non-word characters
        tweet = re.sub(r'[^\w\s]', '', tweet)

        # Remove extra spaces
        tweet = re.sub(r'\s+', ' ', tweet).strip()

        cleanedTweets.append(tweet)

    df['tweet'] = cleanedTweets


cleandf(df)


df.to_csv("regex.csv", index=False)
