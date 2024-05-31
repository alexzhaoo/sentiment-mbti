import pandas as pd
import re


df = pd.read_csv("datasets/englishdataset.csv")


def cleandf(df):

    tweets = df['tweet']

    cleanedTweets = []

    for tweet in tweets:   
        if isinstance(tweet,bytes):
            tweet = tweet.decode('uft-8', errors = 'ignore')

        tweet = re.sub(r'http\S+', '', tweet)

        tweet = re.sub(r'[^\w\s]', '', tweet)

        tweet = re.sub(r'\s+', ' ', tweet).strip()

        cleanedTweets.append(tweet)

    df['tweet'] = cleanedTweets    
    
    return 0

cleandf(df)


df.to_csv("regex.csv", index= False)




