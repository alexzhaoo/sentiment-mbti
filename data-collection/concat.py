import pandas as pd


df = pd.read_csv("datasets/filteredTweets.csv")

def remove_first_b(tweet):
    if isinstance(tweet, str) and tweet.startswith('b'):
        return tweet[1:]
    return tweet


df['tweet'] = df['tweet'].apply(remove_first_b)




df['tweet'] = df.groupby('name')['tweet'].transform(lambda x: ' || '.join(x))


df = df.drop_duplicates(subset=['name'])

df = df.reset_index(drop=True)


df.to_csv("datasets/concatenatedTweets.csv", index=False)
