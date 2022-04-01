import pandas as pd

workOut = pd.read_csv('resources/workoutData.csv')

funWorkOut = workOut.apply(lambda x: x*2) #multiply every value with 2
# print(funWorkOut)

twoPulseWorkOut = workOut['Calories'].apply(lambda x: x*2) #double the value of Calories
print(twoPulseWorkOut)
