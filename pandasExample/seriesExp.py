import pandas as pd

fruits = ['apple', 'mango', 'banana', 'cherry']
sr = pd.Series(fruits)
print("Before")
print(sr)
sr[0] = 'coconut'
# print(sr[0])
print("After")
print(sr)
# print()

sr1 = pd.Series(['one', 'two', 'three', 'four', 'five'], index=[1,2,3,4,5])
# print(sr1)
# print()

days = {'day1': 'mon', 'day2': 'tue', 'day3': 'wed', 'day4': 'thur', 'day5': 'fri'}
sr2 = pd.Series(days)
# print(sr2)

