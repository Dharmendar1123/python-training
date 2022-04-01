import pandas as pd

user = {
    "name": ['aman', 'yash', 'raj', 'adi'],
    "age": ['22', '23', '19', '25']
}

df = pd.DataFrame(user)
# print(df)

calendar = {
    "month": ['jan', 'feb', 'march', 'april'],
    "days": [31, 28, 31, 30]
}

df1 = pd.DataFrame(calendar, index=[1, 2, 3, 4])
print(df1)