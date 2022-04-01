import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')

new_workOut = workOut.sort_index()
# print(new_workOut)

sortByValue_WorkOut = workOut.sort_values(by='Pulse')
# print(sortByValue_WorkOut)

rank_workOut = workOut['Pulse'].rank()
# print(rank_workOut)


df = workOut
df['Pulse'] = df['Pulse'].rank()
# a = df.sort_values(by='Pulse') #after ranking the pulse sorting them
# print(df)

descDuration = workOut.sort_values(by="Duration", ascending=False)
# print(descDuration)

dateRank = workOut
dateRank['Date'] = dateRank['Date'].rank()
print(dateRank)