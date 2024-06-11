import pandas as pd


df = pd.read_csv("datasets/MBTI_dataset_100.csv")
df2 = pd.read_csv("datasets/regex.csv")
df.drop([
    'total votes',
    'first letter votes percentage',
    'second letter votes percentage',
    'third letter votes percentage',
    'fourth letter votes percentage',
    'first function',
    'second function',
    'third function',
    'fourth function',
    'Instinctual_Variant_type',
    'Tritype_type',
    'Socionics_type',
    'Big5_type',
    'Attitudinal_Psyche_type',
    'Temperaments_type',
    'fourletters_type_votes',
    'Instinctual_Variant_total_votes',
    'Tritype_total_votes',
    'Socionics_total_votes',
    'Big5_total_votes',
    'Attitudinal_Psyche_total_votes',
    'Temperaments_total_votes',
    'Instinctual_Variant_type_votes',
    'Tritype_type_votes',
    'Socionics_type_votes',
    'Big5_type_votes',
    'Attitudinal_Psyche_type_votes',
    'Temperaments_type_votes'
], axis=1, inplace=True)


names = df['name']

def truncate(name):
    return name.split('(')[0].strip()

df['name'] = df['name'].apply(truncate)

df.to_csv("newmbti.csv",index = False)



