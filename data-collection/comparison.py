import pandas as pd


allTweets = pd.read_csv("datasets/regex.csv")

accounts = pd.read_csv("datasets/accounts.csv")

celebsMbti = pd.read_csv("datasets/newmbti.csv")

celebsMbti['name'] = celebsMbti['name'].str.lower()
accounts['name'] = accounts['name'].str.lower()


namesMBTI = celebsMbti['name']


def truncate(name):
    return name.split('.')[0].strip()

filtered_accounts = pd.merge(accounts, celebsMbti[['name', 'personality']], on='name', how='left')

filtered_accounts = filtered_accounts.dropna(subset = ["personality"])

accounts = filtered_accounts

allTweets['name'] = allTweets['name'].apply(truncate)

mask = allTweets['name'].isin(filtered_accounts['twitter'])

filteredTweets = allTweets[mask]

filteredTweets.to_csv("filteredTweets.csv", index = False)


