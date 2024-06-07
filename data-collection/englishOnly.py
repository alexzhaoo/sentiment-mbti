import pandas as pd
import re
from langdetect import detect, DetectorFactory

df = pd.read_csv("datasets/regex.csv")

DetectorFactory.seed = 0

# def cleandf(df):

#     tweets = df['tweet']

#     cleanedTweets = []

#     for tweet in tweets:   
#         if isinstance(tweet,bytes):
#             tweet = tweet.decode('uft-8', errors = 'ignore')

#         tweet = re.sub(r'http\S+', '', tweet)

#         tweet = re.sub(r'[^\w\s]', '', tweet)

#         tweet = re.sub(r'\s+', ' ', tweet).strip()

#         cleanedTweets.append(tweet)

#     df['tweet'] = cleanedTweets    
    
#     return 0


def langdetect(tweet):
    try: 
        return detect(tweet) == 'en'
    except:
        return False
    
# cleandf(df)

englishmask = df['tweet'].apply(langdetect)

dfenglish = df[englishmask]

dfenglish.to_csv("finalenglish.csv",index = False)















