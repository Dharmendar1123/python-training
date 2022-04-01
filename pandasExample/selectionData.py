import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')

#print(workOut.loc[1]) #get one row of DataFrame

#print(workOut[1:5]) # get the subset of the DataFrame

#print(workOut.iloc[1,3]) #get value from 1st row and 3rd column

#print(workOut.loc[1,'Pulse']) #get Pulse value from row 1st

filterWorkOut = workOut[workOut['Pulse'] > 105] #filter Data whose pulse value is greater than 105
print(filterWorkOut)