import os
import pandas as pd


folder = 'twitter-celebrity-tweets-data'


dataframes = []


for filename in os.listdir(folder):
    if filename.endswith('.csv'):
        file = os.path.join(folder, filename)
        df = pd.read_csv(file)
        df.drop(['twitter_id','date'], axis=1, inplace=True)
        df['name'] = filename

        

        dataframes.append(df)

concatenated_df = pd.concat(dataframes, ignore_index=True)

outputname = 'allTweets.csv'
concatenated_df.to_csv(outputname, index=False)

