import pandas as pd
from pathlib import Path

user = pd.DataFrame({
    'name':['nilesh', 'aditya', 'ashitosh', 'pawan'],
    'age':[23, 22, 24, 25],
    'tech':['GCP', 'Devops', 'Dev', 'Tester']
})
filePath = Path('resources/writeFile.csv')

user.to_csv(filePath, index=False)

df = pd.read_csv('resources/writeFile.csv')
print(df)