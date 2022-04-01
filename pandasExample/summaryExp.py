import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')

newWorkOut = workOut.dropna()
sumWorkOut = newWorkOut.sum()  # gives the total value of a column if number.
# print(sumWorkOut)

cWorkOut = workOut['Pulse'].cumsum() #give Cumulative sum of a column with number value
# print(cWorkOut)

minWorkOut = workOut['Pulse'].min() #give minimum value from the column
# print(minWorkOut)

maxWorkOut = workOut['Pulse'].max() #give maximum value from the column
# print(maxWorkOut)

descWorkOut = workOut.describe() #gives various values like mean, min, max, 25% etc of a column
# print(descWorkOut)

meanWorkOut = workOut.mean() # gives mean of the column
# print(meanWorkOut)

medianWorkOut = workOut.median()
print(medianWorkOut)