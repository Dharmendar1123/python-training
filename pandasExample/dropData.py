import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')
delete_workOut = workOut.drop([0, 1, 2]) #delete row 0, 1 and 2
# print(delete_workOut)

null_workOut = workOut.dropna() #delete row with null values 18, 22 and 28
# print(null_workOut)

new_workOut = workOut.drop('Date', axis=1) #delete column Date
print(new_workOut)

# print(workOut)
