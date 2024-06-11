import pandas as pd


df = pd.read_csv("datasets/mbti_1.csv")

df['posts'] = df['posts'].str.split(r'\|\|\|')


dfexplode = df.explode('posts').reset_index(drop=True)


dfexplode.to_csv("mbtisorted.csv",index = False)
