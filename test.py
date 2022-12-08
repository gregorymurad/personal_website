import pandas as pd

df = pd.read_csv("Logs/universities-comparison.csv")
df.set_index('Subjects')

print(df)
print(len(df.iloc[0,1:]))
print(df.iloc[0,1:].sum()/len(df.iloc[0,1:]))

df['mean'] =df.iloc[:,1:].mean(axis=1)
print(df)