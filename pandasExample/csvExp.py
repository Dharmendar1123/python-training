import pandas as pd

users = pd.read_csv('resources/email.csv')
df = pd.DataFrame(users, index=None)
# print(df.loc[0]["First name"])
print(df)