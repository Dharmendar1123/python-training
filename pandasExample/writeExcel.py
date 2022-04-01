import pandas as pd

user = pd.DataFrame({
    'name':['nilesh', 'aditya', 'ashitosh', 'pawan'],
    'age':[23, 22, 24, 25],
    'tech':['GCP', 'Devops', 'Dev', 'Tester']
})

user.to_excel('resources/output.xlsx')