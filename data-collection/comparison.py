import pandas as pd


allTweets = pd.read_csv("datasets/regex.csv")

accounts = pd.read_csv("datasetse/accounts.csv")

celebsMbti = pd.read_csv("datasets/newmbti.csv")

namesMBTI = celebsMbti['name']


filtered_accounts = accounts[accounts['name'].isin(namesMBTI)]

accounts = filtered_accounts